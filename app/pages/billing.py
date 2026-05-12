import reflex as rx
from app.states.billing_state import BillingState


def billing_page() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.h2(
                    "Billing & Financials",
                    class_name="text-2xl font-bold text-gray-900",
                ),
                rx.el.p(
                    "Track revenue, invoices, and payouts.",
                    class_name="text-sm text-gray-500 mt-1",
                ),
            ),
            class_name="mb-8",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.span(
                    "Total Revenue (Paid)",
                    class_name="text-sm font-medium text-gray-500",
                ),
                rx.el.span(
                    f"₹{BillingState.today_revenue:.2f}",
                    class_name="text-3xl font-bold text-green-600 mt-2",
                ),
                class_name="p-6 bg-white border border-gray-100 rounded-2xl shadow-sm flex flex-col",
            ),
            rx.el.div(
                rx.el.span(
                    "Pending Amount",
                    class_name="text-sm font-medium text-gray-500",
                ),
                rx.el.span(
                    f"₹{BillingState.pending_amount:.2f}",
                    class_name="text-3xl font-bold text-amber-500 mt-2",
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
                            "Invoice",
                            class_name="px-6 py-3 text-left text-xs font-bold text-gray-400 uppercase tracking-widest",
                        ),
                        rx.el.th(
                            "Customer",
                            class_name="px-6 py-3 text-left text-xs font-bold text-gray-400 uppercase tracking-widest",
                        ),
                        rx.el.th(
                            "Amount",
                            class_name="px-6 py-3 text-left text-xs font-bold text-gray-400 uppercase tracking-widest",
                        ),
                        rx.el.th(
                            "Status",
                            class_name="px-6 py-3 text-left text-xs font-bold text-gray-400 uppercase tracking-widest",
                        ),
                        rx.el.th(
                            "Date",
                            class_name="px-6 py-3 text-left text-xs font-bold text-gray-400 uppercase tracking-widest",
                        ),
                        rx.el.th(
                            "Method",
                            class_name="px-6 py-3 text-left text-xs font-bold text-gray-400 uppercase tracking-widest",
                        ),
                        class_name="bg-gray-50/50",
                    )
                ),
                rx.el.tbody(
                    rx.foreach(
                        BillingState.invoices,
                        lambda inv: rx.el.tr(
                            rx.el.td(
                                inv["id"],
                                class_name="px-6 py-4 text-sm font-bold text-gray-900",
                            ),
                            rx.el.td(
                                inv["customer"],
                                class_name="px-6 py-4 text-sm text-gray-700",
                            ),
                            rx.el.td(
                                f"₹{inv['amount']:.2f}",
                                class_name="px-6 py-4 text-sm font-bold text-gray-900",
                            ),
                            rx.el.td(
                                rx.el.span(
                                    inv["status"],
                                    class_name=rx.match(
                                        inv["status"],
                                        (
                                            "Paid",
                                            "bg-green-50 text-green-600 px-2.5 py-1 rounded-full text-xs font-bold",
                                        ),
                                        (
                                            "Pending",
                                            "bg-amber-50 text-amber-600 px-2.5 py-1 rounded-full text-xs font-bold",
                                        ),
                                        (
                                            "Overdue",
                                            "bg-red-50 text-red-600 px-2.5 py-1 rounded-full text-xs font-bold",
                                        ),
                                        (
                                            "Refunded",
                                            "bg-gray-100 text-gray-500 px-2.5 py-1 rounded-full text-xs font-bold",
                                        ),
                                        "bg-gray-100 text-gray-500 px-2.5 py-1 rounded-full text-xs font-bold",
                                    ),
                                ),
                                class_name="px-6 py-4",
                            ),
                            rx.el.td(
                                inv["date"],
                                class_name="px-6 py-4 text-sm text-gray-500",
                            ),
                            rx.el.td(
                                inv["method"],
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