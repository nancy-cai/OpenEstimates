'''
Created on Feb 21, 2017

@author: OA-User2
'''
import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import pageobject
from locators import CapturePageLocators
from locators import MainPageLocators


class Test(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.driver.get('http://www.openestimates.com.au/')
 

    def tearDown(self):
        self.driver.quit()


    def testFullOEJourneywithCL(self):
        main_page = pageobject.MainPage(self.driver)
        estimate_page = pageobject.PropertyCapturePage(self.driver)
        main_page.click_first_estimate_my_property()
        estimate_page.input_address('21 scotsman street')
        estimate_page.click_address()
        estimate_page.click_find_property()
        estimate_page.choose_property_type('Apartment')
        estimate_page.choose_relation('Investor')
        estimate_page.choose_condition('Good')
        time.sleep(2)
        estimate_page.change_attributes()
        time.sleep(2)
        estimate_page.click_next()
        time.sleep(2)
        estimate_page.choose_special_features('Pool')
        time.sleep(2)
        estimate_page.click_start_ranking()
        time.sleep(5)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()