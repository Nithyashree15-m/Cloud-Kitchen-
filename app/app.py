import reflex as rx
from app.components.layout import layout
from app.pages.dashboard import dashboard_page
from app.pages.orders import orders_page
from app.pages.kitchen import kitchen_page
from app.pages.menu import menu_page
from app.pages.inventory import inventory_page
from app.pages.staff import staff_page
from app.pages.customers import customers_page
from app.pages.delivery import delivery_page
from app.pages.billing import billing_page
from app.states.order_state import OrderState
from app.states.menu_state import MenuState
from app.states.inventory_state import InventoryState
from app.states.staff_state import StaffState
from app.states.customer_state import CustomerState
from app.states.delivery_state import DeliveryState
from app.states.billing_state import BillingState


def index() -> rx.Component:
    return layout(dashboard_page())


def orders() -> rx.Component:
    return layout(orders_page())


def kitchen() -> rx.Component:
    return layout(kitchen_page())


def menu() -> rx.Component:
    return layout(menu_page())


def inventory() -> rx.Component:
    return layout(inventory_page())


def staff() -> rx.Component:
    return layout(staff_page())


def customers() -> rx.Component:
    return layout(customers_page())


def delivery() -> rx.Component:
    return layout(delivery_page())


def billing() -> rx.Component:
    return layout(billing_page())


app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(
            rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""
        ),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(index, route="/", on_load=OrderState.setup_sample_orders)
app.add_page(orders, route="/orders", on_load=OrderState.setup_sample_orders)
app.add_page(kitchen, route="/kitchen", on_load=OrderState.setup_sample_orders)
app.add_page(menu, route="/menu", on_load=MenuState.setup_menu)
app.add_page(
    inventory, route="/inventory", on_load=InventoryState.setup_inventory
)
app.add_page(staff, route="/staff", on_load=StaffState.setup_staff)
app.add_page(
    customers, route="/customers", on_load=CustomerState.setup_customers
)
app.add_page(
    delivery, route="/delivery", on_load=DeliveryState.setup_deliveries
)
app.add_page(billing, route="/billing", on_load=BillingState.setup_billing)