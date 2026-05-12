import reflex as rx
from typing import TypedDict
from faker import Faker
import random

fake = Faker()


class Delivery(TypedDict):
    order_id: str
    customer: str
    driver: str
    status: str
    eta: str
    platform: str


class DeliveryState(rx.State):
    deliveries: list[Delivery] = []

    @rx.event
    def setup_deliveries(self):
        if len(self.deliveries) > 0:
            return
        statuses = ["Assigned", "En Route", "Picked Up"]
        platforms = ["UberEats", "DoorDash", "Direct"]
        drivers = ["Mike R.", "Sarah J.", "David T.", "Alex K."]
        self.deliveries = []
        for i in range(8):
            self.deliveries.append(
                {
                    "order_id": f"ORD-{2000 + i}",
                    "customer": fake.name(),
                    "driver": random.choice(drivers),
                    "status": random.choice(statuses),
                    "eta": f"{random.randint(5, 25)} mins",
                    "platform": random.choice(platforms),
                }
            )

    @rx.var
    def active_deliveries_count(self) -> int:
        return len(self.deliveries)