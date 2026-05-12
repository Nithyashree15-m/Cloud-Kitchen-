import reflex as rx
from app.components.sidebar import sidebar
from app.components.header import header
from app.states.navigation_state import NavigationState


def layout(content: rx.Component) -> rx.Component:
    return rx.el.div(
        sidebar(),
        rx.el.div(
            header(),
            rx.el.main(content, class_name="flex-1 overflow-y-auto p-8"),
            class_name="flex flex-col flex-1 min-w-0",
        ),
        class_name="flex h-screen w-screen bg-gray-50 font-['Inter']",
    )