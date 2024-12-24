from selenium.webdriver.common.by import By


class BrowserWindowPageLocators:

	NEW_TAB_BUTTON = (By.CSS_SELECTOR, "#tabButton")
	NEW_WINDOW_BUTTON = (By.CSS_SELECTOR, "#windowButton")

	TITLE_NEW_TAB = (By.CSS_SELECTOR, "#sampleHeading")

class AlertWindowPageLocators:

	ALERT_BUTTON = (By.CSS_SELECTOR, "button[id='alertButton']")
	TIMER_ALERT_BUTTON = (By.CSS_SELECTOR, "button[id='timerAlertButton']")
	CONFIRM_BUTTON = (By.CSS_SELECTOR, "button[id='confirmButton']")
	PROMT_BUTTON = (By.CSS_SELECTOR, "button[id='promtButton']")

	#alert result
	TEXT_AFTER_CLOSE_ALERT = (By.CSS_SELECTOR, "span[id='confirmResult'")
	TEXT_AFTER_INPUT_TEXT_ON_ALERT = (By.CSS_SELECTOR, "span[id='promptResult'")

class FramesPageLocators:

	BIG_FRAME = (By.CSS_SELECTOR, "iframe[id='frame1']")
	SMALL_FRAME = (By.CSS_SELECTOR, "iframe[id='frame2']")
	TITLE_FRAME = (By.CSS_SELECTOR, "#sampleHeading")

class NestedFramesPageLocators:
	PARENT_FRAME = (By.CSS_SELECTOR, "iframe[id='frame1']")
	PARENT_TEXT = (By.CSS_SELECTOR, "body")
	CHILD_FRAME = (By.CSS_SELECTOR, "iframe[srcdoc='<p>Child Iframe</p>']")
	CHILD_TEXT = (By.CSS_SELECTOR, "p")

class ModalDialogsPageLocators:

	SMALL_MODAL_BUTTON = (By.CSS_SELECTOR, "button[id='showSmallModal']")
	CLOSE_SMALL_MODAL_BUTTON = (By.CSS_SELECTOR, "button[id='closeSmallModal']")
	LARGE_MODAL_BUTTON = (By.CSS_SELECTOR, "button[id='showLargeModal']")
	CLOSE_LARGE_MODAL_BUTTON = (By.CSS_SELECTOR, "button[id='closeLargeModal']")
	TITLE_TEXT_MODAL = (By.CSS_SELECTOR, "div[class ='modal-header']")
	TEXT_MODAL_BODY = (By.CSS_SELECTOR, "div[class='modal-body']")
