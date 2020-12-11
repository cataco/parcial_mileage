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
        "app": "C:\\Users\\usuario\\Downloads\\com.evancharlton.mileage (1).apk"
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
        cls.driver.start_recording_screen()
        filepath = os.path.join(BASE_DIR,
                                "python/recording/test_order_about_menu" + time.strftime("%Y_%m_%d_%H%M%S") + ".mp4")

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
        fill_count = self.driver.find_elements_by_xpath("/hierarchy/android.widget.FrameLayout"
                                                        "/android.widget.LinearLayout/android.widget.FrameLayout/"
                                                        "android.widget.TabHost/android.widget.LinearLayout/"
                                                        "android.widget.FrameLayout/android.widget.FrameLayout/"
                                                        "android.widget.LinearLayout/android.widget.FrameLayout/"
                                                        "android.widget.LinearLayout/android.widget.ListView/"
                                                        "android.widget.LinearLayout/"
                                                        "android.widget.LinearLayout").__len__()
        element = self.driver.find_elements_by_xpath("/hierarchy/android.widget.FrameLayout"
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

    def tearDown(self):
        self.driver.quit()

