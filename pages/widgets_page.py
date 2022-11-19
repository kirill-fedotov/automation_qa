from selenium.common import TimeoutException

from locators.widgets_page_locators import AccordianPageLocators
from pages.base_page import BasePage


class AccordianPage(BasePage):
    locators = AccordianPageLocators()

    def check_accordian(self, accordian_num):
        accordian = {'first':
            {  # 'title': self.locators.SECTION_FIRST,
                'content': self.locators.SECTION_CONTENT_FIRST},
            'second':
                {'title': self.locators.SECTION_SECOND,
                 'content': self.locators.SECTION_CONTENT_SECOND},
            'third':
                {'title': self.locators.SECTION_THIRD,
                 'content': self.locators.SECTION_CONTENT_THIRD}
        }
        section_title = self.element_is_visible(accordian[accordian_num]['title'])
        section_title.click()
        self.scroll_down()
        try:
            section_content = self.element_is_visible(accordian[accordian_num]['content']).text
        except TimeoutException:
            section_title.click()
            section_content = self.element_is_visible(accordian[accordian_num]['content']).text
        return [section_title.text, len(section_content)]

    def check_accordian2(self):
        first_content = self.element_is_visible(self.locators.SECTION_CONTENT_FIRST).text
        self.scroll_to(500)
        self.element_is_visible(self.locators.SECTION_SECOND).click()
        second_content = self.element_is_visible(self.locators.SECTION_CONTENT_SECOND).text
        self.element_is_visible(self.locators.SECTION_THIRD).click()
        third_content = self.element_is_visible(self.locators.SECTION_CONTENT_THIRD).text
        return len(first_content), len(second_content), len(third_content)
