from pages.alerts_frame_window_page import BrowserWindowPage


class TestAlertsFrameWindow:

	class TestBrowserWindow:

		def test_new_tab(self, driver):
			new_tab_page = BrowserWindowPage(driver, "https://demoqa.com/browser-windows")
			new_tab_page.open()
			text_result = new_tab_page.check_opened_new_tab_or_window(tab=True, window=False)
			assert text_result == "This is a sample page", "Окно не открылось, такого текста нет"


		def test_new_window(self, driver):
			new_tab_page = BrowserWindowPage(driver, "https://demoqa.com/browser-windows")
			new_tab_page.open()
			text_result = new_tab_page.check_opened_new_tab_or_window(tab=False, window=True)
			assert text_result == "This is a sample page", "Окно не открылось, такого текста нет"
