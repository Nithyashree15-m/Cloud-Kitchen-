import reflex as rx
from typing import TypedDict
import random


class DashboardState(rx.State):
    kpis: dict[str, dict[str, str | float | bool]] = {
        "orders": {
            "label": "Total Orders",
            "value": "142",
            "change": "+12.5%",
            "trend": True,
        },
        "revenue": {
            "label": "Revenue Today",
            "value": "₹4,280",
            "change": "+8.2%",
            "trend": True,
        },
        "prep_time": {
            "label": "Avg Prep Time",
            "value": "14.2m",
            "change": "-2.1%",
            "trend": True,
        },
        "active": {
            "label": "Active Orders",
            "value": "18",
            "change": "+4",
            "trend": True,
        },
    }
    sales_data: list[dict[str, str | int]] = [
        {"day": "Mon", "sales": 3200},
        {"day": "Tue", "sales": 3800},
        {"day": "Wed", "sales": 3500},
        {"day": "Thu", "sales": 4100},
        {"day": "Fri", "sales": 5200},
        {"day": "Sat", "sales": 6100},
        {"day": "Sun", "sales": 5800},
    ]
    peak_hours: list[dict[str, str | int]] = [
        {"hour": "11am", "orders": 12},
        {"hour": "12pm", "orders": 45},
        {"hour": "1pm", "orders": 38},
        {"hour": "2pm", "orders": 15},
        {"hour": "5pm", "orders": 22},
        {"hour": "6pm", "orders": 58},
        {"hour": "7pm", "orders": 64},
        {"hour": "8pm", "orders": 42},
    ]
    top_items: list[dict[str, str | int]] = [
        {"rank": 1, "name": "Classic Cheeseburger", "sold": 124},
        {"rank": 2, "name": "Truffle Fries", "sold": 98},
        {"rank": 3, "name": "Spicy Chicken Sando", "sold": 86},
        {"rank": 4, "name": "Vanilla Milkshake", "sold": 54},
        {"rank": 5, "name": "Garden Salad", "sold": 42},
    ]
    recent_activity: list[dict[str, str]] = [
        {
            "user": "System",
            "action": "New UberEats order #4521",
            "time": "2 mins ago",
        },
        {
            "user": "Chef Mario",
            "action": "Marked #4518 as Ready",
            "time": "8 mins ago",
        },
        {
            "user": "Driver",
            "action": "Order #4510 picked up",
            "time": "14 mins ago",
        },
        {
            "user": "System",
            "action": "DoorDash order #4520 received",
            "time": "22 mins ago",
        },
    ]