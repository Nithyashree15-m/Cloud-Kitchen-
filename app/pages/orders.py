import reflex as rx
from app.states.order_state import OrderState


def status_tab(label: str) -> rx.Component:
    is_active = OrderState.status_filter == label
    return rx.el.button(
        label,
        on_click=lambda: OrderState.set_status_filter(label),
        class_name=rx.cond(
            is_active,
            "px-4 py-2 text-sm font-semibold text-indigo-600 border-b-2 border-indigo-600",
            "px-4 py-2 text-sm font-medium text-gray-500 hover:text-gray-700 hover:border-b-2 hover:border-gray-200 transition-all",
        ),
    )


def channel_icon(channel: str) -> rx.Component:
    return rx.el.div(
        rx.match(
            channel,
            (
                "UberEats",
                rx.icon("smartphone", class_name="h-4 w-4 text-green-600"),
            ),
            ("DoorDash", rx.icon("zap", class_name="h-4 w-4 text-red-600")),
            ("Direct", rx.icon("globe", class_name="h-4 w-4 text-blue-600")),
            rx.icon("circle_help", class_name="h-4 w-4"),
        ),
        rx.el.span(channel, class_name="text-xs font-semibold text-gray-600"),
        class_name="flex items-center gap-1.5 bg-gray-50 px-2 py-1 rounded-md",
    )


def status_badge(status: str) -> rx.Component:
    return rx.el.span(
        status,
        class_name=rx.match(
            status,
            (
                "New",
                "bg-blue-50 text-blue-600 px-2.5 py-1 rounded-full text-xs font-bold",
            ),
            (
                "Accepted",
                "bg-indigo-50 text-indigo-600 px-2.5 py-1 rounded-full text-xs font-bold",
            ),
            (
                "Preparing",
                "bg-orange-50 text-orange-600 px-2.5 py-1 rounded-full text-xs font-bold",
            ),
            (
                "Ready",
                "bg-green-50 text-green-600 px-2.5 py-1 rounded-full text-xs font-bold",
            ),
            (
                "Delivered",
                "bg-gray-50 text-gray-600 px-2.5 py-1 rounded-full text-xs font-bold",
            ),
            "bg-gray-100 text-gray-500 px-2.5 py-1 rounded-full text-xs font-bold",
        ),
    )


def order_row(order: dict) -> rx.Component:
    return rx.el.tr(
        rx.el.td(
            order["id"], class_name="px-6 py-4 text-sm font-bold text-gray-900"
        ),
        rx.el.td(
            order["customer"],
            class_name="px-6 py-4 text-sm font-medium text-gray-700",
        ),
        rx.el.td(
            rx.el.p(
                order["items"],
                class_name="text-xs text-gray-500 truncate max-w-[200px]",
            ),
            class_name="px-6 py-4",
        ),
        rx.el.td(status_badge(order["status"]), class_name="px-6 py-4"),
        rx.el.td(channel_icon(order["channel"]), class_name="px-6 py-4"),
        rx.el.td(order["time"], class_name="px-6 py-4 text-sm text-gray-500"),
        rx.el.td(
            f"₹{order['total']:.2f}",
            class_name="px-6 py-4 text-sm font-bold text-gray-900",
        ),
        rx.el.td(
            rx.el.button(
                rx.icon("gallery_vertical", class_name="h-4 w-4 text-gray-400"),
                class_name="p-1 hover:bg-gray-100 rounded",
            ),
            class_name="px-6 py-4 text-right",
        ),
        on_click=lambda: OrderState.select_order(order["id"]),
        class_name="hover:bg-gray-50 transition-all cursor-pointer border-b border-gray-50",
    )


def order_detail_modal() -> rx.Component:
    order = OrderState.selected_order
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.el.h3(
                            f"Order {order['id']}",
                            class_name="text-xl font-bold text-gray-900",
                        ),
                        rx.el.button(
                            rx.icon("x", class_name="h-5 w-5"),
                            on_click=lambda: OrderState.select_order(""),
                            class_name="text-gray-400 hover:text-gray-600",
                        ),
                        class_name="flex justify-between items-center mb-6",
                    ),
                    rx.el.div(
                        rx.el.div(
                            rx.el.p(
                                "Customer",
                                class_name="text-xs font-bold text-gray-400 uppercase tracking-wider",
                            ),
                            rx.el.p(
                                order["customer"],
                                class_name="text-lg font-bold text-gray-900",
                            ),
                            class_name="mb-4",
                        ),
                        rx.el.div(
                            rx.el.p(
                                "Order Items",
                                class_name="text-xs font-bold text-gray-400 uppercase tracking-wider mb-2",
                            ),
                            rx.el.p(
                                order["items"],
                                class_name="text-sm text-gray-700 leading-relaxed",
                            ),
                            class_name="mb-6 p-4 bg-gray-50 rounded-xl",
                        ),
                        rx.el.div(
                            rx.el.div(
                                rx.el.p(
                                    "Total Amount",
                                    class_name="text-xs text-gray-500",
                                ),
                                rx.el.p(
                                    f"₹{order['total']:.2f}",
                                    class_name="text-2xl font-black text-indigo-600",
                                ),
                                class_name="mb-4",
                            ),
                            class_name="flex justify-between items-end",
                        ),
                        rx.el.div(
                            rx.el.p(
                                "Quick Actions",
                                class_name="text-xs font-bold text-gray-400 uppercase tracking-wider mb-3",
                            ),
                            rx.el.div(
                                rx.el.button(
                                    "Accept Order",
                                    on_click=lambda: (
                                        OrderState.update_order_status(
                                            order["id"], "Accepted"
                                        )
                                    ),
                                    class_name="w-full py-3 bg-indigo-600 text-white rounded-xl font-bold shadow-lg hover:bg-indigo-700 transition-all mb-2",
                                ),
                                rx.el.button(
                                    "Mark Ready",
                                    on_click=lambda: (
                                        OrderState.update_order_status(
                                            order["id"], "Ready"
                                        )
                                    ),
                                    class_name="w-full py-3 bg-green-600 text-white rounded-xl font-bold shadow-lg hover:bg-green-700 transition-all mb-2",
                                ),
                                rx.el.button(
                                    "Cancel Order",
                                    on_click=lambda: (
                                        OrderState.update_order_status(
                                            order["id"], "Cancelled"
                                        )
                                    ),
                                    class_name="w-full py-3 bg-white border border-red-200 text-red-600 rounded-xl font-bold hover:bg-red-50 transition-all",
                                ),
                                class_name="flex flex-col",
                            ),
                        ),
                    ),
                    class_name="p-8 bg-white rounded-2xl w-full max-w-md shadow-2xl animate-in slide-in-from-right duration-300",
                ),
                class_name="fixed inset-0 bg-black/40 backdrop-blur-sm flex items-center justify-center z-[100]",
            ),
            class_name="relative",
        ),
        class_name=rx.cond(
            OrderState.selected_order_id == "", "hidden", "block"
        ),
    )


def orders_page() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.h2(
                    "Order Management",
                    class_name="text-2xl font-bold text-gray-900",
                ),
                rx.el.p(
                    "Track and manage incoming kitchen orders in real-time.",
                    class_name="text-sm text-gray-500 mt-1",
                ),
            ),
            rx.el.div(
                rx.el.div(
                    rx.icon(
                        "search",
                        class_name="absolute left-3 top-1/2 -translate-y-1/2 h-4 w-4 text-gray-400",
                    ),
                    rx.el.input(
                        placeholder="Search orders, customers...",
                        on_change=OrderState.set_search_query,
                        class_name="pl-10 pr-4 py-2 border border-gray-200 rounded-lg text-sm focus:ring-2 focus:ring-indigo-100 focus:border-indigo-600 w-full sm:w-64 transition-all",
                    ),
                    class_name="relative",
                ),
                class_name="flex items-center gap-3",
            ),
            class_name="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4 mb-8",
        ),
        rx.el.div(
            rx.el.div(
                status_tab("All"),
                status_tab("New"),
                status_tab("Accepted"),
                status_tab("Preparing"),
                status_tab("Ready"),
                status_tab("Delivered"),
                class_name="flex border-b border-gray-200 gap-2 mb-6",
            )
        ),
        rx.el.div(
            rx.el.table(
                rx.el.thead(
                    rx.el.tr(
                        rx.el.th(
                            "ID",
                            class_name="px-6 py-3 text-left text-xs font-bold text-gray-400 uppercase tracking-widest",
                        ),
                        rx.el.th(
                            "Customer",
                            class_name="px-6 py-3 text-left text-xs font-bold text-gray-400 uppercase tracking-widest",
                        ),
                        rx.el.th(
                            "Items",
                            class_name="px-6 py-3 text-left text-xs font-bold text-gray-400 uppercase tracking-widest",
                        ),
                        rx.el.th(
                            "Status",
                            class_name="px-6 py-3 text-left text-xs font-bold text-gray-400 uppercase tracking-widest",
                        ),
                        rx.el.th(
                            "Channel",
                            class_name="px-6 py-3 text-left text-xs font-bold text-gray-400 uppercase tracking-widest",
                        ),
                        rx.el.th(
                            "Time",
                            class_name="px-6 py-3 text-left text-xs font-bold text-gray-400 uppercase tracking-widest",
                        ),
                        rx.el.th(
                            "Total",
                            class_name="px-6 py-3 text-left text-xs font-bold text-gray-400 uppercase tracking-widest",
                        ),
                        rx.el.th("", class_name="px-6 py-3 text-left"),
                        class_name="bg-gray-50/50",
                    )
                ),
                rx.el.tbody(rx.foreach(OrderState.filtered_orders, order_row)),
                class_name="w-full table-auto",
            ),
            class_name="bg-white border border-gray-100 rounded-2xl shadow-sm overflow-hidden",
        ),
        order_detail_modal(),
        class_name="animate-in fade-in duration-500",
    )