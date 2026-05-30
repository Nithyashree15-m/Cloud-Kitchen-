import reflex as rx
from app.states.navigation_state import NavigationState


def nav_item(label: str, icon: str) -> rx.Component:
    is_active = NavigationState.active_page == label
    return rx.el.button(
        rx.icon(
            icon,
            class_name=rx.cond(
                is_active, "h-5 w-5 text-white", "h-5 w-5 text-gray-500"
            ),
        ),
        rx.el.span(
            label,
            class_name=rx.cond(
                is_active,
                "font-semibold text-white",
                "font-medium text-gray-600",
            ),
        ),
        on_click=lambda: NavigationState.set_active_page(label),
        class_name=rx.cond(
            is_active,
            "flex items-center gap-3 w-full p-2.5 rounded-lg bg-indigo-600 transition-all shadow-sm",
            "flex items-center gap-3 w-full p-2.5 rounded-lg hover:bg-gray-100 transition-all text-gray-600",
        ),
    )


def sidebar() -> rx.Component:
    return rx.el.aside(
        rx.el.div(
            rx.el.div(
                rx.image(
                    src="/cloud_white_nine.png",
                    class_name="h-[40px] w-[40px] rounded-xl object-cover shadow-sm border border-gray-100",
                ),
                rx.el.span(
                    "Cloud Nine Cuisine",
                    class_name="text-xl font-bold text-gray-900 tracking-tight",
                ),
                class_name="flex items-center gap-3 mb-8 px-2",
            ),
            rx.el.nav(
                rx.el.div(
                    "MAIN MENU",
                    class_name="text-[10px] font-bold text-gray-400 tracking-widest mb-4 px-2",
                ),
                rx.el.div(
                    nav_item("Dashboard", "layout-dashboard"),
                    nav_item("Orders", "shopping-cart"),
                    nav_item("Kitchen", "cooking-pot"),
                    nav_item("Menu", "book-open"),
                    nav_item("Inventory", "package"),
                    class_name="flex flex-col gap-1",
                ),
                rx.el.div(
                    "MANAGEMENT",
                    class_name="text-[10px] font-bold text-gray-400 tracking-widest mt-8 mb-4 px-2",
                ),
                rx.el.div(
                    nav_item("Staff", "users"),
                    nav_item("Customers", "circle_user_round"),
                    nav_item("Delivery", "truck"),
                    nav_item("Billing", "credit-card"),
                    nav_item("Excel Data", "file-spreadsheet"),
                    class_name="flex flex-col gap-1",
                ),
                class_name="flex-1",
            ),
            class_name="flex flex-col h-full p-6 border-r border-gray-100 bg-white",
        ),
        class_name=rx.cond(
            NavigationState.sidebar_open,
            "fixed inset-y-0 left-0 z-50 w-64 translate-x-0 transition-transform lg:static lg:translate-x-0",
            "fixed inset-y-0 left-0 z-50 w-64 -translate-x-full transition-transform lg:static lg:translate-x-0",
        ),
    )