from pages.base_page import BasePage


class HomePage(BasePage):

    def __init__(self, page):

        super().__init__(page)

        self.add_property_btn = (
            "text=Add Property"
        )

    # ====================================
    # VERIFY HOME PAGE
    # ====================================

    def verify_home_page(self):

        self.page.wait_for_selector(
            self.add_property_btn
        )

        print(
            "Home Page Loaded"
        )

    # ====================================
    # OPEN ADD PROPERTY
    # ====================================

    def open_add_property(self):

        self.page.locator(
            self.add_property_btn
        ).first.click()

        self.page.wait_for_timeout(5000)

        print(
            "Add Property Page Opened"
        )

    # ====================================
    # HANDLE SUCCESS POPUP
    # ====================================

    def handle_success_popup(self):

        try:

            success_popup = self.page.locator(
                "text=Property processed successfully"
            )

            success_popup.wait_for(
                state="visible",
                timeout=10000
            )

            print(
                "Success Popup Displayed"
            )

            # Screenshot
            self.page.screenshot(
                path="property_success_popup.png",
                full_page=True
            )

            # Keep popup visible
            self.page.wait_for_timeout(5000)

            # Close popup
            close_btn = self.page.locator(
                "button"
            ).filter(
                has_text="✕"
            ).first

            if close_btn.count() > 0:

                close_btn.click(
                    force=True
                )

                print(
                    "Success Popup Closed"
                )

        except:

            print(
                "Success Popup Not Displayed"
            )

    # ====================================
    # OPEN PROFILE DROPDOWN
    # ====================================

    def open_profile_dropdown(self):

        self.page.wait_for_timeout(5000)

        self.page.evaluate(
            "window.scrollTo(0,0)"
        )

        self.page.wait_for_timeout(2000)

        profile_section = self.page.locator(
            "text=kylie"
        ).first

        profile_section.wait_for(
            state="visible",
            timeout=15000
        )

        profile_section.click(
            force=True
        )

        print(
            "Profile Dropdown Opened"
        )

        self.page.wait_for_timeout(3000)