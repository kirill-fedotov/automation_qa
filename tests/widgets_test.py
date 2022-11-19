from pages.base_page import BasePage
from pages.widgets_page import AccordianPage


class TestWidgets:
    class TestAccordianPage:

        def test_accordian(self, driver):
            accordian_page = AccordianPage(driver, 'https://demoqa.com/accordian')
            accordian_page.open()
            first_content, second_content, third_content = accordian_page.check_accordian2()
            assert first_content == 574
            assert second_content == 763
            assert third_content == 613

