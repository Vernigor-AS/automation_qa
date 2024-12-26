import time

from pages.widgets_page import AccordianPage, AutoCompletePage


class TestWidget:

	class TestAccordian:

		def test_section_widget(self, driver):
			accordian_page = AccordianPage(driver, "https://demoqa.com/accordian")
			accordian_page.open()
			first_title, first_content = accordian_page.check_accordian("first")
			second_title, second_content = accordian_page.check_accordian("second")
			third_title, third_content = accordian_page.check_accordian("third")
			assert first_title == "What is Lorem Ipsum?" and first_content > 0, "Неправильный заголовок или нет текста"
			assert second_title == "Where does it come from?" and second_content > 0, "Неправильный заголовок или нет текста"
			assert third_title == "Why do we use it?" and third_content > 0, "Неправильный заголовок или нет текста"


	class TestAutoComplete:

		def test_fill_multi_autocomplete(self, driver):
			autocomplete_page = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
			autocomplete_page.open()
			colors = autocomplete_page.fill_input_multi()
			colors_result = autocomplete_page.check_color_in_multi()
			assert colors == colors_result, "Добавленных цветов нет в поле ввода"


		def test_remove_value_from_multi(self, driver):
			autocomplete_page = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
			autocomplete_page.open()
			autocomplete_page.fill_input_multi()
			count_value_before, count_value_after = autocomplete_page.remove_value_from_multi()
			assert count_value_before != count_value_after, "Значение не удалено"

		def test_fill_single_autocomplete(self, driver):
			autocomplete_page = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
			autocomplete_page.open()
			color = autocomplete_page.fill_input_single()
			result_in_container = autocomplete_page.check_color_in_single()
			assert color == result_in_container,  "Добавленных цветов нет в поле ввода"



