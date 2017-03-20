'''
Created on Dec 13, 2016

@author: OA-User2
'''
import time
import unittest

from selenium import webdriver

import pageobject


class Test(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://www.openestimates.com.au/')
 
    def test_logo_navigation(self):
        main_page = pageobject.MainPage(self.driver)
        main_page.click_logo()
        assert main_page.is_title_matched(), 'Not Navigate to OE Homepage'
 
    def test_suburb_search(self):
        main_page = pageobject.MainPage(self.driver)
        main_page.enter_property_search_address('222')
 
    def test_first_estimate_button(self):
        main_page = pageobject.MainPage(self.driver)
        estimate_page = pageobject.PropertyCapturePage(self.driver)
        main_page.click_first_estimate_my_property()
        estimate_page.input_address('21 Scotsman Street')
        estimate_page.click_address()
        
    def test_not_listed_property_from(self):  
        main_page = pageobject.MainPage(self.driver)
        estimate_page = pageobject.PropertyCapturePage(self.driver)
        main_page.click_first_estimate_my_property() 
        estimate_page.input_address('34 thaa')
        time.sleep(3)
        estimate_page.property_not_listed()
        time.sleep(3)
        estimate_page.capture_property_form('23', '3', 'test st.', '')
        estimate_page.continue_btn()
        estimate_page.verify_suburb_error_msg()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
