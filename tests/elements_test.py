import random
import time

import allure

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonsPage, LinksPage, \
    UploadAndDownloadFilePage, DynamicPropertiesPage


@allure.suite('Elements')
class TestElements:

    @allure.feature('TextBox')
    class TestTextBox:

        @allure.title('Check TextBox')
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            created_full_name, created_email, created_cur_addr, created_perm_addr = text_box_page.check_filled_form()
            assert full_name == created_full_name, "The full name does not match"
            assert email == created_email, "The email does not match"
            assert current_address == created_cur_addr, "The current address does not match"
            assert permanent_address == created_perm_addr, "The permanent address does not match"

    @allure.feature('CheckBox')
    class TestCheckBox:

        @allure.title('Check CheckBox')
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkbox = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_output_result()
            print(input_checkbox)
            print(output_result)
            # time.sleep(5)

    @allure.feature('RadioButton')
    class TestRadioButton:

        @allure.title('Check RadioButton')
        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            radio_button_page.open()
            radio_button_page.click_on_the_radio_button('yes')
            yes_result = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button('impressive')
            impressive_result = radio_button_page.get_output_result()
            assert yes_result == 'Yes', "'Yes' have not be selected"
            assert impressive_result == 'Impressive', "'Impressive' have not be selected"

    @allure.feature('WebTable')
    class TestWebTable:

        @allure.title('Check WebTableAddPerson')
        def test_web_table_add_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            new_person = web_table_page.add_new_person()
            table_result = web_table_page.check_new_added_person()
            assert new_person in table_result, 'the new person was not found in the table'

        @allure.title('Check WebTableSearchPerson')
        def test_web_table_search_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            key_word = web_table_page.add_new_person()[random.randint(0, 5)]
            web_table_page.search_some_person(key_word)
            table_result = web_table_page.check_search_person()
            assert key_word in table_result, 'the person was not found in the table'

        @allure.title('Check WebTableUpdatePersonInfo')
        def test_web_table_update_person_info(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            lastname = web_table_page.add_new_person()[1]
            web_table_page.search_some_person(lastname)
            age = web_table_page.update_person_info()
            row = web_table_page.check_search_person()
            assert age in row, 'the person card has not been changed'

        @allure.title('Check WebTableDeletePerson')
        def test_web_table_delete_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            email = web_table_page.add_new_person()[3]
            web_table_page.search_some_person(email)
            web_table_page.delete_person()
            text = web_table_page.check_deleted()
            assert text == 'No rows found', 'the person has not been deleted'

        @allure.title('Check WebTableChangeCountRow')
        def test_web_table_change_count_row(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            count = web_table_page.select_up_to_some_rows()
            assert count == [5, 10, 20], 'the number of rows in the table has not been changed'

    @allure.feature('ButtonsPage')
    class TestButtonsPage:

        @allure.title('Check DifferentClickOnTheButton')
        def test_different_click_on_the_button(self, driver):
            button_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
            button_page.open()
            double = button_page.click_on_different_button('double')
            right = button_page.click_on_different_button('right')
            click = button_page.click_on_different_button('click')
            assert double == 'You have done a double click', 'The double click button was not pressed'
            assert right == 'You have done a right click', 'The right click button was not pressed'
            assert click == 'You have done a dynamic click', 'The dynamic click button was not pressed'

    @allure.feature('LinksPage')
    class TestLinksPage:

        @allure.title('Check Link')
        def test_check_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            href_link, current_link = links_page.check_new_tab_simple_link()
            assert href_link == current_link, 'The link is broken or url is incorrect'

        @allure.title('Check BrokenLink')
        def test_broken_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            response_code = links_page.check_broken_link('https://demoqa.com/bad-request')
            assert response_code == 400, 'The link works or the status code in zone 400'

    @allure.feature('UploadAndDownloadFile')
    class TestUploadAndDownloadFile:

        @allure.title('Check UploadFile')
        def test_upload_file(self, driver):
            upload_and_download_file_page = UploadAndDownloadFilePage(driver, 'https://demoqa.com/upload-download')
            upload_and_download_file_page.open()
            file_name, result = upload_and_download_file_page.upload_file()
            assert file_name == result, 'the file has not been uploaded'

        @allure.title('Check DownloadFile')
        def test_download_file(self, driver):
            upload_and_download_file_page = UploadAndDownloadFilePage(driver, 'https://demoqa.com/upload-download')
            upload_and_download_file_page.open()
            check = upload_and_download_file_page.download_file()
            assert check is True, 'the file has not been downloaded'

    @allure.feature('DynamicProperties')
    class TestDynamicPropertiesPage:

        @allure.title('Check EnableButton')
        def test_enable_button(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
            dynamic_properties_page.open()
            enable = dynamic_properties_page.check_enable_button()
            assert enable is True, 'button did not enabled after 5 seconds'

        @allure.title('Check DynamicProperties')
        def test_dynamic_properties(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
            dynamic_properties_page.open()
            color_button_before, color_button_after = dynamic_properties_page.check_changet_of_color()
            assert color_button_before != color_button_after, 'colors have not been changed'

        @allure.title('Check AppearButton')
        def test_appear_button(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
            dynamic_properties_page.open()
            appear = dynamic_properties_page.check_appear_button()
            assert appear is True, 'button did not appear after 5 seconds'
