__author__ = '1111376'

import unittest
from appium import webdriver
import time
from nose.tools import assert_equals
import os

class TestCustomStation(unittest.TestCase):
    def setUp(self):

        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.2'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['app'] = os.path.dirname(os.getcwd()) + '/iHeartRadio-Google-Mobile-AMPProd-release.apk'
        #desired_caps['app'] = '/Users/1111096/workspace/android-flagship/iHeartRadio/gradle-build/outputs/apk/iHeartRadio-Google-Mobile-AMPProd-debug.apk'
        desired_caps['app'] = '/Users/1111376/Downloads/iHeartRadio-Google-Mobile-AMPProd-debug.apk'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_pause_resume_station(self):
        time.sleep(10)
        # select skip button
        self.driver.find_element_by_id('android:id/button2').click()
        # select ok button to the Settings pop up
        self.driver.find_element_by_id('android:id/button1').click()
        # select Login
        self.driver.find_element_by_id('com.clearchannel.iheartradio.controller:id/login_gate_log_in').click()
        # enter email
        self.driver.find_element_by_id('com.clearchannel.iheartradio.controller:id/email').send_keys('android15@mailinator.com')
        # enter password
        self.driver.find_element_by_id('com.clearchannel.iheartradio.controller:id/password').send_keys('tester')
        # submit form
        self.driver.find_element_by_id('com.clearchannel.iheartradio.controller:id/email_login').click()

        time.sleep(2)

        self.driver.find_element_by_name("Navigate up").click()
        self.driver.find_element_by_name('Listening History').click()
        time.sleep(2)

        #Listen the station
        self.driver.find_element_by_id('com.clearchannel.iheartradio.controller:id/popupwindow_btn').click()
        self.driver.find_element_by_name('Listen Now').click()
        time.sleep(5)
        self.driver.find_element_by_name("Navigate up").click()

        time.sleep(10)
        #Thumb up the track
        self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.support.v4.widget.DrawerLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.widget.ListView[1]/android.widget.FrameLayout[2]/android.widget.RelativeLayout[1]/android.widget.ImageView[2]").click()
        self.driver.find_element_by_name('Thumbs Up').click()
        time.sleep(2)

        #Thumb Down the track
        self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.support.v4.widget.DrawerLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.widget.ListView[1]/android.widget.FrameLayout[2]/android.widget.RelativeLayout[1]/android.widget.ImageView[2]").click()
        self.driver.find_element_by_name('Thumbs Down').click()
        time.sleep(2)

        #No Perference
        self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.support.v4.widget.DrawerLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.widget.ListView[1]/android.widget.FrameLayout[2]/android.widget.RelativeLayout[1]/android.widget.ImageView[2]").click()
        self.driver.find_element_by_name('No Preference').click()
        time.sleep(2)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCustomStation)
    unittest.TextTestRunner(verbosity=2).run(suite)
