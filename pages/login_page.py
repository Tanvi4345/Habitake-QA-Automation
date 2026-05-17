from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, page):

        super().__init__(page)

        self.email_input = (
            "input[placeholder='Enter Email']"
        )

        self.password_input = (
            "input[placeholder='Password']"
        )

        self.login_btn = (
            "button:has-text('Login')"
        )

    # ====================================
    # OPEN LOGIN PAGE
    # ====================================

    def open_login(self, url):

        self.open(url)

    # ====================================
    # LOGIN
    # ====================================

    def login(self, email, password):

        self.fill(
            self.email_input,
            email
        )

        self.fill(
            self.password_input,
            password
        )

        self.click(
            self.login_btn
        )

        self.page.wait_for_timeout(6000)

        print(
            "Login Successful"
        )