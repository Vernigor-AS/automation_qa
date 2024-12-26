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