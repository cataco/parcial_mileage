import base64
import os
import unittest
import time

import pytest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Untitled(unittest.TestCase):
    reportDirectory = 'reports'
    reportFormat = 'xml'
    dc = {
        "platformName": "Android",
        "automationName": "UiAutomator2",
        "deviceName": "emulator-5556",
        "app": "C:\\Users\\usuario\\Downloads\\signedMutants\\parcial2\\com.evancharlton.mileage-mutant25\\com.evancharlton.mileage_3110-aligned-debugSigned.apk"
    }
    testName = 'Untitled'
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.dc['reportDirectory'] = cls.reportDirectory
        cls.dc['reportFormat'] = cls.reportFormat
        cls.dc['testName'] = cls.testName
        cls.dc['udid'] = ''
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
                                                            "android.widget.LinearLayout").__len__()
        self.assertEquals(new_fill_count - fill_count, 1)

    def test_delete_fill(self):
        time.sleep(2)
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/"
                                          "android.widget.FrameLayout/android.widget.TabHost/"
                                          "android.widget.LinearLayout/android.widget.TabWidget/"
                                          "android.widget.RelativeLayout[1]/android.widget.TextView").click()
        time.sleep(2)
        self.driver.find_element_by_id("com.evancharlton.mileage:id/price").send_keys('3')
        self.driver.find_element_by_id("com.evancharlton.mileage:id/volume").send_keys('3')
        self.driver.find_element_by_id("com.evancharlton.mileage:id/odometer").send_keys('3')
        self.driver.find_element_by_id("com.evancharlton.mileage:id/save_btn").click()
        time.sleep(2)
        actions = TouchAction(self.driver)
        fill_count = self.driver.find_elements_by_xpath("/hierarchy/android.widget.FrameLayout"
                                                        "/android.widget.LinearLayout/android.widget.FrameLayout/"
                                                        "android.widget.TabHost/android.widget.LinearLayout/"
                                                        "android.widget.FrameLayout/android.widget.FrameLayout/"
                                                        "android.widget.LinearLayout/android.widget.FrameLayout/"
                                                        "android.widget.LinearLayout/android.widget.ListView/"
                                                        "android.widget.LinearLayout").__len__()
        print(fill_count)
        element = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout"
                                                    "/android.widget.LinearLayout/android.widget.FrameLayout/"
                                                    "android.widget.TabHost/android.widget.LinearLayout/"
                                                    "android.widget.FrameLayout/android.widget.FrameLayout/"
                                                    "android.widget.LinearLayout/android.widget.FrameLayout/"
                                                    "android.widget.LinearLayout/android.widget.ListView/"
                                                    "android.widget.LinearLayout/"
                                                    "android.widget.LinearLayout[1]/android.widget.TextView")
        actions.long_press(element)
        actions.perform()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/"
                                          "android.widget.ListView/android.widget.LinearLayout[2]").click()

        self.driver.find_element_by_id("android:id/button1").click()
        time.sleep(2)
        new_fill_count = self.driver.find_elements_by_xpath("/hierarchy/android.widget.FrameLayout/"
                                                            "android.widget.LinearLayout/android.widget.FrameLayout/"
                                                            "android.widget.TabHost/android.widget.LinearLayout/"
                                                            "android.widget.FrameLayout/android.widget.FrameLayout/"
                                                            "android.widget.LinearLayout/android.widget.FrameLayout/"
                                                            "android.widget.LinearLayout/android.widget.ListView/"
                                                            "android.widget.LinearLayout").__len__()
        self.assertEquals(fill_count - new_fill_count, 1)

    def test_edit_fill(self):
        time.sleep(1)
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout"
                                          "/android.widget.LinearLayout/android.widget.FrameLayout/"
                                          "android.widget.TabHost/android.widget.LinearLayout/"
                                          "android.widget.FrameLayout/android.widget.FrameLayout/"
                                          "android.widget.LinearLayout/android.widget.FrameLayout/"
                                          "android.widget.LinearLayout/android.widget.ListView/"
                                          "android.widget.LinearLayout/"
                                          "android.widget.LinearLayout[1]").click()
        time.sleep(2)
        self.driver.find_element_by_id("com.evancharlton.mileage:id/edit").click()
        time.sleep(2)
        self.driver.find_element_by_id("com.evancharlton.mileage:id/price").send_keys('2')
        self.driver.find_element_by_id("com.evancharlton.mileage:id/volume").send_keys('2')
        self.driver.find_element_by_id("com.evancharlton.mileage:id/odometer").send_keys('2')
        self.driver.find_element_by_id("com.evancharlton.mileage:id/save_btn").click()
        time.sleep(2)
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

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
