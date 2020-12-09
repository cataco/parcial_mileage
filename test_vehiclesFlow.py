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
        "app": "/Users/ccordob/Downloads/com.evancharlton.mileage.apk"
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

    def test_create_vehicle_with_correct_values(self):
        self.driver.find_element_by_id('com.android.permissioncontroller:id/continue_button').click()
        time.sleep(1)
        self.driver.find_element_by_id('android:id/button1').click()
        time.sleep(1)
        #self.driver.find_element_by_xpath(
        #    "xpath=//[@id='icon' and (./preceding-sibling:: | ./following-sibling::*)[@text='Vehicles']]").click()
        time.sleep(1)
        self.driver.find_element_by_id("android:id/text1").click()
        time.sleep(1)
        self.driver.find_element_by_id('com.evancharlton.mileage:id/title').send_keys('TestVehicleName')
        self.driver.find_element_by_id('com.evancharlton.mileage:id/year').send_keys('2020')
        self.driver.find_element_by_id('com.evancharlton.mileage:id/make').send_keys('Test-Make')
        self.driver.find_element_by_id('com.evancharlton.mileage:id/model').send_keys('Test-Model')
        self.driver.find_element_by_id('com.evancharlton.mileage:id/description').send_keys('Test-Description')
        self.driver.scroll(self.driver.find_element_by_id("com.evancharlton.mileage:id/type"),
                           self.driver.find_element_by_id("com.evancharlton.mileage:id/title"))
        self.driver.find_element_by_id('com.evancharlton.mileage:id/make_default').click()
        self.driver.find_element_by_id('com.evancharlton.mileage:id/distance').click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@text='Kilometers']").click()
        time.sleep(1)
        self.driver.scroll(self.driver.find_element_by_id('com.evancharlton.mileage:id/distance'),
                           self.driver.find_element_by_id("com.evancharlton.mileage:id/description"))
        self.driver.find_element_by_id('com.evancharlton.mileage:id/volume').click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@text='Litres']").click()
        self.driver.find_element_by_id('com.evancharlton.mileage:id/economy').click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@text='Km / Litre']").click()
        self.driver.find_element_by_id('com.evancharlton.mileage:id/currency').send_keys('$')
        self.driver.find_element_by_id('com.evancharlton.mileage:id/save_btn').click()
        time.sleep(1)
        name = self.driver.find_element_by_id("android:id/text1").get_attribute(
            "text")
        self.assertEqual(name, 'TestVehicleName')

    def test_edit_vehicle_with_correct_values(self):
        self.driver.find_element_by_id("android:id/text1").click()
        time.sleep(1)
        #TODO validate dta in form and edit with new values

    def test_edit_vehicle_with_incorrect_values(self):
        self.driver.find_element_by_id("android:id/text1").click()
        #TODO

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    if __name__ == '__main__':
        unittest.main()
