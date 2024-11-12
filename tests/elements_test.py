import time
from pages.element_page import TextBoxPage, CheckBoxPage, RadioButtonPage


class TestElements:
    class TestTextBox:

       def test_text_box(self, driver):
        text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
        text_box_page.open()
        full_name, email, current_address, permanent_address = text_box_page.fill_in_all_fields()
        output_name, output_email, output_current_address, output_permanent_address = text_box_page.check_text()
        time.sleep(5)
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



