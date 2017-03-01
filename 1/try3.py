'''
Created on Dec 13, 2016

@author: OA-User2
'''
import unittest
from selenium import webdriver

class Test(unittest.TestCase):


    def setUp(self):
        global driver
        driver=webdriver.Chrome()
        driver.get('http://www.openagent.com.au');


    def tearDown(self):
        self.assertEqual(driver.title, "Traveling Tony's Photography - Welcome")
        


    def testName(self):
        driver.quit()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()