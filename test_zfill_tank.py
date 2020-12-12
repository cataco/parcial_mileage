import base64
import os
import unittest
import time

import pytest
from appium import webdriver

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Untitled(unittest.TestCase):
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

    def test_add_fill(self):
        try:
            self.driver.find_element_by_id('android:id/button1').click()
        except:
            pass
        time.sleep(1)
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/"
                                          "android.widget.FrameLayout/android.widget.TabHost/"
                                          "android.widget.LinearLayout/android.widget.TabWidget/"
                                          "android.widget.RelativeLayout[2]/android.widget.TextView").click()
        time.sleep(2)
        fill_count = self.driver.find_elements_by_xpath("/hierarchy/android.widget.FrameLayout"
                                                        "/android.widget.LinearLayout/android.widget.FrameLayout/"
                                                        "android.widget.TabHost/android.widget.LinearLayout/"
                                                        "android.widget.FrameLayout/android.widget.FrameLayout/"
                                                        "android.widget.LinearLayout/android.widget.FrameLayout/"
                                                        "android.widget.LinearLayout/android.widget.ListView/"
                                                        "android.widget.LinearLayout/"
                                                        "android.widget.LinearLayout").__len__()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/"
                                          "android.widget.FrameLayout/android.widget.TabHost/"
                                          "android.widget.LinearLayout/android.widget.TabWidget/"
                                          "android.widget.RelativeLayout[1]/android.widget.TextView").click()
        time.sleep(1)
        self.driver.find_element_by_id("com.evancharlton.mileage:id/price").send_keys('1')
        self.driver.find_element_by_id("com.evancharlton.mileage:id/volume").send_keys('1')
        self.driver.find_element_by_id("com.evancharlton.mileage:id/odometer").send_keys('1')
        self.driver.find_element_by_id("com.evancharlton.mileage:id/save_btn").click()
        time.sleep(2)
        new_fill_count = self.driver.find_elements_by_xpath("/hierarchy/android.widget.FrameLayout"
                                                            "/android.widget.LinearLayout/android.widget.FrameLayout/"
                                                            "android.widget.TabHost/android.widget.LinearLayout/"
                                                            "android.widget.FrameLayout/android.widget.FrameLayout/"
                                                            "android.widget.LinearLayout/android.widget.FrameLayout/"
                                                            "android.widget.LinearLayout/android.widget.ListView/"
                                                            "android.widget.LinearLayout/"
                                                            "android.widget.LinearLayout[1]").__len__()
        self.assertEquals(new_fill_count - fill_count, 1)


def test_edit_fill(self):
    try:
        self.driver.find_element_by_id('android:id/button1').click()
    except:
        pass
    time.sleep(1)
    self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/"
                                      "android.widget.FrameLayout/android.widget.TabHost/"
                                      "android.widget.LinearLayout/android.widget.TabWidget/"
                                      "android.widget.RelativeLayout[2]/android.widget.TextView").click()
    time.sleep(1)
    self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout"
                                      "/android.widget.LinearLayout/android.widget.FrameLayout/"
                                      "android.widget.TabHost/android.widget.LinearLayout/"
                                      "android.widget.FrameLayout/android.widget.FrameLayout/"
                                      "android.widget.LinearLayout/android.widget.FrameLayout/"
                                      "android.widget.LinearLayout/android.widget.ListView/"
                                      "android.widget.LinearLayout/"
                                      "android.widget.LinearLayout[1]").click()
    self.driver.find_element_by_id("com.evancharlton.mileage:id/edit").click()
    time.sleep(1)
    price = '2'
    volume = '2'
    odometer = '2'
    self.driver.find_element_by_id("com.evancharlton.mileage:id/price").send_keys(price)
    self.driver.find_element_by_id("com.evancharlton.mileage:id/volume").send_keys(volume)
    self.driver.find_element_by_id("com.evancharlton.mileage:id/odometer").send_keys(odometer)
    self.driver.find_element_by_id("com.evancharlton.mileage:id/save_btn").click()
    for i in range(2, 5):
        fill_data = self.driver.find_element_by_xpath("/hierarchy/"
                                                      "android.widget.FrameLayout/"
                                                      "android.widget.LinearLayout/"
                                                      "android.widget.FrameLayout[2]/"
                                                      "android.widget.LinearLayout/"
                                                      "android.widget.ScrollView/"
                                                      "android.widget.LinearLayout/"
                                                      "android.widget.LinearLayout[{}]/"
                                                      "android.widget.TextView[2]".format(i)).text
        self.assertTrue(fill_data.contains('2'))

    def test_delete_fill(self):
        try:
            self.driver.find_element_by_id('android:id/button1').click()
        except:
            pass
        time.sleep(1)
        actions = TouchAction(self.driver)
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/"
                                          "android.widget.FrameLayout/android.widget.TabHost/"
                                          "android.widget.LinearLayout/android.widget.TabWidget/"
                                          "android.widget.RelativeLayout[2]/android.widget.TextView").click()
        time.sleep(1)
        fill_count = self.driver.find_elements_by_xpath("/hierarchy/android.widget.FrameLayout"
                                                        "/android.widget.LinearLayout/android.widget.FrameLayout/"
                                                        "android.widget.TabHost/android.widget.LinearLayout/"
                                                        "android.widget.FrameLayout/android.widget.FrameLayout/"
                                                        "android.widget.LinearLayout/android.widget.FrameLayout/"
                                                        "android.widget.LinearLayout/android.widget.ListView/"
                                                        "android.widget.LinearLayout/"
                                                        "android.widget.LinearLayout").__len__()
        element = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout"
                                                    "/android.widget.LinearLayout/android.widget.FrameLayout/"
                                                    "android.widget.TabHost/android.widget.LinearLayout/"
                                                    "android.widget.FrameLayout/android.widget.FrameLayout/"
                                                    "android.widget.LinearLayout/android.widget.FrameLayout/"
                                                    "android.widget.LinearLayout/android.widget.ListView/"
                                                    "android.widget.LinearLayout/"
                                                    "android.widget.LinearLayout[1]")
        actions.long_press(element)
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/"
                                          "android.widget.ListView/android.widget.LinearLayout[2]/"
                                          "android.widget.LinearLayout").click()
        new_fill_count = self.driver.find_elements_by_xpath("/hierarchy/android.widget.FrameLayout"
                                                            "/android.widget.LinearLayout/android.widget.FrameLayout/"
                                                            "android.widget.TabHost/android.widget.LinearLayout/"
                                                            "android.widget.FrameLayout/android.widget.FrameLayout/"
                                                            "android.widget.LinearLayout/android.widget.FrameLayout/"
                                                            "android.widget.LinearLayout/android.widget.ListView/"
                                                            "android.widget.LinearLayout/"
                                                            "android.widget.LinearLayout").__len__()

        self.assertEquals(fill_count - new_fill_count, 1)


@classmethod
def tearDownClass(cls):
    cls.driver.quit()
