from faker.generator import random

from locators.alerts_frame_window_locators import BrowserWindowPageLocators, AlertWindowPageLocators, \
	FramesPageLocators, NestedFramesPageLocators
from pages.base_page import BasePage




class BrowserWindowPage(BasePage):

	locators = BrowserWindowPageLocators()

	def check_opened_new_tab_or_window(self, tab, window):
		if tab:
			self.element_is_visible(self.locators.NEW_TAB_BUTTON).click()
			self.driver.switch_to.window(self.driver.window_handles[-1])
			text_title = self.element_is_present(self.locators.TITLE_NEW_TAB).text
			return text_title
		elif window:
			self.element_is_visible(self.locators.NEW_WINDOW_BUTTON).click()
			self.driver.switch_to.window(self.driver.window_handles[-1])
			text_title = self.element_is_present(self.locators.TITLE_NEW_TAB).text
			return text_title


class AlertsWindowPage(BasePage):

	locators = AlertWindowPageLocators()

	def check_alert_after_click(self):
		self.element_is_visible(self.locators.ALERT_BUTTON).click()
		self.check_alert()
		return self.handle_alert()


	def check_alert_after_click_5sec(self):
		self.element_is_visible(self.locators.TIMER_ALERT_BUTTON).click()
		self.check_alert()
		return self.handle_alert()


	def confirm_or_dismiss_alert(self):
		self.element_is_visible(self.locators.CONFIRM_BUTTON).click()
		self.check_alert()
		self.handle_alert()
		result = self.element_is_visible(self.locators.TEXT_AFTER_CLOSE_ALERT).text
		return result

	def input_text_on_the_alert(self):
		names = ["Анатолий", "Евгений","Оксана", "John", "William", "Samanta", "Victoria"]
		self.element_is_visible(self.locators.PROMT_BUTTON).click()
		alert = self.check_alert()
		random_name = random.choice(names)
		alert.send_keys(random_name)
		self.handle_alert()
		result = self.element_is_visible(self.locators.TEXT_AFTER_INPUT_TEXT_ON_ALERT).text
		return random_name, result

class FramesPage(BasePage):

	locators = FramesPageLocators()

	def check_frame1(self, frame_num):
		if frame_num == 'frame1':
			frame = self.element_is_present(self.locators.BIG_FRAME)
			width = frame.get_attribute('width')
			height = frame.get_attribute('height')
			self.driver.switch_to.frame(frame)
			text = self.element_is_present(self.locators.TITLE_FRAME).text
			self.driver.switch_to.default_content()
			return text, width, height

	def check_frame2(self, frame_num):
		if frame_num == 'frame2':
			frame = self.element_is_present(self.locators.SMALL_FRAME)
			width = frame.get_attribute('width')
			height = frame.get_attribute('height')
			self.driver.switch_to.frame(frame)
			text = self.element_is_present(self.locators.TITLE_FRAME).text
			self.driver.switch_to.default_content()
			return text, width, height

class NestedFramesPage(BasePage):

	locators = NestedFramesPageLocators()

	def check_nested_frame(self):
		parent_frame = self.element_is_present(self.locators.PARENT_FRAME)
		self.driver.switch_to.frame(parent_frame)
		parent_text = self.element_is_present(self.locators.PARENT_TEXT).text
		child_frame = self.element_is_present(self.locators.CHILD_FRAME)
		self.driver.switch_to.frame(child_frame)
		child_text = self.element_is_present(self.locators.CHILD_TEXT).text
		return parent_text, child_text