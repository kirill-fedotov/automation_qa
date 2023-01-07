import time

import allure

from pages.widgets_page import AccordianPage, AutoCompletePage, DatePickerPage, SliderPage, ProgressBarPage, TabsPage, \
    ToolTipsPage, MenuPage


@allure.suite('Widgets')
class TestWidgets:

    @allure.feature('Accordian')
    class TestAccordianPage:

        @allure.title('Check Accordian')
        def test_accordian(self, driver):
            accordian_page = AccordianPage(driver, 'https://demoqa.com/accordian')
            accordian_page.open()
            first_title, first_content, second_title, second_content, third_title, third_content \
                = accordian_page.check_accordian2()
            assert first_title == 'What is Lorem Ipsum?' and first_content > 0, 'Incorrect title or missing text'
            assert second_title == 'Where does it come from?' and second_content > 0, 'Incorrect title or missing text'
            assert third_title == 'Why do we use it?' and third_content > 0, 'Incorrect title or missing text'

    @allure.feature('Auto Complete')
    class TestAutoCompletePage:

        @allure.title('Check Fill Multi Autocomplete')
        def test_fill_multi_autocomplete(self, driver):
            autocomplete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            colors = autocomplete_page.fill_input_multi()
            colors_result = autocomplete_page.check_color_in_multi()
            assert colors == colors_result, 'The added colors are missing in the input'

        @allure.title('Check Remove Value From Multi')
        def test_remove_value_from_multi(self, driver):
            autocomplete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            autocomplete_page.fill_input_multi()
            count_value_before, count_value_after = autocomplete_page.remove_value_from_multi()
            assert count_value_before != count_value_after, 'Value was not deleted'

        @allure.title('Check Fill Single Autocomplete')
        def test_fill_single_autocomplete(self, driver):
            autocomplete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            color = autocomplete_page.fill_input_single()
            color_result = autocomplete_page.check_color_in_single()
            assert color in color_result, 'The added color are missing in the input'

    @allure.feature('Date Picker')
    class TestDatePickerPage:

        @allure.title('Check Change Date')
        def test_change_date(self, driver):
            date_picker_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            date_picker_page.open()
            value_date_before, value_date_after = date_picker_page.select_date()
            assert value_date_before != value_date_after, 'The date has not been changed'

        @allure.title('Check Change Date And Time')
        def test_change_date_and_time(self, driver):
            date_picker_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            date_picker_page.open()
            value_date_before, value_date_after = date_picker_page.select_date_and_time()
            assert value_date_before != value_date_after, 'The date and time have not been changed'

    @allure.feature('Slider')
    class TestSliderPage:

        @allure.title('Check Slider')
        def test_slider(self, driver):
            slider = SliderPage(driver, 'https://demoqa.com/slider')
            slider.open()
            value_before, value_after = slider.change_slider_value()
            assert value_before != value_after, 'The slider value has not been changed'

    @allure.feature('Progress Bar')
    class TestProgressBarPage:

        @allure.title('Check Progress Bar')
        def test_progress_bar(self, driver):
            progress_bar = ProgressBarPage(driver, 'https://demoqa.com/progress-bar')
            progress_bar.open()
            value_before, value_after = progress_bar.change_progress_bar_value()
            assert value_before != value_after, 'The progress bar value has not been changed'

    @allure.feature('Tabs')
    class TestTabsPage:

        @allure.title('Check Tabs')
        def test_tabs(self, driver):
            tabs = TabsPage(driver, 'https://demoqa.com/tabs')
            tabs.open()
            what_button, what_content, origin_button, origin_content, use_button, use_content = tabs.check_tabs()
            assert what_button == 'What' and what_content > 1, 'The tab "What" was not pressed or the text is missing'
            assert origin_button == 'Origin' and origin_content > 1, 'The tab "Origin" was not pressed or the text is missing'
            assert use_button == 'Use' and use_content > 1, 'The tab "Use" was not pressed or the text is missing'

    @allure.feature('Tool Tips')
    class TestToolTipsPage:

        @allure.title('Check Tool Tips')
        def test_tool_tips(self, driver):
            tool_tips_page = ToolTipsPage(driver, 'https://demoqa.com/tool-tips')
            tool_tips_page.open()
            tool_tip_text_button, tool_tip_text_field, tool_tip_text_contrary, tool_tip_text_section = \
                tool_tips_page.check_tool_tips()
            assert tool_tip_text_button == 'You hovered over the Button', 'Hover missing or incorrect content'
            assert tool_tip_text_field == 'You hovered over the field', 'Hover missing or incorrect content'
            assert tool_tip_text_contrary == 'You hovered over the Contrary', 'Hover missing or incorrect content'
            assert tool_tip_text_section == 'You hovered over the 1.10.32', 'Hover missing or incorrect content'

    @allure.feature('Menu')
    class TestMenuPage:

        @allure.title('Check Menu')
        def test_menu_items(self, driver):
            menu_page = MenuPage(driver, 'https://demoqa.com/menu')
            menu_page.open()
            data = menu_page.check_menu()
            assert data == ['Main Item 1', 'Main Item 2', 'Sub Item', 'Sub Item', 'SUB SUB LIST »', 'Sub Sub Item 1',
                            'Sub Sub Item 2', 'Main Item 3'], 'Menu items do not exist or are not selected'
