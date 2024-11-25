import random

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

	def web_table_add_new_person(self):
		count =1
		while count !=0:
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
			self.element_is_visible(self.locators.DEPARTMENT_INPUT,).send_keys(department)
			self.element_is_visible(self.locators.SUBMIT_BUTTON,).click()
			count -=1
		return [first_name, last_name, str(age), email, str(salary), department]

	def check_new_added_person(self):
		people_list = self.element_are_present(self.locators.FULL_PEOPLE_LIST)
		data = []
		for item in people_list:
			data.append(item.text.splitlines())
		return data

	def search_person(self, key_word):
		self.element_is_visible(self.locators.SEARCH_INPUT).send_keys(key_word)

	def check_search_person(self):
		delete_button = self.element_is_present(self.locators.DELETE_BUTTON)
		row = delete_button.find_element(By.XPATH, self.locators.PARENT_ROW)
		return row.text.splitlines()

	def update_person_info_first_name(self):
		person_info  = next(generated_person_webtable_page())
		first_name = person_info.first_name
		self.element_is_visible(self.locators.UPDATE_BUTTON).click()
		self.element_is_visible(self.locators.FIRSTNAME_INPUT).clear()
		self.element_is_visible(self.locators.FIRSTNAME_INPUT).send_keys(first_name)
		self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
		return first_name

	def update_person_info_last_name(self):
		person_info = next(generated_person_webtable_page())
		last_name = person_info.last_name
		self.element_is_visible(self.locators.UPDATE_BUTTON).click()
		self.element_is_visible(self.locators.LASTNAME_INPUT).clear()
		self.element_is_visible(self.locators.LASTNAME_INPUT).send_keys(last_name)
		self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
		return last_name


	def update_person_info_email(self):
		person_info = next(generated_person_webtable_page())
		email = person_info.email
		self.element_is_visible(self.locators.UPDATE_BUTTON).click()
		self.element_is_visible(self.locators.EMAIL_INPUT).clear()
		self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(email)
		self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
		return email

	def update_person_info_age(self):
		person_info = next(generated_person_webtable_page())
		age = person_info.age
		self.element_is_visible(self.locators.UPDATE_BUTTON).click()
		self.element_is_visible(self.locators.AGE_INPUT).clear()
		self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
		self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
		return str(age)

	def update_person_info_salary(self):
		person_info = next(generated_person_webtable_page())
		salary = person_info.salary
		self.element_is_visible(self.locators.UPDATE_BUTTON).click()
		self.element_is_visible(self.locators.SALARY_INPUT).clear()
		self.element_is_visible(self.locators.SALARY_INPUT).send_keys(salary)
		self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
		return str(salary)

	def update_person_info_department(self):
		person_info = next(generated_person_webtable_page())
		department = person_info.department
		self.element_is_visible(self.locators.UPDATE_BUTTON).click()
		self.element_is_visible(self.locators.DEPARTMENT_INPUT).clear()
		self.element_is_visible(self.locators.DEPARTMENT_INPUT).send_keys(department)
		self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
		return department

	def delete_person_info(self):
		self.element_is_visible(self.locators.DELETE_BUTTON).click()

	def check_the_users_card_has_been_deleted(self):
		return self.element_is_present(self.locators.NO_ROWS_FOUND).text

	def select_up_to_rows(self):
		count = [5, 10, 20, 25, 100]
		data = []
		for x in count :
			count_rows = (self.go_to_element(self.element_is_visible
											(self.locators.SELECT_ROWS)))
			if count_rows is None:
				print("Элемент не найден или не виден")
				continue
			count_rows.click()
			self.element_is_visible(By.CSS_SELECTOR, f"option[value='{x}']").click()
			data.append(self.check_count_rows)
		return data

	def check_count_rows(self):
		list_rows = self.element_are_present(self.locators.FULL_PEOPLE_LIST)
		return len(list_rows)





