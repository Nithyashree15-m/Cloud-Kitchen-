import reflex as rx
from typing import TypedDict


class Notification(TypedDict):
    id: str
    title: str
    message: str
    time: str
    unread: bool


class NotificationState(rx.State):
    notifications: list[Notification] = [
        {
            "id": "1",
            "title": "New Order",
            "message": "UberEats order #4592 received",
            "time": "2m ago",
            "unread": True,
        },
        {
            "id": "2",
            "title": "Low Stock",
            "message": "Chicken Breast below reorder level",
            "time": "15m ago",
            "unread": True,
        },
        {
            "id": "3",
            "title": "System Update",
            "message": "Menu sync completed successfully",
            "time": "1h ago",
            "unread": False,
        },
    ]
    show_notifications: bool = False

    @rx.var
    def unread_count(self) -> int:
        return sum((1 for n in self.notifications if n["unread"]))

    @rx.event
    def toggle_notifications(self):
        self.show_notifications = not self.show_notifications

    @rx.event
    def mark_all_read(self):
        self.notifications = [n | {"unread": False} for n in self.notifications]