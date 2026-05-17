from pages.login_page import LoginPage

from pages.home_page import HomePage

from pages.add_property_page import AddPropertyPage

from pages.logout_page import LogoutPage

from utils.config import BASE_URL, EMAIL, PASSWORD


def test_add_property(page):

    login = LoginPage(page)

    home = HomePage(page)

    property_page = AddPropertyPage(page)

    logout_page = LogoutPage(page)

    # ====================================
    # LOGIN
    # ====================================

    login.open_login(BASE_URL)

    login.login(EMAIL, PASSWORD)

    # ====================================
    # HOME PAGE
    # ====================================

    home.verify_home_page()

    # ====================================
    # OPEN ADD PROPERTY
    # ====================================

    home.open_add_property()

    # ====================================
    # FILL PROPERTY
    # ====================================

    property_page.select_property_type()

    property_page.fill_location()

    property_page.upload_image()

    property_page.fill_details()

    property_page.fill_description()

    property_page.set_price()

    # ====================================
    # SUBMIT PROPERTY
    # ====================================

    property_page.submit()

    # ====================================
    # SUCCESS POPUP
    # ====================================

    home.handle_success_popup()

    # ====================================
    # LOGOUT FLOW
    # ====================================

    home.open_profile_dropdown()

    logout_page.logout()

    print(
        "Complete Flow Passed"
    )
