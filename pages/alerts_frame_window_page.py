from locators.alerts_frame_window_locators import BrowserWindowPageLocators
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


