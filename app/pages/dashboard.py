import reflex as rx
import plotly.express as px
from app.states.dashboard_state import DashboardState


def kpi_card(label: str, kpi: dict) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.span(
                    kpi["label"], class_name="text-sm font-medium text-gray-500"
                ),
                rx.el.div(
                    rx.el.span(
                        kpi["change"],
                        class_name="text-xs font-bold text-green-600 bg-green-50 px-2 py-0.5 rounded-full",
                    ),
                    class_name="mt-1",
                ),
                class_name="flex flex-col",
            ),
            rx.el.div(
                rx.icon(
                    rx.match(
                        label,
                        ("orders", "shopping-bag"),
                        ("revenue", "dollar-sign"),
                        ("prep_time", "clock"),
                        ("active", "flame"),
                        "circle",
                    ),
                    class_name="h-5 w-5 text-indigo-600",
                ),
                class_name="h-10 w-10 rounded-lg bg-indigo-50 flex items-center justify-center",
            ),
            class_name="flex items-start justify-between",
        ),
        rx.el.div(
            rx.el.span(
                kpi["value"], class_name="text-3xl font-bold text-gray-900"
            ),
            class_name="mt-4",
        ),
        class_name="p-6 bg-white border border-gray-100 rounded-2xl shadow-[0_1px_3px_rgba(0,0,0,0.05)] hover:shadow-md transition-shadow",
    )


def dashboard_page() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.h2(
                    "Welcome back, Hub Manager",
                    class_name="text-2xl font-bold text-gray-900",
                ),
                rx.el.p(
                    "Here's what's happening at Downtown Cloud Hub today.",
                    class_name="text-sm text-gray-500 mt-1",
                ),
            ),
            rx.el.button(
                rx.icon("download", class_name="h-4 w-4 mr-2"),
                "Download Report",
                class_name="flex items-center px-4 py-2 bg-white border border-gray-200 rounded-lg text-sm font-medium hover:bg-gray-50 transition-all",
            ),
            class_name="flex justify-between items-end mb-8",
        ),
        rx.el.div(
            rx.foreach(DashboardState.kpis, lambda k: kpi_card(k[0], k[1])),
            class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.h3(
                    "Weekly Revenue",
                    class_name="text-lg font-bold text-gray-900 mb-6",
                ),
                rx.recharts.area_chart(
                    rx.recharts.cartesian_grid(
                        vertical=False, stroke_dasharray="3 3", stroke="#f1f5f9"
                    ),
                    rx.recharts.graphing_tooltip(
                        content_style={
                            "borderRadius": "12px",
                            "border": "none",
                            "boxShadow": "0 10px 15px -3px rgba(0,0,0,0.1)",
                        }
                    ),
                    rx.recharts.x_axis(
                        data_key="day",
                        axis_line=False,
                        tick_line=False,
                        custom_attrs={"fontSize": 12, "color": "#94a3b8"},
                    ),
                    rx.recharts.y_axis(
                        axis_line=False,
                        tick_line=False,
                        custom_attrs={"fontSize": 12, "color": "#94a3b8"},
                    ),
                    rx.recharts.area(
                        data_key="sales",
                        stroke="#4f46e5",
                        fill="#4f46e5",
                        fill_opacity=0.1,
                        stroke_width=3,
                        type_="monotone",
                    ),
                    data=DashboardState.sales_data,
                    width="100%",
                    height=300,
                ),
                class_name="lg:col-span-2 p-6 bg-white border border-gray-100 rounded-2xl shadow-sm",
            ),
            rx.el.div(
                rx.el.h3(
                    "Top Selling Items",
                    class_name="text-lg font-bold text-gray-900 mb-6",
                ),
                rx.el.div(
                    rx.foreach(
                        DashboardState.top_items,
                        lambda item: rx.el.div(
                            rx.el.div(
                                rx.el.span(
                                    item["rank"].to_string(),
                                    class_name="text-xs font-bold text-gray-400 w-4",
                                ),
                                rx.el.span(
                                    item["name"],
                                    class_name="text-sm font-semibold text-gray-700",
                                ),
                                class_name="flex items-center gap-4",
                            ),
                            rx.el.span(
                                item["sold"].to_string() + " sold",
                                class_name="text-sm font-medium text-indigo-600 bg-indigo-50 px-2 py-0.5 rounded-lg",
                            ),
                            class_name="flex items-center justify-between p-3 rounded-xl hover:bg-gray-50 transition-all border-b border-gray-50 last:border-0",
                        ),
                    ),
                    class_name="flex flex-col gap-1",
                ),
                class_name="p-6 bg-white border border-gray-100 rounded-2xl shadow-sm",
            ),
            class_name="grid grid-cols-1 lg:grid-cols-3 gap-6 mb-8",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.h3(
                    "Peak Hours",
                    class_name="text-lg font-bold text-gray-900 mb-6",
                ),
                rx.recharts.bar_chart(
                    rx.recharts.cartesian_grid(
                        vertical=False, stroke_dasharray="3 3", stroke="#f1f5f9"
                    ),
                    rx.recharts.x_axis(
                        data_key="hour",
                        axis_line=False,
                        tick_line=False,
                        custom_attrs={"fontSize": 12},
                    ),
                    rx.recharts.y_axis(
                        axis_line=False,
                        tick_line=False,
                        custom_attrs={"fontSize": 12},
                    ),
                    rx.recharts.bar(
                        data_key="orders", fill="#4f46e5", radius=[4, 4, 0, 0]
                    ),
                    data=DashboardState.peak_hours,
                    width="100%",
                    height=250,
                ),
                class_name="lg:col-span-2 p-6 bg-white border border-gray-100 rounded-2xl shadow-sm",
            ),
            rx.el.div(
                rx.el.h3(
                    "Recent Activity",
                    class_name="text-lg font-bold text-gray-900 mb-6",
                ),
                rx.el.div(
                    rx.foreach(
                        DashboardState.recent_activity,
                        lambda act: rx.el.div(
                            rx.el.div(
                                rx.el.div(
                                    class_name="h-2 w-2 rounded-full bg-indigo-500"
                                ),
                                class_name="mt-1.5 flex flex-col items-center",
                            ),
                            rx.el.div(
                                rx.el.p(
                                    act["action"],
                                    class_name="text-sm font-medium text-gray-800",
                                ),
                                rx.el.p(
                                    act["time"] + " by " + act["user"],
                                    class_name="text-xs text-gray-500 mt-0.5",
                                ),
                                class_name="pb-4",
                            ),
                            class_name="flex gap-4",
                        ),
                    ),
                    class_name="flex flex-col",
                ),
                class_name="p-6 bg-white border border-gray-100 rounded-2xl shadow-sm overflow-hidden",
            ),
            class_name="grid grid-cols-1 lg:grid-cols-3 gap-6",
        ),
        class_name="animate-in fade-in duration-500",
    )