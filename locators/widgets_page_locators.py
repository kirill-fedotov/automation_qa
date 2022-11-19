from selenium.webdriver.common.by import By


class AccordianPageLocators:
    SECTION_FIRST = (By.XPATH, "//div[@id='section1Heading']")
    SECTION_CONTENT_FIRST = (By.XPATH, "//div[@id='section1Content']")
    SECTION_SECOND = (By.XPATH, "//div[@id='section2Heading']")
    SECTION_CONTENT_SECOND = (By.XPATH, "//div[@id='section2Content']")
    SECTION_THIRD = (By.XPATH, "//div[@id='section3Heading']")
    SECTION_CONTENT_THIRD = (By.XPATH, "//div[@id='section3Content']")