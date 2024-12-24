import time

from pages.alerts_frame_window_page import BrowserWindowPage, AlertsWindowPage, FramesPage, NestedFramesPage


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


	class TestAlertWindow:

		def test_click_button_to_see_alert(self, driver):
			click_button = AlertsWindowPage(driver, "https://demoqa.com/alerts")
			click_button.open()
			alert_text = click_button.check_alert_after_click()
			assert alert_text == "You clicked a button", "Алерт не появился"

		def test_click_button_to_see_alert_5sec(self, driver):
			click_button = AlertsWindowPage(driver, "https://demoqa.com/alerts")
			click_button.open()
			alert_text = click_button.check_alert_after_click_5sec()
			assert alert_text == "This alert appeared after 5 seconds", "Алерт не появился"

		def test_click_button_confirm(self, driver):
			click_button = AlertsWindowPage(driver, "https://demoqa.com/alerts")
			click_button.open()
			alert_result = click_button.confirm_or_dismiss_alert()
			assert alert_result == "You selected Ok"


		def test_click_button_promt_box(self, driver):
			click_button = AlertsWindowPage(driver, "https://demoqa.com/alerts")
			click_button.open()
			chosen_name, result_text = click_button.input_text_on_the_alert()
			assert chosen_name in result_text, "Имя не отображается"

	class TestFramesPage:

		def test_frame1(self, driver):
			frame_page = FramesPage(driver, "https://demoqa.com/frames")
			frame_page.open()
			result_frame1 = frame_page.check_frame1('frame1')
			assert result_frame1 == ('This is a sample page', '500px', '350px'), "Рамка не отображается"

		def test_frame2(self, driver):
			frame_page = FramesPage(driver, "https://demoqa.com/frames")
			frame_page.open()
			result_frame2 = frame_page.check_frame2('frame2')
			assert result_frame2 == ('This is a sample page', '100px', '100px'), "Рамка не отображается"


	class TestNestedFramesPage:

		def test_nested_frames(self, driver):
			nested_frame_page = NestedFramesPage(driver, "https://demoqa.com/nestedframes")
			nested_frame_page.open()
			parent_frame, child_frame = nested_frame_page.check_nested_frame()
			assert parent_frame == "Parent frame", "Рамка не отображается"
			assert child_frame == "Child Iframe", "Вложенная рамка не отображается"

