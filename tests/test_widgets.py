import time

from pages.widgets_page import AccordianPage, AutoCompletePage, DatePickerPage, SliderPage, ProgressBarPage, ToolTips


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

	class TestDatePickerPage:

		def test_change_date(self, driver):
			date_picker_page = DatePickerPage(driver, "https://demoqa.com/date-picker")
			date_picker_page.open()
			value_date_before, value_date_after = date_picker_page.select_date()
			assert value_date_before != value_date_after, "Время и дата не изменились"

		def test_change_date_and_time(self, driver):
			date_picker_page = DatePickerPage(driver, "https://demoqa.com/date-picker")
			date_picker_page.open()
			value_date_before, value_date_after = date_picker_page.select_date_and_time()
			print(value_date_before)
			print(value_date_after)
			assert value_date_before != value_date_after, "Время и дата не изменились"

	class TestSliderPage:

		def test_slider(self, driver):
			slider_page = SliderPage(driver, "https://demoqa.com/slider")
			slider_page.open()
			value_before, value_after = slider_page.change_slider_value()
			assert value_before != value_after, "Значение слайдера не было изменено"


	class TestProgressBarPage:

		def test_progress_bar(self, driver):
			progress_bar_page = ProgressBarPage(driver, "https://demoqa.com/progress-bar")
			progress_bar_page.open()
			value_before, value_after = progress_bar_page.change_progress_bar_value()
			assert value_before != value_after, "Значение прогресс бара не было изменено"

	class TestToolTips:

		def test_tool_tips(self, driver):
			tool_tips_page = ToolTips(driver, "https://demoqa.com/tool-tips")
			tool_tips_page.open()
			button_text, field_text, contrary_text, section_text = tool_tips_page.check_tool_tips()
			assert button_text == "You hovered over the Button", "Текст не отображается или некорректен "
			assert field_text == "You hovered over the text field", "Текст не отображается или некорректен "
			assert contrary_text == "You hovered over the Contrary", "Текст не отображается или некорректен "
			assert section_text == "You hovered over the 1.10.32", "Текст не отображается или некорректен "


