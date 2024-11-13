import random
import time

from selenium.webdriver.common.by import By
from generator.generator import generated_person, generated_person_webtable_page
from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonPageLocators, \
	WebTablePageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
	locators = TextBoxPageLocators()

	def fill_in_all_fields(self):
		person_info = next(generated_person())
		full_name = person_info.full_name
		email = person_info.email
		current_address = person_info.current_address
		permanent_address = person_info.permanent_address
		self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
		self.element_is_visible(self.locators.EMAIL).send_keys(email)
		self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
		self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
		self.element_is_visible(self.locators.SUBMIT).click()
		return full_name, email, current_address, permanent_address

	def check_text(self):
		full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(':')[1]
		email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(':')[1]
		current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
		permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
		return full_name, email, current_address, permanent_address


class CheckBoxPage(BasePage):
	locators = CheckBoxPageLocators()

	def open_full_list(self):
		self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()

	def click_random_checkbox(self):
		item_list = self.element_are_visible(self.locators.ITEM_LIST)
		count = 17
		while count != 0:
			item = item_list[random.randint(0, 16)]
			if count > 0:
				self.go_to_element(item)
				item.click()
				count -= 1
			else:
				break

	def get_checked_checkboxes(self):
		checked_list = self.element_are_present(self.locators.CHECKED_ITEMS)
		data = []
		for box in checked_list:
			title_item = box.find_element(By.XPATH, self.locators.TITLE_ITEM)
			print("Found title:", title_item.text)
			data.append(title_item.text)
		return (str(data).replace(' ', '').replace('doc', '')
				.replace('.', '').lower())

	def get_output_result(self):
		result_list = self.element_are_present(self.locators.OUTPUT_RESULT)
		data = []
		for item in result_list:
			data.append(item.text)
		return str(data).lower().replace(' ', '')


class RadioButtonPage(BasePage):
	locators = RadioButtonPageLocators()

	def click_on_the_radio_button(self, choice):
		choices = {'yes': self.locators.RADIO_BUTTON_YES,
				  'impressive': self.locators.RADIO_BUTTON_IMPRESSIVE,
		           'no': self.locators.RADIO_BUTTON_NO}

		self.element_is_visible(choices[choice]).click()

	def get_output_result(self):
		return self.element_is_present(self.locators.OUTPUT_RESULT).text

class WebTablePage(BasePage):
	locators = WebTablePageLocators()

	def add_button(self):
		self.element_is_visible(self.locators.ADD_BUTTON).click()

	def fill_all_fields_on_web_table_page(self):
		person_info = next(generated_person_webtable_page())
		first_name = person_info.first_name
		last_name = person_info.last_name
		email = person_info.email
		age = person_info.age
		salary = person_info.salary
		department = person_info.department
		self.element_is_visible(self.locators.FIRSTNAME_INPUT).send_keys(first_name)
		self.element_is_visible(self.locators.LASTNAME_INPUT).send_keys(last_name)
		self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(email)
		self.element_is_visible(self.locators.AGE_INPUT).send_keys(str(age))
		self.element_is_visible(self.locators.SALARY_INPUT).send_keys(str(salary))
		self.element_is_visible(self.locators.DEPARTMENT_INPUT).send_keys(department)
		time.sleep(1)
		self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
		return first_name, last_name, email, age, salary, department
