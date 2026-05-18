from pages.login_page import LoginPage

from utils.config import BASE_URL


def test_invalid_login(page):

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
        "kyli@yopmail.com"
    )

    print(
        "Invalid Email Entered"
    )

    # Password Field
    password = page.locator(
        "input[type='password']"
    )

    password.click()

    password.fill(
        "Password@1234"
    )

    print(
        "Invalid Password Entered"
    )

    # Click Login Button
    page.locator(
        "button:has-text('Login')"
    ).click()

    print(
        "Login Button Clicked"
    )

    # Error Toast
    error = page.locator(
        "text=Sign in failed. Invalid email or password."
    )

    error.wait_for(
        state="visible",
        timeout=15000
    )

    print(
        "Invalid Login Validation Passed"
    )

    # Screenshot
    page.screenshot(
        path="Playwright Habitake/screenshots/invalid_login.png",
        full_page=True
    )

    # Hold Screen
    page.wait_for_timeout(10000)