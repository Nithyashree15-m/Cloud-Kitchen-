import reflex as rx


class NavigationState(rx.State):
    active_page: str = "Dashboard"
    sidebar_open: bool = False

    @rx.event
    def set_active_page(self, page: str):
        self.active_page = page
        self.sidebar_open = False
        routes = {
            "Dashboard": "/",
            "Orders": "/orders",
            "Kitchen": "/kitchen",
            "Menu": "/menu",
            "Inventory": "/inventory",
            "Staff": "/staff",
            "Customers": "/customers",
            "Delivery": "/delivery",
            "Billing": "/billing",
            "Excel Data": "/excel",
        }
        return rx.redirect(routes.get(page, "/"))

    @rx.event
    def toggle_sidebar(self):
        self.sidebar_open = not self.sidebar_open