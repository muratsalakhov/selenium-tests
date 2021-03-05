import unittest
from selenium import webdriver
from time import sleep

class SiteTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(r'D:\Workspace\selenium_labs\chromedriver.exe')

    def test_1(self):
        self.driver.get("https://www.artlebedev.ru/case/")

        # определение текстовых полей
        source_textarea = self.driver.find_element_by_id("source")
        target_textarea = self.driver.find_element_by_id("target")
        method_tabs = self.driver.find_element_by_id("method-tabs").find_elements_by_tag_name("a")

        source_textarea.send_keys("привет Мир!")
        method_tabs[0].click()

        for i in range(len(method_tabs)):
            method_tabs[i].click()
            sleep(1)
            if (i==0):
                assert "ПРИВЕТ МИР!" in target_textarea.get_attribute("value")
            elif (i==1):
                assert "привет мир!" in target_textarea.get_attribute("value")
            elif (i==2):
                assert "Привет Мир!" in target_textarea.get_attribute("value")
            elif (i==3):
                assert "Привет мир!" in target_textarea.get_attribute("value")
            elif (i==4):
                assert "ПРИВЕТ мИР!" in target_textarea.get_attribute("value")
unittest.main()