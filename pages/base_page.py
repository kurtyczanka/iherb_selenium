from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def move_mouse_to_element(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()
