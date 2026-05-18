from pages.login_page import LoginPage

from pages.home_page import HomePage

from pages.add_property_page import AddPropertyPage

from utils.config import BASE_URL, EMAIL, PASSWORD


def test_property_without_price(page):

    login = LoginPage(page)

    home = HomePage(page)

    property_page = AddPropertyPage(page)

    # Login
    login.open_login(BASE_URL)

    login.login(EMAIL, PASSWORD)

    # Open Add Property
    home.open_add_property()

    # Fill Data
    property_page.select_property_type()

    property_page.fill_location()

    property_page.upload_image()

    property_page.fill_details()

    property_page.fill_description()

    # Skip Price

    # Submit
    property_page.submit()

    # Validation
    validation = page.locator(
        "text=Price is required"
    )

    validation.wait_for(
        state="visible",
        timeout=10000
    )

    assert validation.is_visible()

    print(
        "Price Validation Passed"
    )

    page.screenshot(
        path="Playwright Habitake/screenshots/property_without_price.png",
        full_page=True
    )