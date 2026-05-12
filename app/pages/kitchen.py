import reflex as rx
from app.states.kitchen_state import KitchenState
from app.states.order_state import OrderState


def kds_header_stat(label: str, count: int, color: str) -> rx.Component:
    return rx.el.div(
        rx.el.span(
            label,
            class_name="text-sm font-bold text-gray-400 uppercase tracking-widest",
        ),
        rx.el.div(count.to_string(), class_name=f"text-4xl font-black {color}"),
        class_name="flex flex-col items-center justify-center p-4 bg-white rounded-2xl border border-gray-100 flex-1",
    )


def ticket_card(order: dict) -> rx.Component:
    border_color = rx.match(
        order["status"],
        ("Accepted", "border-l-[12px] border-l-amber-400"),
        ("Preparing", "border-l-[12px] border-l-orange-500"),
        ("Ready", "border-l-[12px] border-l-green-500"),
        "border-l-gray-200",
    )
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.span(
                        order["id"],
                        class_name="text-2xl font-black text-gray-900",
                    ),
                    rx.el.span(
                        order["time"],
                        class_name="text-sm font-bold text-gray-400 ml-2",
                    ),
                    class_name="flex items-baseline",
                ),
                rx.el.div(
                    rx.icon("clock", class_name="h-4 w-4 mr-1"),
                    rx.el.span("5m 12s", class_name="text-sm font-bold"),
                    class_name="flex items-center text-orange-600 bg-orange-50 px-2 py-1 rounded-lg",
                ),
                class_name="flex justify-between items-start mb-4",
            ),
            rx.el.div(
                rx.el.p(
                    order["items"],
                    class_name="text-xl font-bold text-gray-800 leading-tight border-t border-gray-50 pt-4",
                ),
                class_name="min-h-[120px]",
            ),
            rx.el.div(
                rx.match(
                    order["status"],
                    (
                        "Accepted",
                        rx.el.button(
                            "START COOKING",
                            on_click=lambda: KitchenState.advance_ticket(
                                order["id"]
                            ),
                            class_name="w-full py-6 bg-amber-500 text-white font-black text-xl rounded-xl shadow-lg hover:bg-amber-600 active:scale-[0.98] transition-all",
                        ),
                    ),
                    (
                        "Preparing",
                        rx.el.button(
                            "MARK READY",
                            on_click=lambda: KitchenState.advance_ticket(
                                order["id"]
                            ),
                            class_name="w-full py-6 bg-green-600 text-white font-black text-xl rounded-xl shadow-lg hover:bg-green-700 active:scale-[0.98] transition-all",
                        ),
                    ),
                    rx.el.div(
                        rx.icon(
                            "circle_check",
                            class_name="h-8 w-8 text-green-500 mr-2",
                        ),
                        rx.el.span(
                            "READY FOR PICKUP",
                            class_name="text-green-600 font-black text-lg",
                        ),
                        class_name="flex items-center justify-center p-4 bg-green-50 rounded-xl",
                    ),
                ),
                class_name="mt-6",
            ),
            class_name=f"p-6 h-full flex flex-col justify-between {border_color}",
        ),
        class_name="bg-white rounded-2xl shadow-sm border border-gray-100 overflow-hidden",
    )


def kitchen_page() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            kds_header_stat(
                "Pending", KitchenState.pending_count, "text-amber-500"
            ),
            kds_header_stat(
                "Cooking", KitchenState.preparing_count, "text-orange-500"
            ),
            kds_header_stat(
                "Ready", KitchenState.ready_count, "text-green-600"
            ),
            class_name="flex gap-6 mb-8",
        ),
        rx.el.div(
            rx.foreach(KitchenState.active_tickets, ticket_card),
            class_name="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-6",
        ),
        class_name="animate-in fade-in duration-500",
    )