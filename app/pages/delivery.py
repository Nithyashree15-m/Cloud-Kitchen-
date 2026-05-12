import reflex as rx
from app.states.delivery_state import DeliveryState


def delivery_page() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.h2(
                    "Delivery Logistics",
                    class_name="text-2xl font-bold text-gray-900",
                ),
                rx.el.p(
                    "Monitor active deliveries and driver status.",
                    class_name="text-sm text-gray-500 mt-1",
                ),
            ),
            class_name="mb-8",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.span(
                    "Active Deliveries",
                    class_name="text-sm font-medium text-gray-500",
                ),
                rx.el.span(
                    DeliveryState.active_deliveries_count.to_string(),
                    class_name="text-3xl font-bold text-indigo-600 mt-2",
                ),
                class_name="p-6 bg-white border border-gray-100 rounded-2xl shadow-sm flex flex-col",
            ),
            rx.el.div(
                rx.el.span(
                    "Avg Delivery Time",
                    class_name="text-sm font-medium text-gray-500",
                ),
                rx.el.span(
                    "22 mins",
                    class_name="text-3xl font-bold text-gray-900 mt-2",
                ),
                class_name="p-6 bg-white border border-gray-100 rounded-2xl shadow-sm flex flex-col",
            ),
            class_name="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8",
        ),
        rx.el.div(
            rx.el.table(
                rx.el.thead(
                    rx.el.tr(
                        rx.el.th(
                            "Order ID",
                            class_name="px-6 py-3 text-left text-xs font-bold text-gray-400 uppercase tracking-widest",
                        ),
                        rx.el.th(
                            "Customer",
                            class_name="px-6 py-3 text-left text-xs font-bold text-gray-400 uppercase tracking-widest",
                        ),
                        rx.el.th(
                            "Driver",
                            class_name="px-6 py-3 text-left text-xs font-bold text-gray-400 uppercase tracking-widest",
                        ),
                        rx.el.th(
                            "Status",
                            class_name="px-6 py-3 text-left text-xs font-bold text-gray-400 uppercase tracking-widest",
                        ),
                        rx.el.th(
                            "ETA",
                            class_name="px-6 py-3 text-left text-xs font-bold text-gray-400 uppercase tracking-widest",
                        ),
                        rx.el.th(
                            "Platform",
                            class_name="px-6 py-3 text-left text-xs font-bold text-gray-400 uppercase tracking-widest",
                        ),
                        class_name="bg-gray-50/50",
                    )
                ),
                rx.el.tbody(
                    rx.foreach(
                        DeliveryState.deliveries,
                        lambda d: rx.el.tr(
                            rx.el.td(
                                d["order_id"],
                                class_name="px-6 py-4 text-sm font-bold text-gray-900",
                            ),
                            rx.el.td(
                                d["customer"],
                                class_name="px-6 py-4 text-sm text-gray-700",
                            ),
                            rx.el.td(
                                d["driver"],
                                class_name="px-6 py-4 text-sm font-medium text-gray-900",
                            ),
                            rx.el.td(
                                rx.el.span(
                                    d["status"],
                                    class_name=rx.match(
                                        d["status"],
                                        (
                                            "Assigned",
                                            "bg-blue-50 text-blue-600 px-2.5 py-1 rounded-full text-xs font-bold",
                                        ),
                                        (
                                            "Picked Up",
                                            "bg-amber-50 text-amber-600 px-2.5 py-1 rounded-full text-xs font-bold",
                                        ),
                                        (
                                            "En Route",
                                            "bg-green-50 text-green-600 px-2.5 py-1 rounded-full text-xs font-bold",
                                        ),
                                        "bg-gray-100 text-gray-500 px-2.5 py-1 rounded-full text-xs font-bold",
                                    ),
                                ),
                                class_name="px-6 py-4",
                            ),
                            rx.el.td(
                                d["eta"],
                                class_name="px-6 py-4 text-sm font-bold text-gray-900",
                            ),
                            rx.el.td(
                                d["platform"],
                                class_name="px-6 py-4 text-sm text-gray-500",
                            ),
                            class_name="border-b border-gray-50 hover:bg-gray-50 transition-all",
                        ),
                    )
                ),
                class_name="w-full table-auto",
            ),
            class_name="bg-white border border-gray-100 rounded-2xl shadow-sm overflow-hidden mb-8",
        ),
        class_name="animate-in fade-in duration-500",
    )