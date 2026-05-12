import reflex as rx
from app.states.inventory_state import InventoryState


def inventory_page() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h2(
                "Inventory Tracking",
                class_name="text-2xl font-bold text-gray-900",
            ),
            rx.el.p(
                "Manage your ingredients, suppliers, and stock levels.",
                class_name="text-sm text-gray-500 mt-1",
            ),
            class_name="mb-8",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.span(
                    "Total Items",
                    class_name="text-sm font-medium text-gray-500",
                ),
                rx.el.span(
                    InventoryState.total_items.to_string(),
                    class_name="text-3xl font-bold text-gray-900 mt-2",
                ),
                class_name="p-6 bg-white border border-gray-100 rounded-2xl shadow-sm flex flex-col",
            ),
            rx.el.div(
                rx.el.span(
                    "Low Stock", class_name="text-sm font-medium text-gray-500"
                ),
                rx.el.span(
                    InventoryState.low_stock_count.to_string(),
                    class_name="text-3xl font-bold text-amber-500 mt-2",
                ),
                class_name="p-6 bg-white border border-gray-100 rounded-2xl shadow-sm flex flex-col",
            ),
            rx.el.div(
                rx.el.span(
                    "Critical Stock",
                    class_name="text-sm font-medium text-gray-500",
                ),
                rx.el.span(
                    InventoryState.critical_count.to_string(),
                    class_name="text-3xl font-bold text-red-600 mt-2",
                ),
                class_name="p-6 bg-white border border-gray-100 rounded-2xl shadow-sm flex flex-col",
            ),
            class_name="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8",
        ),
        rx.el.div(
            rx.el.table(
                rx.el.thead(
                    rx.el.tr(
                        rx.el.th(
                            "Item",
                            class_name="px-6 py-3 text-left text-xs font-bold text-gray-400 uppercase tracking-widest",
                        ),
                        rx.el.th(
                            "Quantity",
                            class_name="px-6 py-3 text-left text-xs font-bold text-gray-400 uppercase tracking-widest",
                        ),
                        rx.el.th(
                            "Supplier",
                            class_name="px-6 py-3 text-left text-xs font-bold text-gray-400 uppercase tracking-widest",
                        ),
                        rx.el.th(
                            "Status",
                            class_name="px-6 py-3 text-left text-xs font-bold text-gray-400 uppercase tracking-widest",
                        ),
                        class_name="bg-gray-50/50",
                    )
                ),
                rx.el.tbody(
                    rx.foreach(
                        InventoryState.items,
                        lambda item: rx.el.tr(
                            rx.el.td(
                                item["name"],
                                class_name="px-6 py-4 text-sm font-bold text-gray-900",
                            ),
                            rx.el.td(
                                item["quantity"].to_string()
                                + " "
                                + item["unit"],
                                class_name="px-6 py-4 text-sm font-medium text-gray-700",
                            ),
                            rx.el.td(
                                item["supplier"],
                                class_name="px-6 py-4 text-sm text-gray-500",
                            ),
                            rx.el.td(
                                rx.el.span(
                                    item["status"],
                                    class_name=rx.match(
                                        item["status"],
                                        (
                                            "OK",
                                            "bg-green-50 text-green-600 px-2.5 py-1 rounded-full text-xs font-bold",
                                        ),
                                        (
                                            "Low",
                                            "bg-amber-50 text-amber-600 px-2.5 py-1 rounded-full text-xs font-bold",
                                        ),
                                        (
                                            "Critical",
                                            "bg-red-50 text-red-600 px-2.5 py-1 rounded-full text-xs font-bold",
                                        ),
                                        "bg-gray-100 text-gray-500 px-2.5 py-1 rounded-full text-xs font-bold",
                                    ),
                                ),
                                class_name="px-6 py-4",
                            ),
                            class_name=rx.cond(
                                item["status"] == "Critical",
                                "bg-red-50/30 border-b border-red-50",
                                rx.cond(
                                    item["status"] == "Low",
                                    "bg-amber-50/30 border-b border-amber-50",
                                    "border-b border-gray-50",
                                ),
                            ),
                        ),
                    )
                ),
                class_name="w-full table-auto",
            ),
            class_name="bg-white border border-gray-100 rounded-2xl shadow-sm overflow-hidden",
        ),
        class_name="animate-in fade-in duration-500",
    )