import reflex as rx
from typing import TypedDict, Optional
from faker import Faker

fake = Faker()


class MenuItem(TypedDict):
    id: str
    name: str
    description: str
    price: float
    category: str
    modifiers: list[str]
    available: bool
    seasonal_start: str
    seasonal_end: str


class MenuState(rx.State):
    """State for managing the menu items and categories."""

    items: list[MenuItem] = []
    categories: list[str] = [
        "All",
        "Burgers",
        "Sides",
        "Drinks",
        "Desserts",
        "Combos",
    ]
    active_category: str = "All"
    search_query: str = ""
    show_item_modal: bool = False
    editing_id: str = ""
    form_data: dict[str, str | float | bool] = {
        "name": "",
        "description": "",
        "price": 0.0,
        "category": "Burgers",
        "available": True,
    }

    @rx.event
    def setup_menu(self):
        if len(self.items) > 0:
            return
        sample_names = [
            ("Classic Cheeseburger", "Burgers", 12.99),
            ("Truffle Mushroom Burger", "Burgers", 15.5),
            ("Spicy Zinger Chicken", "Burgers", 11.0),
            ("Large Crispy Fries", "Sides", 4.5),
            ("Sweet Potato Wedges", "Sides", 5.5),
            ("Onion Rings (8pc)", "Sides", 6.0),
            ("Classic Cola", "Drinks", 2.5),
            ("Fresh Lemonade", "Drinks", 3.5),
            ("Craft Root Beer", "Drinks", 4.0),
            ("Chocolate Lava Cake", "Desserts", 7.99),
            ("New York Cheesecake", "Desserts", 6.5),
            ("Burger & Fries Combo", "Combos", 16.0),
            ("Family Feast", "Combos", 45.0),
        ]
        self.items = [
            {
                "id": f"M-{100 + i}",
                "name": name,
                "description": fake.sentence(),
                "price": price,
                "category": cat,
                "modifiers": ["Extra Sauce", "No Onions"],
                "available": True,
                "seasonal_start": "",
                "seasonal_end": "",
            }
            for i, (name, cat, price) in enumerate(sample_names)
        ]

    @rx.var
    def filtered_menu(self) -> list[MenuItem]:
        res = self.items
        if self.active_category != "All":
            res = [i for i in res if i["category"] == self.active_category]
        if self.search_query:
            q = self.search_query.lower()
            res = [
                i
                for i in res
                if q in i["name"].lower() or q in i["category"].lower()
            ]
        return res

    @rx.event
    def set_category(self, cat: str):
        self.active_category = cat

    @rx.event
    def toggle_availability(self, item_id: str):
        self.items = [
            i | {"available": not i["available"]} if i["id"] == item_id else i
            for i in self.items
        ]

    @rx.event
    def open_add_modal(self):
        self.editing_id = ""
        self.form_data = {
            "name": "",
            "description": "",
            "price": 0.0,
            "category": "Burgers",
            "available": True,
        }
        self.show_item_modal = True

    @rx.event
    def handle_submit(self, data: dict):
        if self.editing_id:
            self.items = [
                i | data if i["id"] == self.editing_id else i
                for i in self.items
            ]
        else:
            new_item = MenuItem(
                id=f"M-{len(self.items) + 101}",
                name=str(data.get("name", "")),
                description=str(data.get("description", "")),
                price=float(data.get("price", 0.0)),
                category=str(data.get("category", "Burgers")),
                modifiers=[],
                available=True,
                seasonal_start="",
                seasonal_end="",
            )
            self.items.append(new_item)
        self.show_item_modal = False

    @rx.event
    def delete_item(self, item_id: str):
        self.items = [i for i in self.items if i["id"] != item_id]