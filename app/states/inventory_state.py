import reflex as rx
from typing import TypedDict
import random
import json
import logging


class InventoryItem(TypedDict):
    id: str
    name: str
    quantity: float
    unit: str
    reorder_level: float
    supplier: str
    status: str


class InventoryState(rx.State):
    items: list[InventoryItem] = []
    inventory_storage: str = rx.LocalStorage(
        name="cloud_kitchen_inventory", sync=True
    )

    @rx.event
    def setup_inventory(self):
        if self.inventory_storage:
            try:
                data = json.loads(self.inventory_storage)
                if data:
                    self.items = data
                    return
            except:
                logging.exception("Unexpected error")
        if len(self.items) > 0:
            return
        sample_data = [
            ("Ground Beef", 15.5, "kg", 20.0, "Sysco Meat"),
            ("Burger Buns", 120, "pcs", 100, "Local Bakery"),
            ("Cheddar Cheese", 5.0, "kg", 10.0, "Dairy Co"),
            ("Potatoes", 45.0, "kg", 30.0, "Farm Fresh"),
        ]
        self.items = [
            {
                "id": f"INV-{1000 + i}",
                "name": name,
                "quantity": qty,
                "unit": unit,
                "reorder_level": reorder,
                "supplier": supplier,
                "status": "Critical"
                if qty <= reorder * 0.5
                else "Low"
                if qty <= reorder
                else "OK",
            }
            for i, (name, qty, unit, reorder, supplier) in enumerate(
                sample_data
            )
        ]
        self.inventory_storage = json.dumps(self.items)

    @rx.var
    def total_items(self) -> int:
        return len(self.items)

    @rx.var
    def low_stock_count(self) -> int:
        return sum((1 for i in self.items if i["status"] == "Low"))

    @rx.var
    def critical_count(self) -> int:
        return sum((1 for i in self.items if i["status"] == "Critical"))