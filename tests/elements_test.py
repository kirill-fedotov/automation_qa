import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage


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

    class TestCheckBox:
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkbox = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_output_result()
            print(input_checkbox)
            print(output_result)
            #time.sleep(5)

    class TestRadioButton:
        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            radio_button_page.open()
            radio_button_page.click_on_the_radio_button('yes')
            yes_result = radio_button_page.get_otput_result()
            radio_button_page.click_on_the_radio_button('impressive')
            impressive_result = radio_button_page.get_otput_result()
            assert yes_result == 'Yes', "'Yes' have not be selected"
            assert impressive_result == 'Impressive', "'Impressive' have not be selected"

