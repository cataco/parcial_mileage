import os
import unittest
import time

import pytest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class VehiclesFlow(unittest.TestCase):
    reportDirectory = 'reports'
    reportFormat = 'xml'
    dc = {
        "platformName": "Android",
        "automationName": "UiAutomator2",
        "deviceName": "emulator-5556",
        "app": "/Users/ccordob/Downloads/"
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

    def test_edit_vehicle(self):
        self.driver.find_element_by_id('com.android.permissioncontroller:id/continue_button').click()
        time.sleep(1)
        self.driver.find_element_by_id('android:id/button1').click()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    if __name__ == '__main__':
        unittest.main()
