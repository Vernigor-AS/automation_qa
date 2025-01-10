import random
import time

from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select
from generator.generator import generated_color, generated_date
from locators.widgets_page_locators import AccordianPageLocators, AutoCompletePageLocators, DatePickerPageLocators, \
	SliderPageLocators, ProgressBarPageLocators
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

class DatePickerPage(BasePage):
	locators = DatePickerPageLocators()

	def select_date(self):
		date = next(generated_date())
		input_date = self.element_is_visible(self.locators.INPUT_DATE)
		value_date_before = input_date.get_attribute('value')
		input_date.click()
		self.select_by_text(self.locators.SELECT_MONTH, date.month)
		self.select_by_text(self.locators.SELECT_YEAR, date.year)
		self.select_date_item_from_list(self.locators.SELECT_DAY, date.day)
		value_date_after = input_date.get_attribute('value')
		return value_date_before, value_date_after

	def select_date_and_time(self):
		date = next(generated_date())
		input_date = self.element_is_visible(self.locators.INPUT_DATE_AND_TIME)
		value_date_before = input_date.get_attribute('value')
		input_date.click()
		self.element_is_clickable(self.locators.DATE_AND_TIME_MONTH).click()
		self.select_date_item_from_list(self.locators.DATE_AND_TIME_MONTH_LIST, date.month)
		self.element_is_clickable(self.locators.DATE_AND_TIME_YEAR).click()
		self.select_date_item_from_list(self.locators.DATE_AND_TIME_YEAR_LIST, date.year)
		self.element_is_visible(self.locators.DATE_AND_TIME_DAY, date.day).click()
		self.select_date_item_from_list(self.locators.DATE_AND_TIME_TIME_LIST, date.time)
		input_date_after = self.element_is_visible(self.locators.INPUT_DATE_AND_TIME)
		value_date_after = input_date_after.get_attribute('value')
		return value_date_before, value_date_after

	def select_date_item_from_list(self, elements, value):
		item_list = self.element_are_present(elements)
		for item in item_list:
			if item.text == value:
				item.click()
				break


class SliderPage(BasePage):
	locators = SliderPageLocators()

	def change_slider_value(self):
		value_before = self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')
		slider_input = self.element_is_visible(self.locators.INPUT_SLIDER)
		self.action_drag_and_drop_by_offset(slider_input, random.randint(1, 100), 0 )
		value_after = self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')
		return value_before, value_after


class ProgressBarPage(BasePage):
	locators = ProgressBarPageLocators()

	def change_progress_bar_value(self):
		value_before = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).text
		progress_bar = self.element_is_clickable(self.locators.PROGRESS_BAR_BUTTON)
		progress_bar.click()
		time.sleep(random.randint(2, 5))
		value_after = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).text
		return value_before, value_after