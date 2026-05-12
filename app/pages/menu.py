import reflex as rx
from app.states.menu_state import MenuState


def category_tab(cat: str) -> rx.Component:
    is_active = MenuState.active_category == cat
    return rx.el.button(
        cat,
        on_click=lambda: MenuState.set_category(cat),
        class_name=rx.cond(
            is_active,
            "px-6 py-2 bg-indigo-600 text-white rounded-full font-bold shadow-md transition-all",
            "px-6 py-2 bg-white text-gray-600 hover:bg-gray-100 rounded-full font-semibold border border-gray-200 transition-all",
        ),
    )


def menu_item_card(item: dict) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.image(
                src="/placeholder.svg", class_name="h-40 w-full object-cover"
            ),
            rx.el.div(
                item["category"],
                class_name="absolute top-3 left-3 px-2 py-1 bg-white/90 backdrop-blur rounded-lg text-[10px] font-bold text-indigo-600",
            ),
            class_name="relative",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.h4(
                    item["name"],
                    class_name="text-base font-bold text-gray-900 truncate",
                ),
                rx.el.p(
                    item["description"],
                    class_name="text-xs text-gray-500 line-clamp-2 mt-1",
                ),
                class_name="h-12 mb-2",
            ),
            rx.el.div(
                rx.el.span(
                    f"₹{item['price']:.2f}",
                    class_name="text-lg font-black text-indigo-600",
                ),
                rx.el.div(
                    rx.el.label(
                        rx.el.input(
                            type="checkbox",
                            checked=item["available"],
                            on_change=lambda _: MenuState.toggle_availability(
                                item["id"]
                            ),
                            class_name="sr-only peer",
                        ),
                        rx.el.div(
                            class_name="w-9 h-5 bg-gray-200 peer-focus:outline-none rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-4 after:w-4 after:transition-all peer-checked:bg-indigo-600"
                        ),
                        class_name="relative inline-flex items-center cursor-pointer",
                    ),
                    class_name="flex items-center",
                ),
                class_name="flex items-center justify-between mt-4",
            ),
            class_name="p-4",
        ),
        class_name="bg-white rounded-2xl border border-gray-100 shadow-sm hover:shadow-md transition-all overflow-hidden",
    )


def menu_modal() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.form(
                    rx.el.h3(
                        "Add New Menu Item", class_name="text-xl font-bold mb-6"
                    ),
                    rx.el.div(
                        rx.el.label(
                            "Item Name",
                            class_name="text-xs font-bold text-gray-500 uppercase",
                        ),
                        rx.el.input(
                            name="name",
                            placeholder="e.g. Smash Burger",
                            class_name="w-full p-3 bg-gray-50 border border-gray-200 rounded-xl mt-1 mb-4",
                        ),
                        rx.el.label(
                            "Description",
                            class_name="text-xs font-bold text-gray-500 uppercase",
                        ),
                        rx.el.input(
                            name="description",
                            placeholder="Juicy beef patty with...",
                            class_name="w-full p-3 bg-gray-50 border border-gray-200 rounded-xl mt-1 mb-4",
                        ),
                        rx.el.div(
                            rx.el.div(
                                rx.el.label(
                                    "Price",
                                    class_name="text-xs font-bold text-gray-500 uppercase",
                                ),
                                rx.el.input(
                                    name="price",
                                    type="number",
                                    step="0.01",
                                    placeholder="12.99",
                                    class_name="w-full p-3 bg-gray-50 border border-gray-200 rounded-xl mt-1",
                                ),
                                class_name="flex-1",
                            ),
                            rx.el.div(
                                rx.el.label(
                                    "Category",
                                    class_name="text-xs font-bold text-gray-500 uppercase",
                                ),
                                rx.el.select(
                                    rx.foreach(
                                        MenuState.categories,
                                        lambda c: rx.el.option(c, value=c),
                                    ),
                                    name="category",
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
                            on_click=lambda: MenuState.set_show_item_modal(
                                False
                            ),
                            type="button",
                            class_name="px-6 py-3 border border-gray-200 rounded-xl font-bold",
                        ),
                        rx.el.button(
                            "Save Item",
                            type="submit",
                            class_name="px-6 py-3 bg-indigo-600 text-white rounded-xl font-bold shadow-lg shadow-indigo-200",
                        ),
                        class_name="flex justify-end gap-3 mt-6",
                    ),
                    on_submit=MenuState.handle_submit,
                    class_name="bg-white p-8 rounded-3xl w-full max-w-lg",
                ),
                class_name="fixed inset-0 bg-black/50 backdrop-blur-sm flex items-center justify-center z-[100]",
            ),
            class_name="relative",
        ),
        class_name=rx.cond(MenuState.show_item_modal, "block", "hidden"),
    )


def menu_page() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.h2(
                    "Menu Management",
                    class_name="text-2xl font-bold text-gray-900",
                ),
                rx.el.p(
                    "Manage your digital catalog and item availability.",
                    class_name="text-sm text-gray-500 mt-1",
                ),
            ),
            rx.el.button(
                rx.icon("plus", class_name="h-4 w-4 mr-2"),
                "Add New Item",
                on_click=MenuState.open_add_modal,
                class_name="flex items-center px-4 py-2 bg-indigo-600 text-white rounded-lg text-sm font-bold hover:bg-indigo-700 transition-all shadow-md shadow-indigo-200",
            ),
            class_name="flex justify-between items-end mb-8",
        ),
        rx.el.div(
            rx.el.div(
                rx.foreach(MenuState.categories, category_tab),
                class_name="flex gap-2 flex-wrap mb-8",
            ),
            rx.el.div(
                rx.foreach(MenuState.filtered_menu, menu_item_card),
                class_name="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6",
            ),
        ),
        menu_modal(),
        class_name="animate-in fade-in duration-500",
    )