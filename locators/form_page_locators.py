import random

from selenium.webdriver.common.by import By


class FormPageLocators:
	FIRST_NAME = (By.CSS_SELECTOR, "#firstName")
	LAST_NAME = (By.CSS_SELECTOR, "#lastName")
	EMAIL = (By.CSS_SELECTOR, "#userEmail")
	GENDER = (By.CSS_SELECTOR, f"div[class*='custom-control'] label[for='gender-radio-{random.randint(1, 3)}']")
	MOBILE = (By.CSS_SELECTOR, "#userNumber")
	DATE_OF_BIRTH = (By.CSS_SELECTOR, "#dateOfBirthInput")
	SUBJECTS = (By.CSS_SELECTOR, "#subjectsInput")
	HOBBIES = (By.CSS_SELECTOR, f"div[id*='hobbies'] label[for='hobbies-checkbox-{random.randint(1, 3)}']")
	FILE_INPUT = (By.CSS_SELECTOR, "#uploadPicture")
	CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='currentAddress']")
	SELECT_STATE = (By.CSS_SELECTOR, "#state")
	STATE_INPUT = (By.CSS_SELECTOR, "#react-select-3-input")
	SELECT_CITY = (By.CSS_SELECTOR, "#city")
	CITY_INPUT = (By.CSS_SELECTOR, "#react-select-4-input")
	SUBMIT = (By.CSS_SELECTOR, "#submit")

	#table results
	RESULT_TABLE = ("xpath", "//div[@class='table-responsive']//td[2]")