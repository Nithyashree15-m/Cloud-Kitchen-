import reflex as rx
from typing import TypedDict
from faker import Faker
import random
import json
import logging

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
    delivery_storage: str = rx.LocalStorage(
        name="cloud_kitchen_deliveries", sync=True
    )

    @rx.event
    def setup_deliveries(self):
        if self.delivery_storage:
            try:
                data = json.loads(self.delivery_storage)
                if data:
                    self.deliveries = data
                    return
            except:
                logging.exception("Unexpected error")
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
        self.delivery_storage = json.dumps(self.deliveries)

    @rx.var
    def active_deliveries_count(self) -> int:
        return len(self.deliveries)