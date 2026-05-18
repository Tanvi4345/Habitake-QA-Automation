from pages.login_page import LoginPage

from utils.config import BASE_URL


def test_invalid_email_format(page):

    login = LoginPage(page)

    login.open_login(BASE_URL)

    page.wait_for_timeout(3000)

    # Email
    page.locator(
        "input[placeholder='Enter Email']"
    ).fill(
        "invalidemail"
    )

    # Password
    page.locator(
        "input[type='password']"
    ).fill(
        "Password@1234"
    )

    # Login
    page.locator(
        "button:has-text('Login')"
    ).click()

    print(
        "Invalid Email Format Entered"
    )

    # Validation
    validation = page.locator(
        "text=Invalid email"
    )

    validation.wait_for(
        state="visible",
        timeout=10000
    )

    assert validation.is_visible()

    print(
        "Invalid Email Validation Passed"
    )

    page.screenshot(
        path="Playwright Habitake/screenshots/invalid_email.png",
        full_page=True
    )

    page.wait_for_timeout(5000)