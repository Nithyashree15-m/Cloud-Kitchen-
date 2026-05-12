import reflex as rx
from typing import TypedDict
from faker import Faker
import random

fake = Faker()


class Customer(TypedDict):
    id: str
    name: str
    email: str
    phone: str
    total_orders: int
    total_spent: float
    last_order: str
    is_vip: bool


class CustomerState(rx.State):
    customers: list[Customer] = []
    search_query: str = ""

    @rx.event
    def setup_customers(self):
        if len(self.customers) > 0:
            return
        self.customers = []
        for i in range(15):
            orders = random.randint(1, 50)
            self.customers.append(
                {
                    "id": f"CUS-{1000 + i}",
                    "name": fake.name(),
                    "email": fake.email(),
                    "phone": fake.phone_number()[:12],
                    "total_orders": orders,
                    "total_spent": round(
                        orders * random.uniform(15.0, 45.0), 2
                    ),
                    "last_order": fake.date_this_year().strftime("%Y-%m-%d"),
                    "is_vip": orders > 20,
                }
            )

    @rx.var
    def filtered_customers(self) -> list[Customer]:
        if not self.search_query:
            return self.customers
        q = self.search_query.lower()
        return [
            c
            for c in self.customers
            if q in c["name"].lower() or q in c["email"].lower()
        ]

    @rx.var
    def total_customers(self) -> int:
        return len(self.customers)

    @rx.var
    def vip_count(self) -> int:
        return sum((1 for c in self.customers if c["is_vip"]))

    @rx.var
    def avg_order_value(self) -> float:
        if not self.customers:
            return 0.0
        total_spent = sum((c["total_spent"] for c in self.customers))
        total_orders = sum((c["total_orders"] for c in self.customers))
        return round(total_spent / total_orders, 2) if total_orders > 0 else 0.0

    @rx.event
    def set_search_query(self, query: str):
        self.search_query = query