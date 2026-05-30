import reflex as rx
from app.states.navigation_state import NavigationState
from app.states.notification_state import NotificationState
from app.states.auth_state import AuthState


def header() -> rx.Component:
    return rx.el.header(
        rx.el.div(
            rx.el.button(
                rx.icon("menu", class_name="h-6 w-6"),
                on_click=NavigationState.toggle_sidebar,
                class_name="lg:hidden p-2 text-gray-500 hover:bg-gray-100 rounded-md",
            ),
            rx.el.div(
                rx.el.select(
                    rx.el.option("Downtown Cloud Hub", value="downtown"),
                    rx.el.option("Westside Kitchens", value="westside"),
                    rx.el.option("Eastside Express", value="eastside"),
                    class_name="bg-transparent border-none text-sm font-semibold text-gray-700 focus:ring-0 cursor-pointer appearance-none",
                ),
                rx.icon(
                    "chevron-down", class_name="h-4 w-4 text-gray-400 ml-1"
                ),
                class_name="flex items-center ml-4 px-3 py-1.5 border border-gray-200 rounded-lg hover:border-gray-300 transition-all bg-white",
            ),
            class_name="flex items-center",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.button(
                    rx.icon("bell", class_name="h-5 w-5 text-gray-500"),
                    rx.cond(
                        NotificationState.unread_count > 0,
                        rx.el.span(
                            NotificationState.unread_count.to_string(),
                            class_name="absolute -top-1 -right-1 flex h-4 w-4 items-center justify-center rounded-full bg-red-500 text-[10px] font-bold text-white",
                        ),
                    ),
                    on_click=NotificationState.toggle_notifications,
                    class_name="relative p-2 hover:bg-gray-100 rounded-full transition-all",
                ),
                rx.cond(
                    NotificationState.show_notifications,
                    rx.el.div(
                        rx.el.div(
                            rx.el.h3(
                                "Notifications",
                                class_name="text-sm font-bold text-gray-900",
                            ),
                            rx.el.button(
                                "Mark all read",
                                on_click=NotificationState.mark_all_read,
                                class_name="text-xs font-semibold text-indigo-600 hover:text-indigo-800 transition-colors",
                            ),
                            class_name="flex justify-between items-center p-4 border-b border-gray-100",
                        ),
                        rx.el.div(
                            rx.foreach(
                                NotificationState.notifications,
                                lambda n: rx.el.div(
                                    rx.el.p(
                                        n["title"],
                                        class_name="text-sm font-semibold text-gray-900",
                                    ),
                                    rx.el.p(
                                        n["message"],
                                        class_name="text-xs text-gray-500 mt-1",
                                    ),
                                    class_name=rx.cond(
                                        n["unread"],
                                        "p-4 bg-indigo-50/50 border-b border-gray-100",
                                        "p-4 bg-white border-b border-gray-100",
                                    ),
                                ),
                            ),
                            class_name="max-h-[300px] overflow-y-auto",
                        ),
                        class_name="absolute top-full mt-2 right-0 w-80 bg-white border border-gray-100 shadow-xl rounded-xl overflow-hidden z-50",
                    ),
                ),
                class_name="relative",
            ),
            rx.el.div(
                rx.image(
                    src=f"https://api.dicebear.com/9.x/notionists/svg?seed={AuthState.current_user_email}",
                    class_name="h-8 w-8 rounded-full bg-gray-100",
                ),
                rx.el.div(
                    rx.el.p(
                        AuthState.current_user_name,
                        class_name="text-sm font-bold text-gray-900 leading-tight",
                    ),
                    rx.el.p(
                        AuthState.current_user_email,
                        class_name="text-xs text-gray-500 leading-tight",
                    ),
                    class_name="hidden md:flex flex-col ml-2",
                ),
                rx.el.button(
                    rx.icon("log-out", class_name="h-4 w-4 mr-1.5"),
                    rx.el.span("Logout", class_name="text-sm font-semibold"),
                    on_click=AuthState.logout,
                    class_name="ml-3 flex items-center px-3 py-1.5 border border-gray-200 rounded-lg text-gray-700 hover:bg-gray-50 transition-all",
                ),
                class_name="ml-4 flex items-center",
            ),
            class_name="flex items-center gap-4",
        ),
        class_name="sticky top-0 z-40 flex h-16 items-center justify-between border-b border-gray-100 bg-white/80 backdrop-blur-md px-6",
    )