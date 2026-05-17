import pytest


@pytest.fixture
def logged_in_page(browser):

    context = browser.new_context()

    context.grant_permissions(
        ["geolocation"]
    )

    context.set_geolocation({
        "latitude": 18.5204,
        "longitude": 73.8567
    })

    page = context.new_page()

    yield page

    context.close()