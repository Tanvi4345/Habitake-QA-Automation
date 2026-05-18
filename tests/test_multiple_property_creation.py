from pages.login_page import LoginPage

from pages.home_page import HomePage

from pages.add_property_page import AddPropertyPage

from utils.config import BASE_URL, EMAIL, PASSWORD


def test_multiple_property_creation(page):

    login = LoginPage(page)

    home = HomePage(page)

    property_page = AddPropertyPage(page)

    # Login
    login.open_login(BASE_URL)

    login.login(EMAIL, PASSWORD)

    # Create 2 Properties
    for i in range(2):

        print(
            f"Creating Property {i+1}"
        )

        home.open_add_property()

        property_page.select_property_type()

        property_page.fill_location()

        property_page.upload_image()

        property_page.fill_details()

        property_page.fill_description()

        property_page.set_price()

        property_page.submit()

        home.handle_success_popup()

    print(
        "Multiple Property Test Passed"
    )

    page.screenshot(
        path="Playwright Habitake/screenshots/multiple_property.png",
        full_page=True
    )