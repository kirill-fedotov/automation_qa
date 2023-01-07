import random

from selenium.webdriver.common.by import By


class AccordianPageLocators:
    SECTION_FIRST = (By.XPATH, "//div[@id='section1Heading']")
    SECTION_CONTENT_FIRST = (By.XPATH, "//div[@id='section1Content']")
    SECTION_SECOND = (By.XPATH, "//div[@id='section2Heading']")
    SECTION_CONTENT_SECOND = (By.XPATH, "//div[@id='section2Content']")
    SECTION_THIRD = (By.XPATH, "//div[@id='section3Heading']")
    SECTION_CONTENT_THIRD = (By.XPATH, "//div[@id='section3Content']")


class AutoCompletePageLocators:
    MULTI_INPUT = (By.XPATH, "//input[@id='autoCompleteMultipleInput']")
    MULTI_VALUE = (By.XPATH, "//div[@class='css-1rhbuit-multiValue auto-complete__multi-value']")
    MULTI_VALUE_REMOVE = (By.XPATH, "//div[@class='css-xb97g8 auto-complete__multi-value__remove']")
    SINGLE_CONTAINER = (By.XPATH, "//div[@id='autoCompleteSingleContainer']")
    SINGLE_INPUT = (By.XPATH, "//input[@id='autoCompleteSingleInput']")


class DatePickerPageLocators:
    DATE_INPUT = (By.XPATH, "//input[@id='datePickerMonthYearInput']")
    DATE_SELECT_MONTH = (By.XPATH, "//select[@class='react-datepicker__month-select']")
    DATE_SELECT_YEAR = (By.XPATH, "//select[@class='react-datepicker__year-select']")
    DATE_SELECT_DAY_LIST = (By.XPATH, f"//div[@class='react-datepicker__day react-datepicker__day--00{random.randint(2, 5)}']")

    DATE_AND_TIME_INPUT = (By.XPATH, "//input[@id='dateAndTimePickerInput']")
    DATE_AND_TIME_MONTH = (By.XPATH, "//div[@class='react-datepicker__month-read-view']")
    DATE_AND_TIME_YEAR = (By.XPATH, "//div[@class='react-datepicker__year-read-view']")
    DATE_AND_TIME_TIME_LIST = (By.XPATH, "//li[@class='react-datepicker__time-list-item ']")
    DATE_AND_TIME_MONTH_LIST = (By.XPATH, "//div[@class='react-datepicker__month-option']")
    DATE_AND_TIME_YEAR_LIST = (By.XPATH, "//div[@class='react-datepicker__year-option']")


class SliderPageLocators:
    INPUT_SLIDER = (By.XPATH, "//input[@class='range-slider range-slider--primary']")
    SLIDER_VALUE = (By.XPATH, "//input[@id='sliderValue']")


class ProgressBarPageLocators:
    PROGRESS_BAR_BUTTON = (By.XPATH, "//button[@id='startStopButton']")
    PROGRESS_BAR_VALUE = (By.XPATH, "//div[@class='progress-bar bg-info']")


class TabsPageLocators:
    TABS_WHAT = (By.XPATH, "//a[@id='demo-tab-what']")
    TABS_WHAT_CONTENT = (By.XPATH, "//div[@id='demo-tabpane-what']")
    TABS_ORIGIN = (By.XPATH, "//a[@id='demo-tab-origin']")
    TABS_ORIGIN_CONTENT = (By.XPATH, "//div[@id='demo-tabpane-origin']")
    TABS_USE = (By.XPATH, "//a[@id='demo-tab-use']")
    TABS_USE_CONTENT = (By.XPATH, "//div[@id='demo-tabpane-use']")


class ToolTipsPageLocators:
    BUTTON = (By.XPATH, "//button[@id='toolTipButton']")
    TOOL_TIP_BUTTON = (By.XPATH, "//button[@aria-describedby='buttonToolTip']")

    #FIELD = (By.CSS_SELECTOR, "div[id='buttonToolTopContainer'] input[id='toolTipTextField']")
    FIELD = (By.CSS_SELECTOR, "input[id='toolTipTextField']")
    TOOL_TIP_FIELD = (By.XPATH, "//input[@aria-describedby='textFieldToolTip']")

    CONTRARY_LINK = (By.XPATH, "//*[.='Contrary']")
    TOOL_TIP_CONTRARY = (By.XPATH, "//a[@aria-describedby='contraryTexToolTip']")

    SECTION_LINK = (By.XPATH, "//*[.='1.10.32']")
    TOOL_TIP_SECTION = (By.XPATH, "//a[@aria-describedby='sectionToolTip']")

    TOOL_TIP_INNERS = (By.XPATH, "//div[@class='tooltip-inner']")


class MenuPageLocators:
    MENU_ITEM_LIST = (By.CSS_SELECTOR, "ul[id='nav'] li a")

