import reflex as rx
from app.states.staff_state import StaffState


def staff_modal() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.form(
                    rx.el.h3(
                        "Add Staff Member", class_name="text-xl font-bold mb-6"
                    ),
                    rx.el.div(
                        rx.el.label(
                            "Full Name",
                            class_name="text-xs font-bold text-gray-500 uppercase",
                        ),
                        rx.el.input(
                            name="name",
                            placeholder="e.g. John Doe",
                            class_name="w-full p-3 bg-gray-50 border border-gray-200 rounded-xl mt-1 mb-4",
                        ),
                        rx.el.label(
                            "Email",
                            class_name="text-xs font-bold text-gray-500 uppercase",
                        ),
                        rx.el.input(
                            name="email",
                            type="email",
                            placeholder="john@example.com",
                            class_name="w-full p-3 bg-gray-50 border border-gray-200 rounded-xl mt-1 mb-4",
                        ),
                        rx.el.div(
                            rx.el.div(
                                rx.el.label(
                                    "Phone",
                                    class_name="text-xs font-bold text-gray-500 uppercase",
                                ),
                                rx.el.input(
                                    name="phone",
                                    placeholder="555-1234",
                                    class_name="w-full p-3 bg-gray-50 border border-gray-200 rounded-xl mt-1",
                                ),
                                class_name="flex-1",
                            ),
                            rx.el.div(
                                rx.el.label(
                                    "Role",
                                    class_name="text-xs font-bold text-gray-500 uppercase",
                                ),
                                rx.el.select(
                                    rx.el.option("Admin", value="Admin"),
                                    rx.el.option("Manager", value="Manager"),
                                    rx.el.option("Cook", value="Cook"),
                                    rx.el.option("Server", value="Server"),
                                    name="role",
                                    class_name="w-full p-3 bg-gray-50 border border-gray-200 rounded-xl mt-1 appearance-none",
                                ),
                                class_name="flex-1",
                            ),
                            class_name="flex gap-4 mb-4",
                        ),
                        class_name="flex flex-col",
                    ),
                    rx.el.div(
                        rx.el.button(
                            "Cancel",
                            on_click=StaffState.toggle_modal,
                            type="button",
                            class_name="px-6 py-3 border border-gray-200 rounded-xl font-bold",
                        ),
                        rx.el.button(
                            "Save Staff",
                            type="submit",
                            class_name="px-6 py-3 bg-indigo-600 text-white rounded-xl font-bold shadow-lg shadow-indigo-200",
                        ),
                        class_name="flex justify-end gap-3 mt-6",
                    ),
                    on_submit=StaffState.handle_submit,
                    class_name="bg-white p-8 rounded-3xl w-full max-w-lg",
                ),
                class_name="fixed inset-0 bg-black/50 backdrop-blur-sm flex items-center justify-center z-[100]",
            ),
            class_name="relative",
        ),
        class_name=rx.cond(StaffState.show_modal, "block", "hidden"),
    )


def staff_page() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.h2(
                    "Staff & Access Control",
                    class_name="text-2xl font-bold text-gray-900",
                ),
                rx.el.p(
                    "Manage your team members and their roles.",
                    class_name="text-sm text-gray-500 mt-1",
                ),
            ),
            rx.el.button(
                rx.icon("plus", class_name="h-4 w-4 mr-2"),
                "Add Staff",
                on_click=StaffState.toggle_modal,
                class_name="flex items-center px-4 py-2 bg-indigo-600 text-white rounded-lg text-sm font-bold hover:bg-indigo-700 transition-all shadow-md shadow-indigo-200",
            ),
            class_name="flex justify-between items-end mb-8",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.span(
                    "Total Staff",
                    class_name="text-sm font-medium text-gray-500",
                ),
                rx.el.span(
                    StaffState.total_staff.to_string(),
                    class_name="text-3xl font-bold text-gray-900 mt-2",
                ),
                class_name="p-6 bg-white border border-gray-100 rounded-2xl shadow-sm flex flex-col",
            ),
            rx.el.div(
                rx.el.span(
                    "On Duty Now",
                    class_name="text-sm font-medium text-gray-500",
                ),
                rx.el.span(
                    StaffState.on_duty_count.to_string(),
                    class_name="text-3xl font-bold text-indigo-600 mt-2",
                ),
                class_name="p-6 bg-white border border-gray-100 rounded-2xl shadow-sm flex flex-col",
            ),
            rx.el.div(
                rx.el.span(
                    "Managers", class_name="text-sm font-medium text-gray-500"
                ),
                rx.el.span(
                    StaffState.manager_count.to_string(),
                    class_name="text-3xl font-bold text-gray-900 mt-2",
                ),
                class_name="p-6 bg-white border border-gray-100 rounded-2xl shadow-sm flex flex-col",
            ),
            rx.el.div(
                rx.el.span(
                    "Cooks", class_name="text-sm font-medium text-gray-500"
                ),
                rx.el.span(
                    StaffState.cook_count.to_string(),
                    class_name="text-3xl font-bold text-gray-900 mt-2",
                ),
                class_name="p-6 bg-white border border-gray-100 rounded-2xl shadow-sm flex flex-col",
            ),
            class_name="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8",
        ),
        rx.el.div(
            rx.el.table(
                rx.el.thead(
                    rx.el.tr(
                        rx.el.th(
                            "Name",
                            class_name="px-6 py-3 text-left text-xs font-bold text-gray-400 uppercase tracking-widest",
                        ),
                        rx.el.th(
                            "Role",
                            class_name="px-6 py-3 text-left text-xs font-bold text-gray-400 uppercase tracking-widest",
                        ),
                        rx.el.th(
                            "Email",
                            class_name="px-6 py-3 text-left text-xs font-bold text-gray-400 uppercase tracking-widest",
                        ),
                        rx.el.th(
                            "Phone",
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
                        StaffState.staff,
                        lambda s: rx.el.tr(
                            rx.el.td(
                                s["name"],
                                class_name="px-6 py-4 text-sm font-bold text-gray-900",
                            ),
                            rx.el.td(
                                rx.el.span(
                                    s["role"],
                                    class_name=rx.match(
                                        s["role"],
                                        (
                                            "Admin",
                                            "bg-purple-50 text-purple-600 px-2.5 py-1 rounded-full text-xs font-bold",
                                        ),
                                        (
                                            "Manager",
                                            "bg-blue-50 text-blue-600 px-2.5 py-1 rounded-full text-xs font-bold",
                                        ),
                                        (
                                            "Cook",
                                            "bg-orange-50 text-orange-600 px-2.5 py-1 rounded-full text-xs font-bold",
                                        ),
                                        (
                                            "Server",
                                            "bg-green-50 text-green-600 px-2.5 py-1 rounded-full text-xs font-bold",
                                        ),
                                        "bg-gray-100 text-gray-500 px-2.5 py-1 rounded-full text-xs font-bold",
                                    ),
                                ),
                                class_name="px-6 py-4",
                            ),
                            rx.el.td(
                                s["email"],
                                class_name="px-6 py-4 text-sm text-gray-500",
                            ),
                            rx.el.td(
                                s["phone"],
                                class_name="px-6 py-4 text-sm text-gray-500",
                            ),
                            rx.el.td(
                                rx.el.span(
                                    s["status"],
                                    class_name=rx.cond(
                                        s["status"] == "Active",
                                        "text-green-600 font-bold text-sm",
                                        "text-gray-400 font-medium text-sm",
                                    ),
                                ),
                                class_name="px-6 py-4",
                            ),
                            class_name="border-b border-gray-50 hover:bg-gray-50 transition-all",
                        ),
                    )
                ),
                class_name="w-full table-auto",
            ),
            class_name="bg-white border border-gray-100 rounded-2xl shadow-sm overflow-hidden mb-8",
        ),
        staff_modal(),
        class_name="animate-in fade-in duration-500",
    )