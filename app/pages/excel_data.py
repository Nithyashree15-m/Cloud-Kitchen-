import reflex as rx
from app.states.excel_state import ExcelState, UPLOAD_ID
from app.states.order_state import OrderState
from app.states.menu_state import MenuState
from app.states.inventory_state import InventoryState
from app.states.staff_state import StaffState
from app.states.customer_state import CustomerState
from app.states.delivery_state import DeliveryState
from app.states.billing_state import BillingState


def summary_card(label: str, count, icon: str) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(icon, class_name="h-5 w-5 text-indigo-600"),
            class_name="h-10 w-10 rounded-lg bg-indigo-50 flex items-center justify-center mb-3",
        ),
        rx.el.span(
            label,
            class_name="text-xs font-bold text-gray-400 uppercase tracking-widest",
        ),
        rx.el.span(
            count.to_string(),
            class_name="text-2xl font-bold text-gray-900 mt-1",
        ),
        class_name="p-5 bg-white border border-gray-100 rounded-2xl shadow-sm flex flex-col",
    )


def sheet_pill(name: str) -> rx.Component:
    return rx.el.span(
        rx.icon("sheet", class_name="h-3 w-3 mr-1.5"),
        name,
        class_name="inline-flex items-center px-2.5 py-1 bg-gray-50 text-gray-700 text-xs font-bold rounded-lg border border-gray-100",
    )


def excel_data_page() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.h2(
                    "Excel Data", class_name="text-2xl font-bold text-gray-900"
                ),
                rx.el.p(
                    "Export all your operational data to Excel or restore from a backup workbook.",
                    class_name="text-sm text-gray-500 mt-1",
                ),
            ),
            class_name="mb-8",
        ),
        rx.el.div(
            summary_card("Orders", OrderState.orders.length(), "shopping-cart"),
            summary_card("Menu Items", MenuState.items.length(), "book-open"),
            summary_card("Inventory", InventoryState.items.length(), "package"),
            summary_card("Staff", StaffState.staff.length(), "users"),
            summary_card(
                "Customers",
                CustomerState.customers.length(),
                "circle_user_round",
            ),
            summary_card(
                "Deliveries", DeliveryState.deliveries.length(), "truck"
            ),
            summary_card(
                "Invoices", BillingState.invoices.length(), "credit-card"
            ),
            class_name="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-7 gap-4 mb-8",
        ),
        rx.cond(
            ExcelState.status_message != "",
            rx.el.div(
                rx.icon(
                    rx.cond(
                        ExcelState.is_error, "circle_alert", "circle_check"
                    ),
                    class_name="h-5 w-5 mr-3 shrink-0",
                ),
                rx.el.span(
                    ExcelState.status_message, class_name="text-sm font-medium"
                ),
                class_name=rx.cond(
                    ExcelState.is_error,
                    "flex items-center bg-red-50 text-red-600 p-4 rounded-2xl mb-6 border border-red-100",
                    "flex items-center bg-green-50 text-green-700 p-4 rounded-2xl mb-6 border border-green-100",
                ),
            ),
        ),
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.icon("download", class_name="h-5 w-5 text-indigo-600"),
                    class_name="h-10 w-10 rounded-lg bg-indigo-50 flex items-center justify-center mb-4",
                ),
                rx.el.h3(
                    "Export Data", class_name="text-lg font-bold text-gray-900"
                ),
                rx.el.p(
                    "Download all current operational records as a single .xlsx workbook with one sheet per module.",
                    class_name="text-sm text-gray-500 mt-2 mb-4",
                ),
                rx.el.div(
                    sheet_pill("orders"),
                    sheet_pill("menu"),
                    sheet_pill("inventory"),
                    sheet_pill("staff"),
                    sheet_pill("customers"),
                    sheet_pill("deliveries"),
                    sheet_pill("billing"),
                    class_name="flex flex-wrap gap-2 mb-6",
                ),
                rx.cond(
                    ExcelState.last_export_time != "",
                    rx.el.p(
                        "Last exported: " + ExcelState.last_export_time,
                        class_name="text-xs text-gray-400 mb-4",
                    ),
                ),
                rx.el.button(
                    rx.icon("download", class_name="h-4 w-4 mr-2"),
                    rx.cond(
                        ExcelState.is_processing,
                        "Processing...",
                        "Download Excel Workbook",
                    ),
                    on_click=ExcelState.export_data,
                    disabled=ExcelState.is_processing,
                    class_name="flex items-center justify-center w-full px-4 py-3 bg-indigo-600 text-white rounded-xl text-sm font-bold hover:bg-indigo-700 transition-all shadow-md shadow-indigo-200 disabled:opacity-50",
                ),
                class_name="p-6 bg-white border border-gray-100 rounded-2xl shadow-sm",
            ),
            rx.el.div(
                rx.el.div(
                    rx.icon("upload", class_name="h-5 w-5 text-indigo-600"),
                    class_name="h-10 w-10 rounded-lg bg-indigo-50 flex items-center justify-center mb-4",
                ),
                rx.el.h3(
                    "Import Data", class_name="text-lg font-bold text-gray-900"
                ),
                rx.el.p(
                    "Upload a previously exported .xlsx workbook to restore records. Only sheets present in the file will be imported.",
                    class_name="text-sm text-gray-500 mt-2 mb-4",
                ),
                rx.el.div(
                    rx.icon(
                        "triangle_alert",
                        class_name="h-4 w-4 mr-2 shrink-0 text-amber-600",
                    ),
                    rx.el.span(
                        "Warning: Importing overwrites existing browser-stored records for included sheets.",
                        class_name="text-xs font-medium text-amber-700",
                    ),
                    class_name="flex items-start bg-amber-50 p-3 rounded-xl border border-amber-100 mb-4",
                ),
                rx.upload.root(
                    rx.el.div(
                        rx.icon(
                            "cloud_upload",
                            class_name="h-10 w-10 text-gray-400 mb-3",
                        ),
                        rx.el.p(
                            "Drop .xlsx file here or click to browse",
                            class_name="text-sm font-semibold text-gray-700",
                        ),
                        rx.el.p(
                            "Accepted: .xlsx workbooks only",
                            class_name="text-xs text-gray-400 mt-1",
                        ),
                        class_name="flex flex-col items-center justify-center p-8 border-2 border-dashed border-gray-200 hover:border-indigo-400 rounded-xl cursor-pointer transition-all bg-gray-50/50",
                    ),
                    id=UPLOAD_ID,
                    accept={
                        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet": [
                            ".xlsx"
                        ],
                    },
                    multiple=False,
                    max_files=1,
                ),
                rx.el.div(
                    rx.foreach(
                        rx.selected_files(UPLOAD_ID),
                        lambda f: rx.el.div(
                            rx.icon(
                                "file_spreadsheet",
                                class_name="h-4 w-4 text-indigo-600 mr-2",
                            ),
                            rx.el.span(
                                f,
                                class_name="text-sm font-medium text-gray-700",
                            ),
                            class_name="flex items-center bg-indigo-50 px-3 py-2 rounded-lg mt-2 border border-indigo-100",
                        ),
                    ),
                    class_name="mb-4",
                ),
                rx.cond(
                    ExcelState.last_import_time != "",
                    rx.el.p(
                        "Last imported: " + ExcelState.last_import_time,
                        class_name="text-xs text-gray-400 mb-4 mt-2",
                    ),
                ),
                rx.el.div(
                    rx.el.button(
                        rx.icon("upload", class_name="h-4 w-4 mr-2"),
                        rx.cond(
                            ExcelState.is_processing,
                            "Processing...",
                            "Apply Import",
                        ),
                        type="button",
                        on_click=ExcelState.handle_upload(
                            rx.upload_files(upload_id=UPLOAD_ID)
                        ),
                        disabled=ExcelState.is_processing,
                        class_name="flex items-center justify-center flex-1 px-4 py-3 bg-indigo-600 text-white rounded-xl text-sm font-bold hover:bg-indigo-700 transition-all shadow-md shadow-indigo-200 disabled:opacity-50",
                    ),
                    rx.el.button(
                        "Clear",
                        type="button",
                        on_click=rx.clear_selected_files(UPLOAD_ID),
                        class_name="px-4 py-3 bg-white border border-gray-200 text-gray-700 rounded-xl text-sm font-bold hover:bg-gray-50 transition-all",
                    ),
                    class_name="flex gap-3 mt-4",
                ),
                class_name="p-6 bg-white border border-gray-100 rounded-2xl shadow-sm",
            ),
            class_name="grid grid-cols-1 lg:grid-cols-2 gap-6",
        ),
        class_name="animate-in fade-in duration-500",
    )