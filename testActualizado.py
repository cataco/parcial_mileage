import base64
import os
import unittest
import time
from _ast import Assert

import pytest
from appium import webdriver
from appium.webdriver import WebElement


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Untitled(unittest.TestCase):
    reportDirectory = 'reports'
    reportFormat = 'xml'
    dc = {
        "platformName": "Android",
        "automationName": "UiAutomator2",
        "deviceName": "emulator-5556",
        "app": "/Users/SergioM/Downloads/com.evancharlton.mileage.apk"
    }
    testName = 'Untitled'
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.dc['reportDirectory'] = cls.reportDirectory
        cls.dc['reportFormat'] = cls.reportFormat
        cls.dc['testName'] = cls.testName
        cls.dc['udid'] = 'emulator-5554'
        cls.dc['appPackage'] = 'com.evancharlton.mileage'
        cls.dc['appActivity'] = '.Mileage'
        cls.dc['platformName'] = 'android'
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', cls.dc)

    def pruebaNextBack(self):
        self.driver.find_element_by_xpath("xpath=//*[@id='price']").send_keys('22')
        self.driver.find_element_by_xpath("xpath=//*[@id='volume']").send_keys('22')
        self.driver.find_element_by_xpath("xpath=//*[@id='odometer']").send_keys('22')
        self.driver.find_element_by_xpath("xpath=//*[@text='12/12/20']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='OK']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='Save Fillup']").click()
        self.driver.find_element_by_xpath(
            "xpath=//*[@id='icon' and (./preceding-sibling::* | ./following-sibling::*)[@text='Fillup']]").click()
        self.driver.find_element_by_xpath("xpath=//*[@id='price']").send_keys('33')
        self.driver.find_element_by_xpath("xpath=//*[@id='volume']").send_keys('33')
        self.driver.find_element_by_xpath("xpath=//*[@id='odometer']").send_keys('33')
        self.driver.find_element_by_xpath("xpath=//*[@text='12/12/20']").click()
        self.driver.find_element_by_xpath("xpath=//*[@contentDescription='Increase day']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='OK']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='Save Fillup']").click()
        self.driver.find_element_by_xpath(
            "xpath=//*[@id='icon' and (./preceding-sibling::* | ./following-sibling::*)[@text='Fillup']]").click()
        self.driver.find_element_by_xpath("xpath=//*[@id='price']").send_keys('77')
        self.driver.find_element_by_xpath("xpath=//*[@id='volume']").click()
        self.driver.find_element_by_xpath("xpath=//*[@id='volume']").send_keys('77')
        self.driver.find_element_by_xpath("xpath=//*[@id='odometer']").click()
        self.driver.find_element_by_xpath("xpath=//*[@id='odometer']").send_keys('77')
        self.driver.find_element_by_xpath("xpath=//*[@text='12/12/20']").click()
        self.driver.find_element_by_xpath("xpath=//*[@contentDescription='Decrease day']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='OK']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='Save Fillup']").click()
        self.driver.find_element_by_xpath(
            "xpath=//*[@id='icon' and (./preceding-sibling::* | ./following-sibling::*)[@text='History']]").click()
        self.driver.find_element_by_xpath(
            "xpath=//*[@class='android.widget.LinearLayout' and ./*[@text='12/11/20']]").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='Next']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='Previous']").click()

    def pruebaOrden(self):
        self.driver.find_element_by_xpath("xpath=//*[@id='price']").send_keys('22')
        self.driver.find_element_by_xpath("xpath=//*[@id='volume']").send_keys('22')
        self.driver.find_element_by_xpath("xpath=//*[@id='odometer']").send_keys('22')
        self.driver.find_element_by_xpath("xpath=//*[@text='12/12/20']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='OK']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='Save Fillup']").click()
        self.driver.find_element_by_xpath(
            "xpath=//*[@id='icon' and (./preceding-sibling::* | ./following-sibling::*)[@text='Fillup']]").click()
        self.driver.find_element_by_xpath("xpath=//*[@id='price']").send_keys('33')
        self.driver.find_element_by_xpath("xpath=//*[@id='volume']").send_keys('33')
        self.driver.find_element_by_xpath("xpath=//*[@id='odometer']").send_keys('33')
        self.driver.find_element_by_xpath("xpath=//*[@text='12/12/20']").click()
        self.driver.find_element_by_xpath("xpath=//*[@contentDescription='Increase day']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='OK']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='Save Fillup']").click()
        self.driver.find_element_by_xpath(
            "xpath=//*[@id='icon' and (./preceding-sibling::* | ./following-sibling::*)[@text='Fillup']]").click()
        self.driver.find_element_by_xpath("xpath=//*[@id='price']").send_keys('77')
        self.driver.find_element_by_xpath("xpath=//*[@id='volume']").click()
        self.driver.find_element_by_xpath("xpath=//*[@id='volume']").send_keys('77')
        self.driver.find_element_by_xpath("xpath=//*[@id='odometer']").click()
        self.driver.find_element_by_xpath("xpath=//*[@id='odometer']").send_keys('77')
        self.driver.find_element_by_xpath("xpath=//*[@text='12/12/20']").click()
        self.driver.find_element_by_xpath("xpath=//*[@contentDescription='Decrease day']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='OK']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='Save Fillup']").click()
        self.driver.find_element_by_xpath(
            "xpath=//*[@id='icon' and (./preceding-sibling::* | ./following-sibling::*)[@text='History']]").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='12/11/20']").click()
        self.driver.press_keycode(4)  # back
        self.driver.find_element_by_xpath("xpath=//*[@text='12/12/20']").click()
        self.driver.press_keycode(4)  # back
        self.driver.find_element_by_xpath("xpath=//*[@text='12/13/20']").click()
        self.driver.press_keycode(4)  # back


    def pruebaStatistics(self):
        self.driver.find_element_by_xpath("xpath=//*[@id='price']").send_keys('22')
        self.driver.find_element_by_xpath("xpath=//*[@id='volume']").send_keys('22')
        self.driver.find_element_by_xpath("xpath=//*[@id='odometer']").send_keys('22')
        self.driver.find_element_by_xpath("xpath=//*[@text='12/12/20']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='OK']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='Save Fillup']").click()
        self.driver.find_element_by_xpath(
            "xpath=//*[@id='icon' and (./preceding-sibling::* | ./following-sibling::*)[@text='Fillup']]").click()
        self.driver.find_element_by_xpath("xpath=//*[@id='price']").send_keys('33')
        self.driver.find_element_by_xpath("xpath=//*[@id='volume']").send_keys('33')
        self.driver.find_element_by_xpath("xpath=//*[@id='odometer']").send_keys('33')
        self.driver.find_element_by_xpath("xpath=//*[@text='12/12/20']").click()
        self.driver.find_element_by_xpath("xpath=//*[@contentDescription='Increase day']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='OK']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='Save Fillup']").click()
        self.driver.find_element_by_xpath(
            "xpath=//*[@id='icon' and (./preceding-sibling::* | ./following-sibling::*)[@text='Fillup']]").click()
        self.driver.find_element_by_xpath("xpath=//*[@id='price']").send_keys('77')
        self.driver.find_element_by_xpath("xpath=//*[@id='volume']").click()
        self.driver.find_element_by_xpath("xpath=//*[@id='volume']").send_keys('77')
        self.driver.find_element_by_xpath("xpath=//*[@id='odometer']").click()
        self.driver.find_element_by_xpath("xpath=//*[@id='odometer']").send_keys('77')
        self.driver.find_element_by_xpath("xpath=//*[@text='12/12/20']").click()
        self.driver.find_element_by_xpath("xpath=//*[@contentDescription='Decrease day']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='OK']").click()
        self.driver.find_element_by_xpath("xpath=//*[@text='Save Fillup']").click()
        self.driver.find_element_by_xpath("xpath=//*[@id='icon' and (./preceding-sibling::* | ./following-sibling::*)[@text='Statistics']]").click()
        result1 = (self.driver.find_element_by_xpath("xpath=//*[@text='$484.00']"))
        WebElement
        result2 = (self.driver.find_element_by_xpath("xpath=//*[@text='$2500.67']"))
        WebElement
        result3 = (self.driver.find_element_by_xpath("xpath=//*[@text='$5929.00']"))
        Assert.assertEquals(result1.getText(), "$484.00");
        Assert.assertEquals(result2.getText(), "$2500.67");
        Assert.assertEquals(result3.getText(), "$5929.00");


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
