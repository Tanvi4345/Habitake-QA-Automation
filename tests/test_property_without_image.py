from pages.login_page import LoginPage

from pages.home_page import HomePage

from pages.add_property_page import AddPropertyPage

from utils.config import BASE_URL, EMAIL, PASSWORD


def test_property_without_image(page):

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
    # FILL PROPERTY DETAILS
    # ====================================

    property_page.select_property_type()

    property_page.fill_location()

    property_page.fill_details()

    property_page.fill_description()

    property_page.set_price()

    print(
        "Property Details Filled"
    )

    # ====================================
    # SUBMIT PROPERTY
    # ====================================

    property_page.submit()

    print(
        "Create Button Clicked"
    )

    # ====================================
    # IMAGE VALIDATION
    # ====================================

    error = page.locator(
        "text=At least one photo is required."
    )

    # Scroll to validation section
    error.scroll_into_view_if_needed()

    # Wait for validation message
    error.wait_for(
        state="visible",
        timeout=10000
    )

    # Assertion
    assert error.is_visible()

    print(
        "Image Validation Passed"
    )

    # ====================================
    # SCREENSHOT
    # ====================================

    page.screenshot(
        path="property_without_image.png",
        full_page=True
    )

    print(
        "Screenshot Captured"
    )

    # ====================================
    # HOLD SCREEN
    # ====================================

    page.wait_for_timeout(5000)