'''
Created on Dec 16, 2016

@author: OA-User2
'''
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from locators import CapturePageLocators
from locators import MainPageLocators
from locators import LeadCapturePageLocators
from locators import PropertyPageLocators
from token import EQUAL
import sys
from selenium.webdriver.support import expected_conditions as EC
from locators import ComparePageLocators
from selenium.common.exceptions import TimeoutException


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
   

    def click_logo(self):
        self.driver.find_element(*MainPageLocators.LOGO).click()

    def is_title_matched(self):
        return 'OpenEstimates' in self.driver.title

    def click_first_estimate_my_property(self):
        self.driver.find_element(*MainPageLocators.first_estimate).click()

    def click_second_estimate_my_property(self):
        self.driver.find_element(*MainPageLocators.second_estimate).click()

    def enter_property_search_address(self, postcode):
        self.driver.find_element(*MainPageLocators.SuburbSearch).send_keys(postcode)
        WebDriverWait(self.driver, 10).until(
            lambda driver: self.driver.find_elements(*MainPageLocators.suburb_search_auto_dropdown))
        self.driver.find_element(*MainPageLocators.first_address_of_suburb_search).click()


class PropertyCapturePage(BasePage):
    
    def wait_until_find(self,by,location):
        WebDriverWait(self.driver, 10).until(
            lambda driver: self.driver.find_elements(by,location))
    
    def wait_until_visible(self,location1):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(location1)) 
    
    def input_address(self, street_add):
        self.driver.find_element(*CapturePageLocators.property_search_input).send_keys(street_add)
        self.wait_until_find(*CapturePageLocators.autocomplete_list)

    def click_address(self):
        global address 
        address ='3302/21 Scotsman Street'
        addressList = self.driver.find_elements(*CapturePageLocators.autocomplete_list)
        for addres in addressList:
            if address in addres.text:
                addres.click()     
                
    def click_find_property(self):
        self.driver.find_element(*CapturePageLocators.find_property_btn).click()


    def property_not_listed(self):
        self.driver.find_element(*CapturePageLocators.property_not_list).click()
        

    def capture_property_form(self, unit, street_no, street_name, suburb):
        self.driver.find_element(*CapturePageLocators.not_list_form_unit).send_keys(unit)
        self.driver.find_element(*CapturePageLocators.not_list_form_streetno).send_keys(street_no)
        self.driver.find_element(*CapturePageLocators.not_list_form_streetname).send_keys(street_name)
        self.driver.find_element(*CapturePageLocators.not_list_form_suburb).send_keys(suburb)
        
    def verify_streetno_error_msg(self):
        streetno_error_msg = self.driver.find_element(*CapturePageLocators.not_list_form_streetno_err)  
        return streetno_error_msg.is_displayed()
    
    def verify_streetname_error_msg(self):
        streetname_error_msg = self.driver.find_element(*CapturePageLocators.not_list_form_streetname_err)  
        return streetname_error_msg.is_displayed()  
    
    def verify_suburb_error_msg(self):
        suburb_error_msg = self.driver.find_element(*CapturePageLocators.not_list_form_suburb_err)  
        return suburb_error_msg.is_displayed()     
              
    def continue_btn(self):    
        self.driver.find_element(*CapturePageLocators.not_list_form_continue).click()
               
    def back_btn(self):
        self.driver.find_element(*CapturePageLocators.not_list_form_back).click()
        
   
    def choose_property_type(self,prtype):
        self.wait_until_visible((CapturePageLocators.property_type))
        types= self.driver.find_elements(*CapturePageLocators.property_type)
        #ptype = self.driver.find_element_by_xpath("//*[@id='slide1']/div[2]/div['+i+']/div/a/p")
        for ptype in types:            
            if ptype.text == prtype:
                ptype.click()
                break

    def choose_relation(self, relate):
        self.wait_until_visible((CapturePageLocators.relation_to_property))
        relations = self.driver.find_elements(*CapturePageLocators.relation_to_property)
        for relation in relations:
            if relation.text == relate:
                relation.click()
                break
            
    def choose_condition(self,con):
        self.wait_until_visible(CapturePageLocators.condition)
        conditions = self.driver.find_elements(*CapturePageLocators.condition)
        for condition in conditions:
            if condition.text == con:
                condition.click()
                break
            
    def change_attributes(self):
        self.wait_until_visible(CapturePageLocators.bed_plus)
        self.driver.find_element(*CapturePageLocators.bed_plus).click()
        self.driver.find_element(*CapturePageLocators.bath_plus).click()
        
    def click_next(self):
        self.driver.find_element(*CapturePageLocators.next_button_attributes).click()
        
    def choose_special_features(self,fea1):
        self.wait_until_visible(CapturePageLocators.special_features)
        features = self.driver.find_elements(*CapturePageLocators.special_features) 
        for feature in features:
            if feature.text == fea1:
                feature.click()
                break
            
    def click_start_ranking(self):
        self.driver.find_element(*CapturePageLocators.start_ranking_button).click()
        
    def compare_loop(self, con,sz,fea,lo,va):
        for i in range(0,3):
            self.choose_compare_condition(con)
            self.choose_compare_size(sz)
            self.choose_compare_feature(fea)
            self.choose_compare_location(lo)
            self.choose_compare_worth(va)
        
    def choose_compare_condition(self, con):
        try:
            self.wait_until_visible(ComparePageLocators.compare_condition)
            
        except TimeoutException:
            print 'took too long'
                
        conditions = self.driver.find_elements(*ComparePageLocators.compare_condition)
        for condition in conditions:
            if  condition.text == con:
                condition.click()
                break  
            
            
    def choose_compare_size(self, sz):
        self.wait_until_visible(ComparePageLocators.compare_size)
        sizes = self.driver.find_elements(*ComparePageLocators.compare_size)
        for size in sizes:
            if size.text == sz:
                size.click()
                break
            
    def choose_compare_feature(self, fea):
        self.wait_until_visible(ComparePageLocators.compare_feature)
        features = self.driver.find_elements(*ComparePageLocators.compare_feature)
        for feature in features:
            if feature.text == fea:
                feature.click()
                break
            
    def choose_compare_location(self, lo):
        self.wait_until_visible(ComparePageLocators.compare_location)
        locations = self.driver.find_elements(*ComparePageLocators.compare_location) 
        for location in locations:
            if location.text == lo:
                location.click()
                break
            
    def choose_compare_worth(self, va):
        self.wait_until_visible(ComparePageLocators.compare_worth)
        values = self.driver.find_elements(*ComparePageLocators.compare_worth) 
        for value in values:
            if value.text == va:
                value.click()
                break
    
#             
#     def verify_lead_title(self):
#         try:
#             self.wait_until_visible(CapturePageLocators.result_estimation)
#         except TimeoutException:
#             print ' page time out'
#         title_actual = self.driver.find_element(*CapturePageLocators._title_text).text
#         title_expect1 = 'Create your very own Property Profile.'  
#         title_expect2 = 'Sign up to see the sold prices of the properties you just compared'      
#         title_expect3 = 'Sign up to compare more properties and continue to refine your estimate'
#         try:
#             assert title_actual == title_expect2 or title_actual ==title_expect1 or title_actual ==title_expect3
#         except Exception:
#             print 'Title not right'
#             print title_actual

    def verify_new_lead_title(self):
        try:
             self.wait_until_visible(LeadCapturePageLocators.new_lead_title)        
        except Exception:
            print ' form tome out'    
        title_actual = self.driver.find_element(*LeadCapturePageLocators.new_lead_title).text  
        title_expected = 'Your answers are now being calculated into the estimate.'
        try:
            assert title_actual == title_expected
        except Exception:
            print 'Title not right'
            print title_actual 
            
    def lead_form(self,name,email,phone):
          lead_name=self.driver.find_element(*LeadCapturePageLocators.lead_name)
          lead_name.click()
          lead_name.send_keys(name)
          lead_email=self.driver.find_element(*LeadCapturePageLocators.lead_email)
          lead_email.click()
          lead_email.send_keys(email)
          lead_phone=self.driver.find_element(*LeadCapturePageLocators.lead_phone)
          lead_phone.click()
          lead_phone.send_keys(phone)
          
    def click_get_my_estimate(self):
        self.driver.find_element(*LeadCapturePageLocators.get_my_estimate_btn).click()  
        
    def verify_sign_in_title(self):
        self.wait_until_visible(LeadCapturePageLocators.sign_in_title)
        actual_title = self.driver.find_element(*LeadCapturePageLocators.sign_in_title).text
        expected_title = 'Sign in to your account now'
        try:
            assert actual_title == expected_title
        except Exception:
            print ' sign in title not right'
            print actual_title
            
    def enter_sign_in_pass(self, pw):    
        pas = self.driver.find_element(*LeadCapturePageLocators.sign_in_password) 
        pas.click()
        pas.send_keys(pw)              
    
    def click_see_my_estimate(self):
        self.driver.find_element(*LeadCapturePageLocators.see_my_estimate_btn).click()

     
    def verify_address_on_pp(self):
       
        self.wait_until_visible(PropertyPageLocators.property_guide)
        actual_address = self.driver.find_element(*PropertyPageLocators.pp_address).text
        try:
            assert address in actual_address
        except Exception:
            print 'address on pp is not the same as user input in OE'    
    
    
    
    
    
    
    
            
#     def verify_thank_you_title(self):
#         try:
#             self.wait_until_visible(CapturePageLocators.thank_you)
#         except TimeoutException:
#             print 'thank you timeout'    
#         actual_thank_title = self.driver.find_element(*CapturePageLocators.thank_you).text
#         expected_actual_title = 'Thank you.'
#         try:
#              assertTrue(actual_thank_title == expected_actual_title)
#         except Exception:
#             print 'thank you page wrong'
        
#         
#     def choose_whether_to_sell(self,sell):
#         self.wait_until_visible(CapturePageLocators.whether_sell)
#         sell_options=self.driver.find_elements(*CapturePageLocators.whether_sell)
#         for sell_option in sell_options:
#             if sell_option.text == sell:
#                 sell_option.click()
#                 break
#                 
#     def choose_when_to_sell(self,when):
#         self.wait_until_visible(CapturePageLocators.when_to_sell)
#         when_options=self.driver.find_elements(*CapturePageLocators.when_to_sell)
#         for when_option in when_options:
#             if when_option.text == when:
#                 when_option.click()
#                 break
#             
#     def choose_call_back(self,call):
#         self.wait_until_visible(CapturePageLocators.call_back)
#         callback_options=self.driver.find_elements(*CapturePageLocators.call_back)
#         for call_option in callback_options:
#             if call_option == call:
#                 call_option.click()
#                 break
#             
#     def verify_call_back_msg(self):
#         self.wait_until_visible(CapturePageLocators.result_call_text)
#         actual_call_back_msg = self.driver.find_element(*CapturePageLocators.result_call_text)
#         expected_call_msg = 'Great! Someone from our team will be in touch with you shortly.'
#         try:
#             assertTrue(actual_call_back_msg == expected_call_msg)
#         except Exception:
#             print 'call back msg assert failed'                        
