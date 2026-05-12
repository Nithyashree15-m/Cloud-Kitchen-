import reflex as rx
from app.states.customer_state import CustomerState


def customers_page() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.h2(
                    "Customers & CRM",
                    class_name="text-2xl font-bold text-gray-900",
                ),
                rx.el.p(
                    "Manage your customer relationships and order history.",
                    class_name="text-sm text-gray-500 mt-1",
                ),
            ),
            rx.el.div(
                rx.icon(
                    "search",
                    class_name="absolute left-3 top-1/2 -translate-y-1/2 h-4 w-4 text-gray-400",
                ),
                rx.el.input(
                    placeholder="Search customers...",
                    on_change=CustomerState.set_search_query,
                    class_name="pl-10 pr-4 py-2 border border-gray-200 rounded-lg text-sm focus:ring-2 focus:ring-indigo-100 focus:border-indigo-600 w-full sm:w-64 transition-all",
                ),
                class_name="relative",
            ),
            class_name="flex justify-between items-end mb-8",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.span(
                    "Total Customers",
                    class_name="text-sm font-medium text-gray-500",
                ),
                rx.el.span(
                    CustomerState.total_customers.to_string(),
                    class_name="text-3xl font-bold text-gray-900 mt-2",
                ),
                class_name="p-6 bg-white border border-gray-100 rounded-2xl shadow-sm flex flex-col",
            ),
            rx.el.div(
                rx.el.span(
                    "VIP Customers",
                    class_name="text-sm font-medium text-gray-500",
                ),
                rx.el.span(
                    CustomerState.vip_count.to_string(),
                    class_name="text-3xl font-bold text-indigo-600 mt-2",
                ),
                class_name="p-6 bg-white border border-gray-100 rounded-2xl shadow-sm flex flex-col",
            ),
            rx.el.div(
                rx.el.span(
                    "Avg Order Value",
                    class_name="text-sm font-medium text-gray-500",
                ),
                rx.el.span(
                    f"₹{CustomerState.avg_order_value:.2f}",
                    class_name="text-3xl font-bold text-green-600 mt-2",
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
                            "Customer",
                            class_name="px-6 py-3 text-left text-xs font-bold text-gray-400 uppercase tracking-widest",
                        ),
                        rx.el.th(
                            "Contact",
                            class_name="px-6 py-3 text-left text-xs font-bold text-gray-400 uppercase tracking-widest",
                        ),
                        rx.el.th(
                            "Orders",
                            class_name="px-6 py-3 text-left text-xs font-bold text-gray-400 uppercase tracking-widest",
                        ),
                        rx.el.th(
                            "Spent",
                            class_name="px-6 py-3 text-left text-xs font-bold text-gray-400 uppercase tracking-widest",
                        ),
                        rx.el.th(
                            "Last Order",
                            class_name="px-6 py-3 text-left text-xs font-bold text-gray-400 uppercase tracking-widest",
                        ),
                        class_name="bg-gray-50/50",
                    )
                ),
                rx.el.tbody(
                    rx.foreach(
                        CustomerState.filtered_customers,
                        lambda c: rx.el.tr(
                            rx.el.td(
                                rx.el.div(
                                    rx.el.span(
                                        c["name"],
                                        class_name="text-sm font-bold text-gray-900 mr-2",
                                    ),
                                    rx.cond(
                                        c["is_vip"],
                                        rx.el.span(
                                            "VIP",
                                            class_name="bg-yellow-100 text-yellow-800 text-[10px] font-bold px-2 py-0.5 rounded-md",
                                        ),
                                    ),
                                    class_name="flex items-center",
                                ),
                                class_name="px-6 py-4",
                            ),
                            rx.el.td(
                                rx.el.div(
                                    rx.el.p(
                                        c["email"],
                                        class_name="text-sm text-gray-700",
                                    ),
                                    rx.el.p(
                                        c["phone"],
                                        class_name="text-xs text-gray-500",
                                    ),
                                ),
                                class_name="px-6 py-4",
                            ),
                            rx.el.td(
                                c["total_orders"].to_string(),
                                class_name="px-6 py-4 text-sm font-medium text-gray-900",
                            ),
                            rx.el.td(
                                f"₹{c['total_spent']:.2f}",
                                class_name="px-6 py-4 text-sm font-bold text-indigo-600",
                            ),
                            rx.el.td(
                                c["last_order"],
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