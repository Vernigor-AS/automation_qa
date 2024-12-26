import random

from selenium.common import TimeoutException
from selenium.webdriver import Keys

from generator.generator import generated_color
from locators.widgets_page_locators import AccordianPageLocators, AutoCompletePageLocators
from pages.base_page import BasePage



class AccordianPage(BasePage):

	locators = AccordianPageLocators()

	def check_accordian(self, accordian_num):
		accordian = {"first":
						 {"title": self.locators.SECTION1,
						  "content": self.locators.SECTION1_CONTENT},
					 "second":
						 {"title": self.locators.SECTION2,
						  "content": self.locators.SECTION2_CONTENT},
					 "third":{
						 "title": self.locators.SECTION3,
						 "content": self.locators.SECTION3_CONTENT}
					 }
		section_title = self.element_is_visible(accordian[accordian_num]["title"])
		section_title.click()
		try:
			section_content = self.element_is_visible(accordian[accordian_num]["content"]).text
		except TimeoutException:
			section_title.click()
			section_content = self.element_is_visible(accordian[accordian_num]["content"]).text
		return section_title.text, len(section_content)


class AutoCompletePage(BasePage):

	locators = AutoCompletePageLocators()

	def fill_input_multi(self):
		colors = random.sample(next(generated_color()).color_name, k=random.randint(2, 6))
		for color in colors:
			input_multi = self.element_is_visible(self.locators.MULTI_INPUT)
			input_multi.send_keys(color)
			input_multi.send_keys(Keys.ENTER)
		return colors

	def remove_value_from_multi(self):
		count_value_before = len(self.element_are_present(self.locators.MULTI_VALUE))
		remove_button_list = self.element_are_visible(self.locators.MULTI_VALUE_DELETE)
		for value in remove_button_list:
			value.click()
			break
		count_value_after = len(self.element_are_present(self.locators.MULTI_VALUE))
		return count_value_before, count_value_after

	def check_color_in_multi(self):
		color_list = self.element_are_present(self.locators.MULTI_VALUE)
		colors = []
		for color in color_list:
			colors.append(color.text)
		return colors

	def fill_input_single(self):
		color = random.sample(next(generated_color()).color_name, k=1)
		input_single = self.element_is_clickable(self.locators.SINGLE_INPUT)
		input_single.send_keys(color)
		input_single.send_keys(Keys.ENTER)
		return color[0]

	def check_color_in_single(self):
		color = self.element_is_visible(self.locators.SINGLE_VALUE)
		return color.text



