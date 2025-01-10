import random


from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from tests.conftest import driver


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)


    def element_are_visible(self, locator, timeout=12):
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))


    def element_is_visible(self, locator, timeout=12):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))


    def element_is_present(self, locator, timeout=12):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def element_are_present(self, locator, timeout=12):
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def element_is_not_visible(self, locator, timeout=12):
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=12):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def go_to_element(self, element):
        self.driver.execute_script(f'arguments[0].scrollIntoView();', element)

    def select_by_text(self, element, value):
        select = Select(self.element_is_present(element))
        select.select_by_visible_text(value)

    def select_by_index(self, element, index):
        select = Select(self.element_is_visible(element))
        select.select_by_index(index)

    def check_alert(self):
        return wait(self.driver, 10).until(EC.alert_is_present())

    def handle_alert(self):
        alert = self.check_alert()
        alert_text = alert.text
        action = random.choice(['accept', 'dismiss'])
        if action == "accept":
            alert.accept()
            print("Alert accepted.")
        elif action == "dismiss":
            alert.dismiss()
            print("Alert dismissed.")
        return alert_text


    def action_double_click(self, element):
        action = ActionChains(self.driver)
        action.double_click(element)
        action.perform()

    def action_right_click(self, element):
        action = ActionChains(self.driver)
        action.context_click(element)
        action.perform()

    def action_drag_and_drop_by_offset(self, element, x_coord, y_coord):
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(element, x_coord, y_coord)
        action.perform()


