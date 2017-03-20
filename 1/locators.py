'''
Created on Jan 5, 2017

@author: OA-User2
'''
from selenium.webdriver.common.by import By


class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""
    LOGO = (By.XPATH, '//*[@id="property-navbar-bottom"]/div[1]/div/div/div[1]/a/img')
    first_estimate = (By.ID, 'welcome-continue')
    second_estimate = (By.ID, 'welcome-continue2')
    SuburbSearch = (By.ID, 'property-search')
    suburb_search_auto_dropdown = (By.XPATH, '//*[@id="box-initial"]/div/div/div/ul')
    first_address_of_suburb_search = (By.XPATH, '//*[@id="box-initial"]/div/div/div/ul/li[1]')


class CapturePageLocators(object):
    
    property_search_input = (By.ID, 'address-input')
    autocomplete_list = (By.CLASS_NAME, 'address-autocomplete')
    find_property_btn = (By.ID, 'address-valuation')
    
    property_not_list = (By.CLASS_NAME, 'no-rp-address-li')
    not_list_form_unit = (By.ID, 'unit-number-input')
    not_list_form_streetno = (By.ID, 'street-number-input')
    not_list_form_streetname = (By.ID, 'street-name-input')
    not_list_form_suburb = (By.ID, 'suburb-input')

    not_list_form_streetno_err = (By.ID, 'street-number-input-err-msg')
    not_list_form_streetname_err = (By.ID, 'street-name-input-err-msg')
    not_list_form_suburb_err = (By.ID, 'suburb-input-err-msg')
    
    not_list_form_continue = (By.XPATH, '//*[@id="address-form"]/div/div[5]/a')
    not_list_form_back = (By.XPATH, '//*[@id="address-form"]/div/div[6]/a')
    
    back_arrow = (By.XPATH, "//a[@data-slide='prev']")
    forth_arrow = (By.XPATH, "//a[@data-slide='next']")
    
    property_type = (By.XPATH, "//*[@id='slide1']/div[2]/div/div/a/p")
    relation_to_property = (By.XPATH, "//*[@id='slide2']/div[2]/div/div/a/p")
    condition = (By.XPATH, "//*[@id='slide3']/div[2]/div/div/a/p")
    bed_plus = (By.ID, "proptype-bedrooms-plus")
    bed_minus = (By.ID, "proptype-bedrooms-minus")
    bath_plus = (By.ID, "proptype-bathrooms-plus")
    bath_minus = (By.ID, "proptype-bathrooms-minus")
    car_plus = (By.ID, "proptype-carspaces-plus")
    car_minus = (By.ID, "proptype-carspaces-minus")
    next_button_attributes = (By.XPATH, "//*[@id='slide4']/div[2]/div[4]/a")
    special_features = (By.XPATH, "//*[@id='slide5']/div[2]/div/label")
    start_ranking_button = (By.ID,"btn-start-ranking")

class ComparePageLocators(object):
    compare_condition = (By.XPATH,"//div[@data-question-id='8']/a")
    compare_size = (By.XPATH, "//div[@data-question-id='14']/a")
    compare_feature  = (By.XPATH, "//div[@data-question-id='15']/a")
    compare_location  = (By.XPATH, "//div[@data-question-id='16']/a")
    compare_worth  = (By.XPATH, "//div[@data-question-id='17']/a")
    skip = (By.ID,"skip-property-btn")
    photo_prev = (By.XPATH, "//*[@id=property-image-carousel']/div[4]/a[1]")
    photo_next = (By.XPATH, "//*[@id=property-image-carousel']/div[4]/a[2]")
    question_prev = (By.XPATH,"//*[@id='property-questions-carousel']/div[3]/a[1]")
    question_next = (By.XPATH,"//*[@id='property-questions-carousel']/div[3]/a[2]")
    map_photo =(By.ID, "map-explain")
    
class LeadCapturePageLocators(object):
    result_estimation = (By.ID, "results-estimate")
    lead_title_text = (By.XPATH, "//*[@id='results-feedback']/div/div[2]/h1")    
    lead_name = (By.ID,"name-input-lead")
    lead_email = (By.ID,"email-input-lead")
    lead_phone = (By.ID,"phone-input-lead")
    get_started = (By.LINK_TEXT, "Get started")
    thank_you = (By.XPATH, "//*[@id='results-box']/div[3]/div[1]/b")
    whether_sell = (By.XPATH, "//*[@id='results-selling-question']/div/a")
    when_to_sell = (By.XPATH, "//*[@id='results-selling-period']/div/a")
    call_back = (By.XPATH, "//*[@id='results-agents-shortlist']/div/a")
    result_call_text = (By.XPATH, "//*[@id='results-thank-you']/p")