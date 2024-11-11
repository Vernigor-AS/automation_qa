import time
from pages.element_page import TextBoxPage

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
