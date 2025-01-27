from selenium.webdriver.common.by import By


class AccordianPageLocators:

	SECTION1 = (By.CSS_SELECTOR, "div[id='section1Heading']")
	SECTION1_CONTENT = (By.CSS_SELECTOR, "div[id='section1Content'] p")
	SECTION2 = (By.CSS_SELECTOR, "div[id='section2Heading']")
	SECTION2_CONTENT = (By.CSS_SELECTOR, "div[id='section2Heading']")
	SECTION3 = (By.CSS_SELECTOR, "div[id='section3Heading']")
	SECTION3_CONTENT = (By.CSS_SELECTOR, "div[id='section3Heading']")

class AutoCompletePageLocators:

	MULTI_INPUT = (By.CSS_SELECTOR, "input[id='autoCompleteMultipleInput']")
	MULTI_VALUE = (By.CSS_SELECTOR, "div[class='css-12jo7m5 auto-complete__multi-value__label']")
	MULTI_VALUE_DELETE = (By.CSS_SELECTOR, "div[class='css-xb97g8 auto-complete__multi-value__remove'] ")
	SINGLE_INPUT = (By.CSS_SELECTOR, "input[id='autoCompleteSingleInput']")
	SINGLE_VALUE = (By.CSS_SELECTOR, "div[class='auto-complete__single-value css-1uccc91-singleValue']")

class DatePickerPageLocators:

	INPUT_DATE = (By.CSS_SELECTOR, "input[id='datePickerMonthYearInput']")
	SELECT_MONTH = (By.CSS_SELECTOR, "select[class='react-datepicker__month-select']")
	SELECT_YEAR = (By.CSS_SELECTOR, "select[class='react-datepicker__year-select']")
	SELECT_DAY = (By.CSS_SELECTOR, "div[class^='react-datepicker__day react-datepicker__day']")

	INPUT_DATE_AND_TIME = (By.CSS_SELECTOR, "input[id='dateAndTimePickerInput']")
	DATE_AND_TIME_MONTH = (By.CSS_SELECTOR, "div[class='react-datepicker__month-read-view']")
	DATE_AND_TIME_YEAR = (By.CSS_SELECTOR, "div[class='react-datepicker__year-read-view']")
	DATE_AND_TIME_DAY = (By.CSS_SELECTOR, "div[class^='react-datepicker__day react-datepicker__day']")
	DATE_AND_TIME_TIME_LIST = (By.CSS_SELECTOR, "li[class='react-datepicker__time-list-item ']")
	DATE_AND_TIME_MONTH_LIST = (By.CSS_SELECTOR, "div[class='react-datepicker__month-option']")
	DATE_AND_TIME_YEAR_LIST = (By.CSS_SELECTOR, "div[class='react-datepicker__year-option']")

class SliderPageLocators:

	INPUT_SLIDER = (By.CSS_SELECTOR, "input[class='range-slider range-slider--primary']")
	SLIDER_VALUE = (By.CSS_SELECTOR, "input[id='sliderValue']")

class ProgressBarPageLocators:

	PROGRESS_BAR_BUTTON = (By.CSS_SELECTOR, "button[id='startStopButton']")
	PROGRESS_BAR_VALUE = (By.CSS_SELECTOR, "div[class='progress-bar bg-info']")

class ToolTipsPageLocators:

	HOVER_ME_TO_SEE_BUTTON = (By.CSS_SELECTOR, "button[id='toolTipButton']")
	TOOL_TIP_BUTTON = (By.CSS_SELECTOR, "button[aria-describedby='buttonToolTip']")
	INPUT_HOVER_ME_TO_SEE = (By.CSS_SELECTOR, "input[id='toolTipTextField']")
	TOOL_TIP_INPUT = (By.CSS_SELECTOR, "input[aria-describedby='textFieldToolTip']")
	CONTRARY = (By.XPATH, "//div[@id='texToolTopContainer']//a[(text()='Contrary')]")
	TOOL_TIP_CONTRARY = (By.CSS_SELECTOR, "a[aria-describedby='contraryTexToolTip']")
	SECTION = (By.XPATH, "//*[.='1.10.32']")
	TOOL_TIP_SECTION = (By.CSS_SELECTOR, "a[aria-describedby='sectionToolTip']")
	TOOL_TIPS_INNERS = (By.CSS_SELECTOR, "div[class='tooltip-inner']")
