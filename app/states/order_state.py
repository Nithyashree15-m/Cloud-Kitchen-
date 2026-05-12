import reflex as rx
from typing import TypedDict
from faker import Faker
import random

fake = Faker()


class Order(TypedDict):
    id: str
    customer: str
    items: str
    status: str
    channel: str
    time: str
    total: float


class OrderState(rx.State):
    orders: list[Order] = []
    status_filter: str = "All"
    search_query: str = ""
    selected_order_id: str = ""

    @rx.event
    def setup_sample_orders(self):
        if len(self.orders) > 0:
            return
        channels = ["UberEats", "DoorDash", "Direct"]
        statuses = ["New", "Accepted", "Preparing", "Ready", "Delivered"]
        self.orders = []
        for i in range(20):
            self.orders.append(
                {
                    "id": f"ORD-{1000 + i}",
                    "customer": fake.name(),
                    "items": f"{random.randint(1, 4)}x {fake.word().capitalize()} Burger, {random.randint(1, 2)}x Fries",
                    "status": random.choice(statuses),
                    "channel": random.choice(channels),
                    "time": f"{random.randint(0, 23)}:{random.randint(10, 59)}",
                    "total": round(random.uniform(15.0, 85.0), 2),
                }
            )

    @rx.var
    def filtered_orders(self) -> list[Order]:
        filtered = self.orders
        if self.status_filter != "All":
            filtered = [
                o for o in filtered if o["status"] == self.status_filter
            ]
        if self.search_query:
            query = self.search_query.lower()
            filtered = [
                o
                for o in filtered
                if query in o["customer"].lower() or query in o["id"].lower()
            ]
        return filtered

    @rx.var
    def selected_order(self) -> Order:
        for o in self.orders:
            if o["id"] == self.selected_order_id:
                return o
        return {
            "id": "",
            "customer": "",
            "items": "",
            "status": "",
            "channel": "",
            "time": "",
            "total": 0.0,
        }

    @rx.event
    def set_status_filter(self, status: str):
        self.status_filter = status

    @rx.event
    def set_search_query(self, query: str):
        self.search_query = query

    @rx.event
    def select_order(self, order_id: str):
        self.selected_order_id = order_id

    @rx.event
    def update_order_status(self, order_id: str, new_status: str):
        self.orders = [
            o | {"status": new_status} if o["id"] == order_id else o
            for o in self.orders
        ]
        if self.selected_order_id == order_id:
            yield rx.toast(f"Order {order_id} moved to {new_status}")