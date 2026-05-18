from pages.base_page import BasePage

import random
import os


class AddPropertyPage(BasePage):

    def __init__(self, page):

        super().__init__(page)

        self.create_btn = "button:has-text('Create')"

    # ====================================
    # PROPERTY TYPE
    # ====================================

    def select_property_type(self):

        self.page.locator("text=Sell Property").click()

        self.page.locator("text=Residential").click()

        self.page.locator("text=Secondary market").click()

        self.page.locator("text=Public").click()

        print("Property Type Selected")

    # ====================================
    # LOCATION
    # ====================================

    def fill_location(self):

        # self.page.keyboard.press(
        #     "Escape"
        # )

        # Country
        self.page.locator("(//div[@class='relative'])[3]").first.click()

        inputs = self.page.locator("input[placeholder='Enter here']")

        # Address
        inputs.nth(0).fill(f"Pune Property {random.randint(100,999)}")

        print("Address Filled")

        self.page.wait_for_timeout(2000)

        # Country Dropdown
        # ====================================

        # Open Country Dropdown
        self.page.locator("text=Select").first.click()

        self.page.wait_for_timeout(3000)

        # Search Field
        search_inputs = self.page.locator("input[placeholder='Search...']")

        # Type India
        search_inputs.nth(0).fill("India")

        print("India Typed")

        self.page.wait_for_timeout(2000)

        # Select India
        self.page.locator("(//div[@class='relative']//li)[3]").first.click()

        print("Country Selected Successfully")

        self.page.wait_for_timeout(3000)

        # # State Dropdown
        # self.page.locator(
        #     "text=Select"
        # ).first.click()

        # inputs = self.page.locator(
        #     "input[placeholder='Search...']"
        # )

        # # State
        # inputs.nth(0).fill(
        #     f"Maharashtra"
        # )

        # self.page.locator("(//div[@class='relative']//li)[4]").first.click()

        # self.page.wait_for_timeout(3000)

        # self.page.keyboard.press(
        #     "ArrowDown"
        # )

        # self.page.wait_for_timeout(1000)

        # self.page.keyboard.press(
        #     "ArrowDown"
        # )

        # self.page.wait_for_timeout(1000)

        # self.page.keyboard.press(
        #     "Enter"
        # )

        # # City Dropdown
        # self.page.locator(
        #     "text=Select"
        # ).first.click()

        # inputs = self.page.locator(
        #     "input[placeholder='Search...']"
        # )

        # # City
        # inputs.nth(0).fill(
        #     f"Pune"
        # )

        # self.page.locator("(//div[@class='relative']//li)[1]").first.click()

        # self.page.wait_for_timeout(3000)

        # self.page.keyboard.press(
        #     "ArrowDown"
        # )

        # self.page.wait_for_timeout(1000)

        # self.page.keyboard.press(
        #     "ArrowDown"
        # )

        # self.page.wait_for_timeout(1000)

        # self.page.keyboard.press(
        #     "Enter"
        # )

        zip_inputs = self.page.locator("input[placeholder='Enter here']")

        zip_inputs.nth(1).fill(str(random.randint(400000, 499999)))

        print("Zip Code Filled")

    # ====================================
    # IMAGE UPLOAD
    # ====================================

    def upload_image(self):

        file_path = os.path.abspath("Playwright Habitake/test_data/test_image2.jpg")

        self.page.set_input_files("input[type='file']", file_path)

        self.page.wait_for_timeout(5000)

        print("Image Uploaded")

        # Open image preview
        self.page.locator("img").first.click()

        self.page.wait_for_timeout(3000)

        # Image Label
        self.page.locator("input[placeholder='Enter label']").fill(
            f"Property {random.randint(1000,9999)}"
        )

        print("Image Label Added")

    # ====================================
    # DETAILS
    # ====================================

    def fill_details(self):

        inputs = self.page.locator("input[placeholder='Enter here']")

        inputs.nth(2).fill(f"Automation Property {random.randint(100,999)}")

        inputs.nth(3).fill(str(random.randint(1000, 5000)))

        inputs.nth(4).fill(str(random.randint(1, 10)))

        self.page.wait_for_timeout(2000)

        # Bedrooms
        self.page.get_by_role("button", name="3").nth(0).click(force=True)

        print("Bedrooms selected")

        # Bathrooms
        self.page.get_by_role("button", name="2").nth(0).click(force=True)

        print("Bathrooms selected")

        # Parking
        self.page.get_by_role("button", name="1").nth(0).click(force=True)

        print("Parking selected")

        # Amenities
        self.page.locator("text=TV set").first.click(force=True)

        self.page.locator("text=Air conditioning").first.click(force=True)

        print("Amenities selected")

    # ====================================
    # DESCRIPTION
    # ====================================

    def fill_description(self):

        self.page.locator("textarea").fill(
            f"Automation Description {random.randint(1000,9999)}"
        )

        print("Description Added")

    # ====================================
    # PRICE
    # ====================================

    def set_price(self):

        self.page.locator("input[placeholder='Enter price']").fill(
            str(random.randint(10000, 90000))
        )

        print("Price Added")

    # ====================================
    # SUBMIT
    # ====================================

    def submit(self):

        self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")

        self.page.wait_for_timeout(3000)

        self.page.locator(self.create_btn).first.click(force=True)

        print("Create Button Clicked")

        self.page.wait_for_timeout(5000)

        # Success Message
        success = self.page.locator("text=Property processed successfully")

        if success.count() > 0:

            print("Success Message Displayed")

        self.page.screenshot(path="Playwright Habitake/screenshots/property_submit.png", full_page=True)

        print("Property Submitted Successfully")
