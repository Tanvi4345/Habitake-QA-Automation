from pages.login_page import LoginPage

from pages.home_page import HomePage

from pages.add_property_page import AddPropertyPage

from utils.config import BASE_URL, EMAIL, PASSWORD

import random


def test_property_type_selection(page):

    login = LoginPage(page)

    home = HomePage(page)

    property_page = AddPropertyPage(page)

    # ====================================
    # LOGIN
    # ====================================

    login.open_login(BASE_URL)

    login.login(EMAIL, PASSWORD)

    print(
        "Login Successful"
    )

    # ====================================
    # OPEN ADD PROPERTY PAGE
    # ====================================

    home.open_add_property()

    print(
        "Add Property Page Opened"
    )

    # ====================================
    # RANDOM PROPERTY TYPE
    # ====================================

    property_types = [

        "Residential",

        "Commercial",

        "Luxury",

        "Rental"

    ]

    selected_property = random.choice(
        property_types
    )

    print(
        f"Selected Property Type: {selected_property}"
    )

    # ====================================
    # CATEGORY
    # ====================================

    page.locator(
        "text=Sell Property"
    ).click()

    # ====================================
    # RANDOM PROPERTY CLICK
    # ====================================

    page.locator(
        f"text={selected_property}"
    ).first.click()

    print(
        "Random Property Type Selected"
    )

    # ====================================
    # PROPERTY CONDITION
    # ====================================

    page.locator(
        "text=Secondary market"
    ).click()

    # ====================================
    # SEO OPTION
    # ====================================

    page.locator(
        "text=Public"
    ).click()

    # ====================================
    # FILL LOCATION
    # ====================================

    property_page.fill_location()

    # ====================================
    # UPLOAD IMAGE
    # ====================================

    property_page.upload_image()

    # ====================================
    # PROPERTY DETAILS
    # ====================================

    property_page.fill_details()

    # ====================================
    # DESCRIPTION
    # ====================================

    property_page.fill_description()

    # ====================================
    # PRICE
    # ====================================

    property_page.set_price()

    # ====================================
    # SUBMIT PROPERTY
    # ====================================

    property_page.submit()

    print(
        "Create Button Clicked"
    )

    # ====================================
    # SUCCESS MESSAGE
    # ====================================

    page.wait_for_timeout(5000)

    assert "property-listing" in page.url

    print(
        "Property Created Successfully"
    )

    # assert success.is_visible()

    print(
        "Property Created Successfully"
    )

    # ====================================
    # SCREENSHOT
    # ====================================

    page.screenshot(
        path="random_property_created.png",
        full_page=True
    )

    print(
        "Screenshot Captured"
    )

    page.wait_for_timeout(3000)