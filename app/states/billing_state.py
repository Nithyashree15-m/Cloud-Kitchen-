import reflex as rx
from typing import TypedDict
from faker import Faker
import random

fake = Faker()


class Invoice(TypedDict):
    id: str
    customer: str
    amount: float
    status: str
    date: str
    method: str


class BillingState(rx.State):
    invoices: list[Invoice] = []
    channel_data: list[dict[str, str | int]] = [
        {"name": "UberEats", "value": 4500},
        {"name": "DoorDash", "value": 3800},
        {"name": "Direct", "value": 2100},
    ]

    @rx.event
    def setup_billing(self):
        if len(self.invoices) > 0:
            return
        statuses = ["Paid", "Paid", "Paid", "Pending", "Overdue", "Refunded"]
        methods = ["Credit Card", "Stripe", "PayPal"]
        self.invoices = []
        for i in range(12):
            self.invoices.append(
                {
                    "id": f"INV-{3000 + i}",
                    "customer": fake.name(),
                    "amount": round(random.uniform(25.0, 150.0), 2),
                    "status": random.choice(statuses),
                    "date": fake.date_this_month().strftime("%Y-%m-%d"),
                    "method": random.choice(methods),
                }
            )

    @rx.var
    def today_revenue(self) -> float:
        return sum(
            (inv["amount"] for inv in self.invoices if inv["status"] == "Paid")
        )

    @rx.var
    def pending_amount(self) -> float:
        return sum(
            (
                inv["amount"]
                for inv in self.invoices
                if inv["status"] == "Pending"
            )
        )