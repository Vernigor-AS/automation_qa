import time


import pytest

from conftest import driver
from pages.element_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonsPage, LinksPage


class TestElements:
	class TestTextBox:

		def test_text_box(self, driver):
			text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
			text_box_page.open()
			full_name, email, current_address, permanent_address = text_box_page.fill_in_all_fields()
			output_name, output_email, output_current_address, output_permanent_address = text_box_page.check_text()
			assert full_name == output_name, "Полное имя не совпадает"
			assert email == output_email, "email не совпадает"
			assert current_address == output_current_address, "Текущий адрес не совпадает"
			assert permanent_address == output_permanent_address, "Адрес прописки не совпадает"

	class TestCheckBox:
		def test_check_box(self, driver):
			check_box = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
			check_box.open()
			check_box.open_full_list()
			check_box.click_random_checkbox()
			input_checkboxes = check_box.get_checked_checkboxes()
			output_result = check_box.get_output_result()
			assert input_checkboxes == output_result, 'Чекбоксы не выбраны'

	class TestRadioButton:

		def test_radio_button(self, driver):
			radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
			radio_button_page.open()
			radio_button_page.click_on_the_radio_button('yes')
			output_yes = radio_button_page.get_output_result()
			radio_button_page.click_on_the_radio_button('impressive')
			output_impressive = radio_button_page.get_output_result()
			radio_button_page.click_on_the_radio_button('no')
			output_no = radio_button_page.get_output_result()
			assert output_yes == 'Yes', "Кнопка 'YES' не выбрана"
			assert output_impressive == 'Impressive', "Кнопка 'Impressive' не выбрана"
			assert output_no == 'No', "Кнопка 'No' не выбрана"

	class TestWebTable:

		def test_web_table_add_person(self, driver):
			web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
			web_table_page.open()
			web_table_page.add_button()
			new_person = web_table_page.web_table_add_new_person()
			table_result = web_table_page.check_new_added_person()
			print(new_person)
			print(table_result)
			assert new_person in table_result

		def test_web_table_search_person(self, driver):
			web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
			web_table_page.open()
			web_table_page.add_button()
			last_name = web_table_page.web_table_add_new_person()[1]
			web_table_page.search_person(last_name)
			table_result = web_table_page.check_search_person()
			assert last_name in table_result, "Искомый человек не отображается в таблице "

		def test_web_table_update_person_info(self, driver):
			web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
			web_table_page.open()
			web_table_page.add_button()
			last_name = web_table_page.web_table_add_new_person()[1]
			web_table_page.search_person(last_name)
			email = web_table_page.update_person_info_email()
			row = web_table_page.check_search_person()
			assert email in row, "Карточка пользователя не была изменена"

		def test_web_table_delete_person_info(self, driver):
			web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
			web_table_page.open()
			web_table_page.add_button()
			last_name = web_table_page.web_table_add_new_person()[1]
			web_table_page.search_person(last_name)
			web_table_page.delete_person_info()
			text = web_table_page.check_the_users_card_has_been_deleted()
			assert text == "No rows found", "Карточка пользователя не была удалена"

		@pytest.mark.xfail
		def test_web_table_change_count_row(self, driver):
			web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
			web_table_page.open()
			count = web_table_page.select_up_to_rows()
			assert count == [5, 10, 20, 25, 100], "Невозможно выбрать больше 20 строк"

	class TestButtonsPage:

		def test_different_click_on_the_buttons(self, driver):
			button_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
			button_page.open()
			double = button_page.tap_on_the_double_click_button('double')
			right = button_page.tap_on_the_right_click_button('right')
			click = button_page.tap_on_the_click_me_button('click')
			assert double == 'You have done a double click' , "Текст о двойном нажатии отсутствует"
			assert right == 'You have done a right click', "Текст о нажатии правой кнопки мыши отсутствует"
			assert click == 'You have done a dynamic click', "Тест о нажатии отсутствует"

class TestLinksPage:

	@pytest.mark.need_rewiev
	def test_home_and_dynamic_link(self, driver):
		links_page = LinksPage(driver, 'https://demoqa.com/links')
		links_page.open()
		home_link = links_page.go_to_home_link(driver)
		time.sleep(3)
		dynamic_link = links_page.go_to_dynamic_link(driver)
		time.sleep(3)
		"""Две ссылки на одну и ту же страницу"""

		assert home_link == "https://demoqa.com/", "Домашняя страница не отображается"
		assert dynamic_link == "https://demoqa.com/", "Домашняя страница не отображается"


	def test_will_send_an_api_call_created_link(self, driver):
		links_page = LinksPage(driver, 'https://demoqa.com/links')
		links_page.open()
		check_status = links_page.check_created_api_link()
		assert '201' in check_status.text

	def test_will_send_an_api_call_no_content_link(self, driver):
		links_page = LinksPage(driver, 'https://demoqa.com/links')
		links_page.open()
		check_status = links_page.check_no_content_link()
		assert '204' in check_status.text

	def test_will_send_an_api_call_moved_link(self, driver):
		links_page = LinksPage(driver, 'https://demoqa.com/links')
		links_page.open()
		check_status = links_page.check_moved_link()
		assert '301' in check_status.text

	def test_will_send_an_api_call_bad_request_link(self, driver):
		links_page = LinksPage(driver, 'https://demoqa.com/links')
		links_page.open()
		check_status = links_page.check_bad_request_link()
		assert '400' in check_status.text

	def test_will_send_an_api_call_unauthorized_link(self, driver):
		links_page = LinksPage(driver, 'https://demoqa.com/links')
		links_page.open()
		check_status = links_page.check_unauthorized_link()
		assert '401' in check_status.text

	def test_will_send_an_api_call_forbidden_link(self, driver):
		links_page = LinksPage(driver, 'https://demoqa.com/links')
		links_page.open()
		check_status = links_page.check_forbidden_link()
		assert '403' in check_status.text

	def test_will_send_an_api_call_not_found_link(self, driver):
		links_page = LinksPage(driver, 'https://demoqa.com/links')
		links_page.open()
		check_status = links_page.check_not_found_link()
		assert '404' in check_status.text
