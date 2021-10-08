import unittest
from selenium import webdriver


class BaseTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://pl.iherb.com/")
        self.driver.maximize_window()
        self.driver.set_page_load_timeout(10)
        self.driver.find_element_by_css_selector("button[id='truste-consent-button']").click()

    def tearDown(self):
        self.driver.quit()
