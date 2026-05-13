import reflex as rx
from typing import TypedDict, Optional
from faker import Faker
import json
import logging

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
    image: str


class MenuState(rx.State):
    """State for managing the menu items and categories."""

    items: list[MenuItem] = []
    menu_storage: str = rx.LocalStorage(name="cloud_kitchen_menu", sync=True)
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
        if self.menu_storage:
            try:
                data = json.loads(self.menu_storage)
                if data:
                    self.items = data
                    return
            except:
                logging.exception("Unexpected error")
        if len(self.items) > 0:
            return
        sample_names = [
            (
                "Classic Cheeseburger",
                "Burgers",
                80.99,
                "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=400&h=300&fit=crop",
            ),
            (
                "Truffle Mushroom Burger",
                "Burgers",
                70.5,
                "https://images.unsplash.com/photo-1572802419224-296b0aeee0d9?w=400&h=300&fit=crop",
            ),
            (
                "Spicy Zinger Chicken",
                "Burgers",
                110.0,
                "https://images.unsplash.com/photo-1626645738196-c2a7c87a8f58?w=400&h=300&fit=crop",
            ),
            (
                "Large Crispy Fries",
                "Sides",
                60.5,
                "https://images.unsplash.com/photo-1573080496219-bb080dd4f877?w=400&h=300&fit=crop",
            ),
            (
                "Sweet Potato Wedges",
                "Sides",
                50.5,
                "https://images.unsplash.com/photo-1629385701021-fcd568a743e8?w=400&h=300&fit=crop",
            ),
            (
                "Onion Rings (8pc)",
                "Sides",
                65.0,
                "https://images.unsplash.com/photo-1639024471283-03518883512d?w=400&h=300&fit=crop",
            ),
            (
                "Classic Cola",
                "Drinks",
                45.5,
                "https://images.unsplash.com/photo-1622483767028-3f66f32aef97?w=400&h=300&fit=crop",
            ),
            (
                "Fresh Lemonade",
                "Drinks",
                30.5,
                "https://images.unsplash.com/photo-1621263764928-df1444c5e859?w=400&h=300&fit=crop",
            ),
            (
                "Craft Root Beer",
                "Drinks",
                130.0,
                "https://images.unsplash.com/photo-1558642452-9d2a7deb7f62?w=400&h=300&fit=crop",
            ),
            (
                "Chocolate Lava Cake",
                "Desserts",
                70.99,
                "https://images.unsplash.com/photo-1624353365286-3f8d62daad51?w=400&h=300&fit=crop",
            ),
            (
                "New York Cheesecake",
                "Desserts",
                65.5,
                "https://www.allrecipes.com/thmb/aEnGTTMYn_1asJi_E25B5-Hv03w=/0x512/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/221142-new-york-style-cheesecake-VAT-Beauty-4x3-7a5b4da8cde4437ab0c592e4f4cbe658.jpg",
            ),
            (
                "Burger & Fries Combo",
                "Combos",
                120.0,
                "https://images.unsplash.com/photo-1594212699903-ec8a3eca50f5?w=400&h=300&fit=crop",
            ),
            (
                "Family Feast",
                "Combos",
                180.0,
                "https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=400&h=300&fit=crop",
            ),
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
                "image": img_url,
            }
            for i, (name, cat, price, img_url) in enumerate(sample_names)
        ]
        self.menu_storage = json.dumps(self.items)

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
        self.menu_storage = json.dumps(self.items)

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
                image="https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=400&h=300&fit=crop",
            )
            self.items.append(new_item)
        self.menu_storage = json.dumps(self.items)
        self.show_item_modal = False

    @rx.event
    def delete_item(self, item_id: str):
        self.items = [i for i in self.items if i["id"] != item_id]
        self.menu_storage = json.dumps(self.items)