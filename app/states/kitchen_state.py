import reflex as rx
from typing import TypedDict
from datetime import datetime
from app.states.order_state import OrderState, Order


class KitchenTicket(TypedDict):
    id: str
    customer: str
    items: str
    status: str
    channel: str
    time_placed: str
    elapsed_time: str


class KitchenState(rx.State):
    """State for managing the Kitchen Display System (KDS)."""

    @rx.var
    async def active_tickets(self) -> list[Order]:
        """Filters OrderState for statuses relevant to the kitchen (Accepted, Preparing)."""
        order_state = await self.get_state(OrderState)
        return [
            o
            for o in order_state.orders
            if o["status"] in ["Accepted", "Preparing", "Ready"]
        ]

    @rx.var
    async def pending_count(self) -> int:
        tickets = await self.active_tickets
        return sum((1 for o in tickets if o["status"] == "Accepted"))

    @rx.var
    async def preparing_count(self) -> int:
        tickets = await self.active_tickets
        return sum((1 for o in tickets if o["status"] == "Preparing"))

    @rx.var
    async def ready_count(self) -> int:
        tickets = await self.active_tickets
        return sum((1 for o in tickets if o["status"] == "Ready"))

    @rx.event
    async def advance_ticket(self, order_id: str):
        """Handles status transitions from the KDS interface."""
        order_state = await self.get_state(OrderState)
        current_status = ""
        for o in order_state.orders:
            if o["id"] == order_id:
                current_status = o["status"]
                break
        new_status = ""
        if current_status == "Accepted":
            new_status = "Preparing"
        elif current_status == "Preparing":
            new_status = "Ready"
        if new_status:
            order_state.orders = [
                o | {"status": new_status} if o["id"] == order_id else o
                for o in order_state.orders
            ]
            yield rx.toast(f"Order {order_id} moved to {new_status}")