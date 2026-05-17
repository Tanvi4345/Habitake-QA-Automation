from pages.login_page import LoginPage

from utils.config import BASE_URL


def test_password_validation(page):

    login = LoginPage(page)

    # Open Login Page
    login.open_login(BASE_URL)

    page.wait_for_timeout(3000)

    # Email Field
    email = page.locator(
        "input[placeholder='Enter Email']"
    )

    email.click()

    email.fill(
        "test@gmail.com"
    )

    print(
        "Email Entered"
    )

    # Password Field
    password = page.locator(
        "input[type='password']"
    )

    password.click()

    password.fill(
        "12345678"
    )

    print(
        "Short Password Entered"
    )
    

    # CLICK LOGIN BUTTON
    page.locator(
        "button:has-text('Login')"
    ).click()

    print(
        "Login Button Clicked"
    )

    # VALIDATION MESSAGE
    validation = page.locator(
        "text=Password must be at least 12 characters long."
    )

    validation.wait_for(
        state="visible",
        timeout=1000
    )

    print(
        "Password Validation Passed"
    )

    # Screenshot
    page.screenshot(
        path="password_validation.png",
        full_page=True
    )

        # HOLD SCREEN
    page.wait_for_timeout(10000)