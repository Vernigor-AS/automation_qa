from selenium.webdriver.common.by import By


class TextBoxPageLocators:

    """для полей (from fields)"""

    FULL_NAME = (By.CSS_SELECTOR, '#userName')
    EMAIL = (By.CSS_SELECTOR, '#userEmail')
    CURRENT_ADDRESS = (By.CSS_SELECTOR, '#currentAddress')
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, '#permanentAddress')
    SUBMIT = (By.CSS_SELECTOR, '#submit')

    """созданная форма (created form)"""

    CREATED_FULL_NAME = (By.CSS_SELECTOR, "#output #name")
    CREATED_EMAIL = (By.CSS_SELECTOR, "#output #email")
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, "#output #currentAddress")
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, "#output #permanentAddress")

class CheckBoxPageLocators:
    """чекбоксы """
    EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, '.rct-icon.rct-icon-expand-all')
    COLLAPSE_ALL_BUTTON = (By.CSS_SELECTOR, '.rct-icon.rct-icon-collapse-all')
    ITEM_LIST = (By.CSS_SELECTOR, "span[class='rct-title']")
    CHECKED_ITEMS = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-check']")
    TITLE_ITEM = ".//ancestor::span[@class='rct-text']"
    OUTPUT_RESULT = (By.CSS_SELECTOR, "span[class='text-success']")

class RadioButtonPageLocators:
    RADIO_BUTTON_YES = (By.CSS_SELECTOR, "label[class^='custom-control'][for='yesRadio']")
    RADIO_BUTTON_IMPRESSIVE = (By.CSS_SELECTOR, "label[class^='custom-control'][for='impressiveRadio']")
    RADIO_BUTTON_NO = (By.CSS_SELECTOR, "label[class^='custom-control'][for='noRadio']")
    OUTPUT_RESULT = (By.CSS_SELECTOR, '.text-success')

class WebTablePageLocators:
    #add person
    ADD_BUTTON = (By.CSS_SELECTOR, "#addNewRecordButton")
    FIRSTNAME_INPUT = (By.CSS_SELECTOR, "#firstName")
    LASTNAME_INPUT = (By.CSS_SELECTOR, "#lastName")
    EMAIL_INPUT = (By.CSS_SELECTOR, "#userEmail")
    AGE_INPUT = (By.CSS_SELECTOR, "#age")
    SALARY_INPUT = (By.CSS_SELECTOR, "#salary")
    DEPARTMENT_INPUT = (By.CSS_SELECTOR, "#department")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "#submit")

    SEARCH_INPUT = (By.CSS_SELECTOR, "#searchBox")
    SELECT_ROWS = (By.CSS_SELECTOR, "select[aria-label='rows per page']")
    SELECT_VALUE_5 = (By.CSS_SELECTOR, "span select [value='5']")
    SELECT_VALUE_10 = (By.CSS_SELECTOR, "span select [value='10']")
    SELECT_VALUE_20 = (By.CSS_SELECTOR, "span select [value='20']")
    SELECT_VALUE_25 = (By.CSS_SELECTOR, "span select [value='25']")
    SELECT_VALUE_100 = (By.CSS_SELECTOR, "span select [value='100']")
    #table
    FULL_PEOPLE_LIST = (By.CSS_SELECTOR, "div[class='rt-tr-group']")
    DELETE_BUTTON = (By.CSS_SELECTOR, "span[title='Delete']")
    PARENT_ROW = "div[class='rt-tr-group']"
    NO_ROWS_FOUND = (By.CSS_SELECTOR, "div[class='rt-noData']")
    COUNT_ROW_LIST = (By.CSS_SELECTOR, "")

    #update
    UPDATE_BUTTON = (By.CSS_SELECTOR, "span[title='Edit']")

class ButtonsPageLocators:
    DOUBLE_CLICK_BUTTON = (By.CSS_SELECTOR, "#doubleClickBtn")
    RIGHT_CLICK_BUTTON = (By.CSS_SELECTOR, "#rightClickBtn")
    CLICK_ME_BUTTON = (By.XPATH, "//div[3]/button")

    #result
    DOUBLE_CLICK_TEXT = (By.XPATH, "//p[text()='You have done a double click']")
    RIGHT_CLICK_TEXT = (By.XPATH, "//p[text()='You have done a right click']")
    CLICK_ME_TEXT = (By.XPATH, "//p[text()='You have done a dynamic click']")

class LinksPageLocators:
    HOME_PAGE_LINK = (By.CSS_SELECTOR, "a[id='simpleLink']")
    HOME_PAGE_DYNAMIC_LINK = (By.CSS_SELECTOR, "a[id='dynamicLink']")
    API_CALL_CREATED = (By.CSS_SELECTOR, "a[id='created']")
    API_CALL_NO_CONTENT = (By.CSS_SELECTOR, "a[id='no-content']")
    API_CALL_MOVED = (By.CSS_SELECTOR, "a[id='moved']")
    API_CALL_BAD_REQUEST = (By.CSS_SELECTOR, "a[id='bad-request']")
    API_CALL_UNAUTHORIZED = (By.CSS_SELECTOR, "a[id='unauthorized']")
    API_CALL_FORBIDDEN = (By.CSS_SELECTOR, "a[id='forbidden']")
    API_CALL_NOT_FOUND = (By.CSS_SELECTOR, "a[id='invalid-url']")
    LINK_RESPONSE_TEXT = (By.CSS_SELECTOR, "p[id='linkResponse']")




