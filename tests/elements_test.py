from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from pages.elements_page import TextBoxPage


class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            created_full_name, created_email, created_cur_addr, created_perm_addr = text_box_page.check_filled_form()
            assert full_name == created_full_name, "The full name does not match"
            assert email == created_email, "The email does not match"
            assert current_address == created_cur_addr, "The current address does not match"
            assert permanent_address == created_perm_addr, "The permanent address does not match"




