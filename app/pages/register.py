import reflex as rx
from app.states.auth_state import AuthState


def register_page() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.image(
                        src="/cloud_white_nine.png",
                        class_name="h-12 w-12 rounded-xl object-cover shadow-sm border border-gray-100",
                    ),
                    rx.el.h1(
                        "Create your account",
                        class_name="text-2xl font-bold text-gray-900 mt-4",
                    ),
                    rx.el.p(
                        "Join Cloud Nine Cuisine in seconds",
                        class_name="text-sm text-gray-500 mt-1",
                    ),
                    class_name="flex flex-col items-center mb-8",
                ),
                rx.el.form(
                    rx.el.div(
                        rx.el.label(
                            "Full Name",
                            class_name="text-xs font-bold text-gray-500 uppercase tracking-wider",
                        ),
                        rx.el.input(
                            name="name",
                            type="text",
                            placeholder="Jane Doe",
                            required=True,
                            class_name="w-full p-3 mt-1 bg-gray-50 border border-gray-200 rounded-xl text-sm text-gray-900 focus:bg-white focus:ring-2 focus:ring-indigo-100 focus:border-indigo-600 transition-all",
                        ),
                        class_name="mb-4",
                    ),
                    rx.el.div(
                        rx.el.label(
                            "Email",
                            class_name="text-xs font-bold text-gray-500 uppercase tracking-wider",
                        ),
                        rx.el.input(
                            name="email",
                            type="email",
                            placeholder="you@kitchen.com",
                            required=True,
                            class_name="w-full p-3 mt-1 bg-gray-50 border border-gray-200 rounded-xl text-sm text-gray-900 focus:bg-white focus:ring-2 focus:ring-indigo-100 focus:border-indigo-600 transition-all",
                        ),
                        class_name="mb-4",
                    ),
                    rx.el.div(
                        rx.el.label(
                            "Password",
                            class_name="text-xs font-bold text-gray-500 uppercase tracking-wider",
                        ),
                        rx.el.input(
                            name="password",
                            type="password",
                            placeholder="At least 6 characters",
                            required=True,
                            class_name="w-full p-3 mt-1 bg-gray-50 border border-gray-200 rounded-xl text-sm text-gray-900 focus:bg-white focus:ring-2 focus:ring-indigo-100 focus:border-indigo-600 transition-all",
                        ),
                        class_name="mb-4",
                    ),
                    rx.el.div(
                        rx.el.label(
                            "Confirm Password",
                            class_name="text-xs font-bold text-gray-500 uppercase tracking-wider",
                        ),
                        rx.el.input(
                            name="confirm_password",
                            type="password",
                            placeholder="Re-enter password",
                            required=True,
                            class_name="w-full p-3 mt-1 bg-gray-50 border border-gray-200 rounded-xl text-sm text-gray-900 focus:bg-white focus:ring-2 focus:ring-indigo-100 focus:border-indigo-600 transition-all",
                        ),
                        class_name="mb-4",
                    ),
                    rx.cond(
                        AuthState.error_message != "",
                        rx.el.div(
                            rx.icon(
                                "circle_alert",
                                class_name="h-4 w-4 mr-2 shrink-0",
                            ),
                            rx.el.span(
                                AuthState.error_message,
                                class_name="text-sm font-medium",
                            ),
                            class_name="flex items-center bg-red-50 text-red-600 p-3 rounded-xl mb-4 border border-red-100",
                        ),
                    ),
                    rx.el.button(
                        "Create Account",
                        type="submit",
                        class_name="w-full py-3 bg-indigo-600 text-white rounded-xl font-bold shadow-lg shadow-indigo-200 hover:bg-indigo-700 active:scale-[0.99] transition-all",
                    ),
                    on_submit=AuthState.handle_register,
                    reset_on_submit=False,
                ),
                rx.el.div(
                    rx.el.span(
                        "Already have an account? ",
                        class_name="text-sm text-gray-500",
                    ),
                    rx.el.a(
                        "Sign in",
                        href="/login",
                        class_name="text-sm font-bold text-indigo-600 hover:text-indigo-800",
                    ),
                    class_name="flex justify-center mt-6",
                ),
                rx.el.div(
                    rx.icon(
                        "info",
                        class_name="h-3.5 w-3.5 text-gray-400 mr-2 shrink-0",
                    ),
                    rx.el.span(
                        "Your account is stored locally in this browser only.",
                        class_name="text-xs text-gray-500",
                    ),
                    class_name="flex items-center justify-center mt-6 p-3 bg-gray-50 rounded-xl border border-gray-100",
                ),
                class_name="bg-white p-8 rounded-3xl border border-gray-100 shadow-sm w-full max-w-md",
            ),
            class_name="min-h-screen w-screen bg-gray-50 flex items-center justify-center p-6 font-['Inter']",
        ),
    )