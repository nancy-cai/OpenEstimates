'''
Created on Dec 13, 2016

@author: OA-User2
'''
import unittest
from selenium import webdriver

class TestAssertEqaul(unittest.TestCase):


    def setUp(self):
        global driver
        driver=webdriver.Chrome()
        driver.get('http://www.openagent.com.au');


    def tearDown(self):
        driver.quit()
        


    def testAssert(self):
       self.assertTrue((driver.title=="Traveling Tony's Photography - Welcome")|(driver.title=="Find and Compare the Best Real Estate Agents - OpenAgent"))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()