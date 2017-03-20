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
        self.driver.get('http://wwwuat.openestimates.com.au/')
 

    def tearDown(self):
        self.driver.quit()


    def testFullOEJourney(self):
        main_page = pageobject.MainPage(self.driver)
        estimate_page = pageobject.PropertyCapturePage(self.driver)
        main_page.click_first_estimate_my_property()
        estimate_page.input_address('21 scotsman street')
        estimate_page.click_address()
        estimate_page.click_find_property()
        estimate_page.choose_property_type('Apartment')
        estimate_page.choose_relation('Investor')
        estimate_page.choose_condition('Good')
        estimate_page.change_attributes()
        estimate_page.click_next()
        estimate_page.choose_special_features('Pool')
        estimate_page.click_start_ranking()
        estimate_page.compare_loop('Better','Smaller','Worse','About the same', 'More')
        estimate_page.verify_lead_title()
        estimate_page.lead_form('nancy test','cainaisi@qq.com','0414660628')
        estimate_page.click_get_started()
        estimate_page.verify_thank_you_title
        estimate_page.choose_whether_to_sell('Yes')
        estimate_page.choose_when_to_sell('Not sure')
        estimate_page.choose_call_back('Yes')
        estimate_page.verify_call_back_msg

    

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()