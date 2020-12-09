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
        # self.driver.find_element_by_xpath(
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
        self.driver.find_element_by_id('com.evancharlton.mileage:id/title').send_keys('-EDIT')
        self.driver.find_element_by_id('com.evancharlton.mileage:id/make').send_keys('-EDIT')
        self.driver.find_element_by_id('com.evancharlton.mileage:id/model').send_keys('-EDIT')
        self.driver.find_element_by_id('com.evancharlton.mileage:id/description').send_keys('-EDIT')
        self.driver.find_element_by_id('com.evancharlton.mileage:id/save_btn').click()
        time.sleep(1)
        title = self.driver.find_element_by_id("android:id/text1").get_attribute(
            "text")
        self.assertEqual(title, '-EDIT')
        self.driver.find_element_by_id("android:id/text1").click()
        time.sleep(1)
        title = self.driver.find_element_by_id('com.evancharlton.mileage:id/title').get_attribute(
            "text")
        self.assertEqual(title, '-EDIT')
        year = self.driver.find_element_by_id('com.evancharlton.mileage:id/year').get_attribute(
            "text")
        self.assertEqual(year, '2020')
        make = self.driver.find_element_by_id('com.evancharlton.mileage:id/make').get_attribute(
            "text")
        self.assertEqual(make, '-EDIT')
        model = self.driver.find_element_by_id('com.evancharlton.mileage:id/model').get_attribute(
            "text")
        self.assertEqual(model, '-EDIT')
        currency = self.driver.find_element_by_id('com.evancharlton.mileage:id/currency').get_attribute(
            "text")
        self.assertEqual(currency, '$$')
        self.driver.back()

    def test_edit_vehicle_with_incorrect_values(self):
        self.driver.find_element_by_id("android:id/text1").click()
        time.sleep(1)
        self.driver.find_element_by_id('com.evancharlton.mileage:id/title').clear()
        self.driver.find_element_by_id('com.evancharlton.mileage:id/year').clear().send_keys('abcd')
        time.sleep(1)
        self.driver.find_element_by_id('com.evancharlton.mileage:id/save_btn').click()
        time.sleep(1)
        self.assertTrue(self.driver.find_element_by_xpath("//*[@text='Invalid vehicle title']").is_displayed())
        year = self.driver.find_element_by_id('com.evancharlton.mileage:id/year').get_attribute("text")
        self.assertEqual(year, 'Year')

    def test_validate_statistics_metrics_match_vehicle(self):
        # Update values in Car
        self.driver.find_element_by_id("android:id/text1").click()
        time.sleep(1)
        self.driver.find_element_by_id('com.evancharlton.mileage:id/distance').click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@text='Kilometers']").click()
        self.driver.find_element_by_id('com.evancharlton.mileage:id/economy').click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@text='Km / Gallon']").click()
        self.driver.find_element_by_id('com.evancharlton.mileage:id/save_btn').click()
        time.sleep(1)
        # Add fill upp
        # self.driver.find_element_by_xpath(
        #    "xpath=//[@id='icon' and (./preceding-sibling:: | ./following-sibling::*)[@text='Fillup']]").click()
        time.sleep(1)
        self.driver.find_element_by_id('com.evancharlton.mileage:id/price').send_keys('5')
        self.driver.find_element_by_id('com.evancharlton.mileage:id/volume').send_keys('10')
        self.driver.find_element_by_id('com.evancharlton.mileage:id/odometer').send_keys('100')
        self.driver.find_element_by_id('com.evancharlton.mileage:id/save_btn').click()
        time.sleep(1)
        # self.driver.find_element_by_xpath(
        #    "xpath=//[@id='icon' and (./preceding-sibling:: | ./following-sibling::*)[@text='Fillup']]").click()
        time.sleep(1)
        self.driver.find_element_by_id('com.evancharlton.mileage:id/price').send_keys('5')
        self.driver.find_element_by_id('com.evancharlton.mileage:id/volume').send_keys('10')
        self.driver.find_element_by_id('com.evancharlton.mileage:id/odometer').send_keys('200')
        self.driver.find_element_by_id('com.evancharlton.mileage:id/save_btn').click()
        time.sleep(1)
        # self.driver.find_element_by_xpath(
        #    "xpath=//[@id='icon' and (./preceding-sibling:: | ./following-sibling::*)[@text='Statistics']]").click()
        self.assertEqual(self.driver.find_element_by_xpath("//*[@text='10.00 km/g']").size(), 3) #fuel economy
        self.assertEqual(self.driver.find_element_by_xpath("//*[@text='$$100.00']").size(), 1) #total cost
        self.assertEqual(self.driver.find_element_by_xpath("//*[@text='10.00 Gallons']").size(), 3) #fuel consumption



    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    if __name__ == '__main__':
        unittest.main()
