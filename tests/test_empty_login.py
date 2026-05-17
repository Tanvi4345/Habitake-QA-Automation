from pages.login_page import LoginPage

from utils.config import BASE_URL


def test_empty_login(page):

    login = LoginPage(page)

    # Open Login Page
    login.open_login(BASE_URL)

    page.wait_for_timeout(3000)

    # Click Login Without Data
    page.locator(
        "button:has-text('Login')"
    ).click()

    print(
        "Login Button Clicked Without Credentials"
    )

    # Validation Message
    validation = page.locator(
        "text=Email is required"
    )

    validation.wait_for(
        state="visible",
        timeout=10000
    )

    assert validation.is_visible()

    print(
        "Empty Login Validation Passed"
    )

    # Screenshot
    page.screenshot(
        path="empty_login.png",
        full_page=True
    )

    page.wait_for_timeout(5000)