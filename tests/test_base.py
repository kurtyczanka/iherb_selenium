import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from timeouts import Timeouts
from constants import Constants


class BaseTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(Constants.base__url)
        self.driver.maximize_window()
        self.driver.set_page_load_timeout(Timeouts.page_load)

        WebDriverWait(self.driver, Timeouts.page_load).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, Constants.cookies__selector))).click()

        sleep(2)

    def tearDown(self):
        self.driver.quit()


