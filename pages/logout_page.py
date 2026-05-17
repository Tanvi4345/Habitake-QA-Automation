from pages.base_page import BasePage


class LogoutPage(BasePage):

    def __init__(self, page):

        super().__init__(page)

    # ====================================
    # LOGOUT
    # ====================================

    def logout(self):

        # Wait dropdown visible
        self.page.wait_for_timeout(3000)

        # ====================================
        # CLICK LOGOUT BUTTON
        # ====================================

        logout_btn = self.page.locator("text=Logout").last

        logout_btn.wait_for(state="visible", timeout=15000)

        logout_btn.click(force=True)

        print("Logout Clicked")

        self.page.wait_for_timeout(3000)

        # ====================================
        # HANDLE CONFIRMATION POPUP
        # ====================================

        yes_btn = self.page.locator("button:has-text('Yes')")

        if yes_btn.count() > 0:

            yes_btn.first.click(force=True)

            print("Logout Confirmation Accepted")

        self.page.wait_for_timeout(5000)

        # ====================================
        # VERIFY LOGIN PAGE
        # ====================================

        self.page.wait_for_selector("text=Login")

        print("Logout Successful")
