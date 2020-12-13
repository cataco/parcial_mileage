import json
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
        self.driver.find_element_by_xpath(
            "//*[@text='Vehicles']/parent::*").click()
        time.sleep(1)
        self.driver.save_screenshot("screenshots/createvehicle_.png")
        self.driver.find_element_by_id("android:id/text1").click()
        time.sleep(1)
        self.driver.find_element_by_id('com.evancharlton.mileage:id/title').send_keys('TestVehicleName')
        self.driver.find_element_by_id('com.evancharlton.mileage:id/year').send_keys('2020')
        self.driver.find_element_by_id('com.evancharlton.mileage:id/make').send_keys('Test-Make')
        self.driver.find_element_by_id('com.evancharlton.mileage:id/model').send_keys('Test-Model')
        self.driver.find_element_by_id('com.evancharlton.mileage:id/description').send_keys('Test-Description')
        self.driver.save_screenshot("screenshots/createvehicle2_.png")
        self.driver.back()
        self.driver.scroll(self.driver.find_element_by_id("com.evancharlton.mileage:id/type"),
                           self.driver.find_element_by_id("com.evancharlton.mileage:id/title"))
        time.sleep(1)
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
        self.driver.save_screenshot("screenshots/createvehicle3_.png")
        name = self.driver.find_element_by_id("android:id/text1").get_attribute(
            "text")
        self.assertEqual(name, 'TestVehicleName')

    def test_edit_vehicle_with_correct_values(self):
        with open('Mileage.json', 'r') as myfile:
            data = myfile.read()
        # parse file
        test_values = json.loads(data)
        for test_value in test_values:
            title = test_value["title"]
            make = test_value["make"]
            model = test_value["model"]
            year = test_value["year"]
            description = "Car: " + title + make
            time.sleep(1)
            self.driver.find_element_by_id("android:id/text1").click()
            time.sleep(1)
            self.driver.find_element_by_id('com.evancharlton.mileage:id/title').send_keys(title)
            self.driver.find_element_by_id('com.evancharlton.mileage:id/make').send_keys(make)
            self.driver.find_element_by_id('com.evancharlton.mileage:id/model').send_keys(model)
            self.driver.find_element_by_id('com.evancharlton.mileage:id/description').send_keys(description)
            self.driver.find_element_by_id('com.evancharlton.mileage:id/year').send_keys(year)
            time.sleep(1)
            self.driver.find_element_by_id('com.evancharlton.mileage:id/save_btn').click()
            time.sleep(1)
            expected_title = self.driver.find_element_by_id("android:id/text1").get_attribute(
                "text")
            self.assertEqual(expected_title, title)
            self.driver.find_element_by_id("android:id/text1").click()
            time.sleep(5)
            expected_title = self.driver.find_element_by_id('com.evancharlton.mileage:id/title').get_attribute(
                "text")
            self.assertEqual(expected_title, title)
            expected_year = self.driver.find_element_by_id('com.evancharlton.mileage:id/year').get_attribute(
                "text")
            self.assertEqual(expected_year, str(year))
            expected_make = self.driver.find_element_by_id('com.evancharlton.mileage:id/make').get_attribute(
                "text")
            self.assertEqual(expected_make, make)
            expected_model = self.driver.find_element_by_id('com.evancharlton.mileage:id/model').get_attribute(
                "text")
            self.assertEqual(expected_model, model)
            self.driver.back()
            self.driver.scroll(self.driver.find_element_by_id("com.evancharlton.mileage:id/type"),
                               self.driver.find_element_by_id("com.evancharlton.mileage:id/title"))
            self.driver.scroll(self.driver.find_element_by_id('com.evancharlton.mileage:id/distance'),
                               self.driver.find_element_by_id("com.evancharlton.mileage:id/description"))
            currency = self.driver.find_element_by_id('com.evancharlton.mileage:id/currency').get_attribute(
                "text")
            self.assertEqual(currency, '$$')
            self.driver.back()

    def test_edit_vehicle_with_incorrect_values(self):
        self.driver.find_element_by_id("android:id/text1").click()
        time.sleep(1)
        self.driver.find_element_by_id('com.evancharlton.mileage:id/title').clear()
        self.driver.find_element_by_id('com.evancharlton.mileage:id/year').clear().send_keys('abcd')
        self.driver.back()
        self.driver.scroll(self.driver.find_element_by_id("com.evancharlton.mileage:id/type"),
                           self.driver.find_element_by_id("com.evancharlton.mileage:id/title"))
        time.sleep(1)
        self.driver.scroll(self.driver.find_element_by_id('com.evancharlton.mileage:id/distance'),
                           self.driver.find_element_by_id("com.evancharlton.mileage:id/description"))
        self.driver.find_element_by_id('com.evancharlton.mileage:id/save_btn').click()
        time.sleep(1)
        self.assertTrue(self.driver.find_element_by_id('com.evancharlton.mileage:id/save_btn').is_displayed())
        year = self.driver.find_element_by_id('com.evancharlton.mileage:id/year').get_attribute("text")
        # self.assertEqual(year, 'Year')
        self.driver.find_element_by_id('com.evancharlton.mileage:id/title').send_keys("New Title")
        time.sleep(1)
        self.driver.back()

    def test_validate_statistics_metrics_match_vehicle(self):
        # Update values in Car
        self.driver.find_element_by_id("android:id/text1").click()
        time.sleep(1)
        self.driver.back()
        self.driver.scroll(self.driver.find_element_by_id("com.evancharlton.mileage:id/type"),
                           self.driver.find_element_by_id("com.evancharlton.mileage:id/title"))
        self.driver.find_element_by_id('com.evancharlton.mileage:id/distance').click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@text='Kilometers']").click()
        time.sleep(1)
        time.sleep(1)
        self.driver.scroll(self.driver.find_element_by_id('com.evancharlton.mileage:id/distance'),
                           self.driver.find_element_by_id("com.evancharlton.mileage:id/description"))
        time.sleep(1)
        self.driver.find_element_by_id('com.evancharlton.mileage:id/economy').click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@text='Km / Gallon']").click()
        self.driver.find_element_by_id('com.evancharlton.mileage:id/save_btn').click()
        time.sleep(1)
        # Add fill upp
        self.driver.find_element_by_xpath(
            "//*[@text='Fillup']/parent::*").click()
        time.sleep(1)
        self.driver.find_element_by_id('com.evancharlton.mileage:id/price').send_keys('5')
        self.driver.find_element_by_id('com.evancharlton.mileage:id/volume').send_keys('10')
        self.driver.find_element_by_id('com.evancharlton.mileage:id/odometer').send_keys('100')
        time.sleep(1)
        self.driver.find_element_by_id('com.evancharlton.mileage:id/save_btn').click()
        time.sleep(1)
        self.driver.find_element_by_xpath(
            "//*[@text='Fillup']/parent::*").click()
        time.sleep(1)
        self.driver.find_element_by_id('com.evancharlton.mileage:id/price').send_keys('5')
        self.driver.find_element_by_id('com.evancharlton.mileage:id/volume').send_keys('10')
        self.driver.find_element_by_id('com.evancharlton.mileage:id/odometer').send_keys('200')
        time.sleep(1)
        self.driver.find_element_by_id('com.evancharlton.mileage:id/save_btn').click()
        time.sleep(1)
        self.driver.find_element_by_xpath(
            "//*[@text='Statistics']/parent::*").click()
        time.sleep(1)
        self.assertEqual(len(self.driver.find_elements_by_xpath("//*[@text='37.85 km/g']")), 3)  # fuel economy
        self.assertTrue(self.driver.find_element_by_xpath("//*[@text='$$100.00']").is_displayed())  # total cost
        # self.assertEqual(len(self.driver.find_elements_by_xpath("//*[@text='10.00 Gallons']")), 3)  # fuel consumption

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    if __name__ == '__main__':
        unittest.main()
