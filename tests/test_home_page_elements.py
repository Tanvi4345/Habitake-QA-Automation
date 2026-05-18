from pages.login_page import LoginPage

from pages.home_page import HomePage

from utils.config import BASE_URL, EMAIL, PASSWORD


def test_home_page_elements(page):

    login = LoginPage(page)

    home = HomePage(page)

    # ====================================
    # LOGIN
    # ====================================

    login.open_login(BASE_URL)

    login.login(EMAIL, PASSWORD)

    print(
        "Login Successful"
    )

    # ====================================
    # VERIFY HOME PAGE
    # ====================================

    home.verify_home_page()

    # ====================================
    # ADD PROPERTY BUTTON
    # ====================================

    add_property_btn = page.locator(
        "a[href='/en/create-property/']"
    ).first

    add_property_btn.wait_for(
        state="visible",
        timeout=10000
    )

    assert add_property_btn.is_visible()

    print(
        "Add Property Button Visible"
    )

    # ====================================
    # SCREENSHOT
    # ====================================

    page.screenshot(
        path="Playwright Habitake/screenshots/home_page_elements.png",
        full_page=True
    )

    print(
        "Home Page Verification Passed"
    )

    page.wait_for_timeout(5000)