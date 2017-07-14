# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest

class AddIncident(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome("C:\\tests\\JARs\\chromedriver_win32\\chromedriver.exe")
        #self.wd=WebDriver.Firefox()
        self.wd.maximize_window()
        self.wd.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_add_incident(self):
        wd = self.wd
        wd.get("https://docit-preprod.stopit.fm/")
        wd.find_element_by_id("password").clear()
        wd.find_element_by_id("password").send_keys("Stopit1234")
        wd.find_element_by_id("email").clear()
        wd.find_element_by_id("email").send_keys("tj2@stopit.fm")
        wd.find_element_by_id("loginButton").click()
        wd.find_element_by_css_selector("div.icon.add_incident").click()
        wd.find_element_by_id("notes").clear()
        wd.find_element_by_id("notes").send_keys("123")
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys("123")
        wd.find_element_by_id("cancelNewIncident").click()
        wd.find_element_by_css_selector("div.icon.home").click()
        wd.find_element_by_css_selector("div.down_arrow").click()
        wd.find_element_by_xpath("//li[@onclick=\"javascript:location.href='/logout/';\"]").click()

    
    def tearDown(self):
        self.wd.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
