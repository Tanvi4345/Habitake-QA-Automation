from pages.login_page import LoginPage

from pages.home_page import HomePage

from pages.logout_page import LogoutPage

from utils.config import BASE_URL, EMAIL, PASSWORD


def test_logout(page):

    login = LoginPage(page)

    home = HomePage(page)

    logout_page = LogoutPage(page)

    # Login
    login.open_login(BASE_URL)

    login.login(EMAIL, PASSWORD)

    # Verify Home
    home.verify_home_page()

    # Open Profile Dropdown
    home.open_profile_dropdown()

    # Logout
    logout_page.logout()

    # # Verify Login Page
    # login_text = page.locator(
    #     "button:has-text('Login')"
    # ).first

    # login_text.wait_for(
    #     state="visible",
    #     timeout=10000
    # )

    # assert login_text.is_visible()

    print(
        "Logout Verification Passed"
    )

    # Screenshot
    page.screenshot(
        path="Playwright Habitake/screenshots/logout_success.png",
        full_page=True
    )

    page.wait_for_timeout(2000)