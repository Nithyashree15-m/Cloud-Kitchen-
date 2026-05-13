import reflex as rx
from typing import TypedDict
from faker import Faker
import random
import json
import logging

fake = Faker()


class StaffMember(TypedDict):
    id: str
    name: str
    role: str
    email: str
    phone: str
    status: str


class StaffState(rx.State):
    staff: list[StaffMember] = []
    staff_storage: str = rx.LocalStorage(name="cloud_kitchen_staff", sync=True)
    show_modal: bool = False
    form_data: dict[str, str] = {
        "name": "",
        "email": "",
        "phone": "",
        "role": "Server",
    }

    @rx.event
    def setup_staff(self):
        if self.staff_storage:
            try:
                data = json.loads(self.staff_storage)
                if data:
                    self.staff = data
                    return
            except:
                logging.exception("Unexpected error")
        if len(self.staff) > 0:
            return
        roles = ["Admin", "Manager", "Cook", "Server"]
        self.staff = []
        for i in range(8):
            role = random.choice(roles)
            self.staff.append(
                {
                    "id": f"EMP-{1000 + i}",
                    "name": fake.name(),
                    "role": role,
                    "email": fake.email(),
                    "phone": fake.phone_number()[:12],
                    "status": random.choice(["Active", "Off-duty"]),
                }
            )
        self.staff_storage = json.dumps(self.staff)

    @rx.var
    def total_staff(self) -> int:
        return len(self.staff)

    @rx.var
    def on_duty_count(self) -> int:
        return sum((1 for s in self.staff if s["status"] == "Active"))

    @rx.var
    def manager_count(self) -> int:
        return sum((1 for s in self.staff if s["role"] in ["Admin", "Manager"]))

    @rx.var
    def cook_count(self) -> int:
        return sum((1 for s in self.staff if s["role"] == "Cook"))

    @rx.event
    def toggle_modal(self):
        self.show_modal = not self.show_modal
        if self.show_modal:
            self.form_data = {
                "name": "",
                "email": "",
                "phone": "",
                "role": "Server",
            }

    @rx.event
    def handle_submit(self, data: dict):
        new_staff = StaffMember(
            id=f"EMP-{1000 + len(self.staff)}",
            name=str(data.get("name", "")),
            role=str(data.get("role", "Server")),
            email=str(data.get("email", "")),
            phone=str(data.get("phone", "")),
            status="Off-duty",
        )
        self.staff.append(new_staff)
        self.staff_storage = json.dumps(self.staff)
        self.show_modal = False