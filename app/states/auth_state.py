import reflex as rx
from typing import TypedDict
import json
import logging
import uuid
import re
from datetime import datetime


class User(TypedDict):
    id: str
    name: str
    email: str
    role: str
    created_at: str
    password: str


class AuthState(rx.State):
    users_storage: str = rx.LocalStorage(
        "", name="cloud_kitchen_users", sync=True
    )
    session_storage: str = rx.LocalStorage(
        "", name="cloud_kitchen_session", sync=True
    )
    error_message: str = ""
    is_loading: bool = False

    @rx.var
    def is_authenticated(self) -> bool:
        if not self.session_storage:
            return False
        try:
            data = json.loads(self.session_storage)
            return bool(data.get("email"))
        except Exception:
            logging.exception("Unexpected error")
            return False

    @rx.var
    def current_user_name(self) -> str:
        if not self.session_storage:
            return ""
        try:
            data = json.loads(self.session_storage)
            return data.get("name", "")
        except Exception:
            logging.exception("Unexpected error")
            return ""

    @rx.var
    def current_user_email(self) -> str:
        if not self.session_storage:
            return ""
        try:
            data = json.loads(self.session_storage)
            return data.get("email", "")
        except Exception:
            logging.exception("Unexpected error")
            return ""

    @rx.var
    def current_user_role(self) -> str:
        if not self.session_storage:
            return ""
        try:
            data = json.loads(self.session_storage)
            return data.get("role", "")
        except Exception:
            logging.exception("Unexpected error")
            return ""

    def _load_users(self) -> list[dict]:
        if not self.users_storage:
            return []
        try:
            return json.loads(self.users_storage)
        except Exception:
            logging.exception("Failed to load users")
            return []

    @rx.event
    def check_auth(self):
        if not self.is_authenticated:
            return rx.redirect("/login")

    @rx.event
    def check_already_authed(self):
        if self.is_authenticated:
            return rx.redirect("/")

    @rx.event
    def clear_error(self):
        self.error_message = ""

    @rx.event
    def handle_register(self, form_data: dict):
        self.error_message = ""
        name = str(form_data.get("name", "")).strip()
        email = str(form_data.get("email", "")).strip().lower()
        password = str(form_data.get("password", ""))
        confirm = str(form_data.get("confirm_password", ""))
        if not name or not email or not password or not confirm:
            self.error_message = "All fields are required."
            return
        if not re.match("^[^@\\s]+@[^@\\s]+\\.[^@\\s]+$", email):
            self.error_message = "Please enter a valid email address."
            return
        if len(password) < 6:
            self.error_message = "Password must be at least 6 characters."
            return
        if password != confirm:
            self.error_message = "Passwords do not match."
            return
        users = self._load_users()
        if any(u.get("email", "").lower() == email for u in users):
            self.error_message = "An account with this email already exists."
            return
        new_user: User = {
            "id": str(uuid.uuid4()),
            "name": name,
            "email": email,
            "role": "Manager",
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "password": password,
        }
        users.append(new_user)
        self.users_storage = json.dumps(users)
        self.session_storage = json.dumps(
            {
                "id": new_user["id"],
                "name": new_user["name"],
                "email": new_user["email"],
                "role": new_user["role"],
            }
        )
        yield rx.toast(f"Welcome, {name}!")
        return rx.redirect("/")

    @rx.event
    def handle_login(self, form_data: dict):
        self.error_message = ""
        email = str(form_data.get("email", "")).strip().lower()
        password = str(form_data.get("password", ""))
        if not email or not password:
            self.error_message = "Email and password are required."
            return
        users = self._load_users()
        match = None
        for u in users:
            if (
                u.get("email", "").lower() == email
                and u.get("password") == password
            ):
                match = u
                break
        if not match:
            self.error_message = "Invalid email or password."
            return
        self.session_storage = json.dumps(
            {
                "id": match["id"],
                "name": match["name"],
                "email": match["email"],
                "role": match.get("role", "Manager"),
            }
        )
        yield rx.toast(f"Welcome back, {match['name']}!")
        return rx.redirect("/")

    @rx.event
    def logout(self):
        self.session_storage = ""
        self.error_message = ""
        return rx.redirect("/login")