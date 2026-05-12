import reflex as rx


class NavigationState(rx.State):
    active_page: str = "Dashboard"
    sidebar_open: bool = False

    @rx.event
    def set_active_page(self, page: str):
        self.active_page = page
        self.sidebar_open = False
        return rx.redirect(f"/{(page.lower() if page != 'Dashboard' else '')}")

    @rx.event
    def toggle_sidebar(self):
        self.sidebar_open = not self.sidebar_open