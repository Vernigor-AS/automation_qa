import os
import time

from selenium.webdriver import Keys

from generator.generator import generated_file, generated_subject, generated_person_form_page
from locators.form_page_locators import FormPageLocators
from pages.base_page import BasePage


class FormPage(BasePage):

	locators = FormPageLocators()

	def fill_form_fields(self):
		person = next(generated_person_form_page())
		file_name, path = generated_file()
		self.element_is_visible(self.locators.FIRST_NAME).send_keys(person.first_name)
		self.element_is_visible(self.locators.LAST_NAME).send_keys(person.last_name)
		self.element_is_visible(self.locators.EMAIL).send_keys(person.email)
		self.element_is_visible(self.locators.GENDER).click()
		self.element_is_visible(self.locators.MOBILE).send_keys(person.mobile)
		self.element_is_visible(self.locators.SUBJECTS).send_keys(generated_subject())
		self.element_is_visible(self.locators.SUBJECTS).send_keys(Keys.RETURN)
		date_of_birth = self.element_is_visible(self.locators.DATE_OF_BIRTH)
		if date_of_birth:
			date_of_birth.click()
			self.driver.execute_script("arguments[0].value='';", date_of_birth)
			date_of_birth.send_keys(person.birth.strftime("%Y-%m-%d"))
			date_of_birth.send_keys(Keys.RETURN)
		self.element_is_visible(self.locators.HOBBIES).click()
		self.element_is_present(self.locators.FILE_INPUT).send_keys(path)
		os.remove(path)
		time.sleep(1)
		current_address = self.element_is_visible(self.locators.CURRENT_ADDRESS).click()
		if current_address:
			current_address.click()
			current_address.send_keys(person.current_address)
		self.element_is_visible(self.locators.SELECT_STATE).click()
		self.element_is_visible(self.locators.STATE_INPUT).send_keys(Keys.RETURN)
		self.element_is_visible(self.locators.SELECT_CITY).click()
		self.element_is_visible(self.locators.CITY_INPUT).send_keys(Keys.RETURN)
		self.element_is_visible(self.locators.SUBMIT).click()
		return person

	def result_form(self):
		result_list = self.element_are_visible(self.locators.RESULT_TABLE)
		data_form = []
		for item in result_list:
			self.go_to_element(item)
			data_form.append(item.text)
		return data_form
