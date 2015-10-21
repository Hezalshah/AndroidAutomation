__author__ = '1111376'

import unittest
from appium import webdriver
import time
from nose.tools import assert_equals
import os

class TestSignUpEmail(unittest.TestCase):
    def setUp(self):

        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.2'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['app'] = os.path.dirname(os.getcwd()) + '/iHeartRadio-Google-Mobile-AMPProd-release.apk'
        #desired_caps['app'] = home + '/buildAgent/work/ed0abf3fb047da1a/iHeartRadio/gradle-build/outputs/apk/iHeartRadio-Google-Mobile-AMPProd-debug.apk'
        desired_caps['app'] = '/Users/1111376/Downloads/iHeartRadio-Google-Mobile-AMPProd-debug.apk'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_signup_email(self):
        time.sleep(10)
        # select skip button
        self.driver.find_element_by_id('android:id/button2').click()
        # select ok button to the Settings pop up
        self.driver.find_element_by_id('android:id/button1').click()
        self.driver.find_element_by_name('Sign Up').click()
        reg_time = str(time.time())
        self.driver.find_element_by_id('com.clearchannel.iheartradio.controller:id/email').send_keys(reg_time + 'android@mailinator.com')
        self.driver.find_element_by_id('com.clearchannel.iheartradio.controller:id/password').send_keys('tester')
        self.driver.find_element_by_id('com.clearchannel.iheartradio.controller:id/zipcode').send_keys('11215')
        self.driver.find_element_by_id('com.clearchannel.iheartradio.controller:id/spinner_item').click()
        time.sleep(2)
        #self.driver.find_element_by_xpath("//android.widget.ListView[1]/android.widget.TextView[16]").click()
        self.driver.find_element_by_name('2007').click()
        time.sleep(2)
        self.driver.find_element_by_id('com.clearchannel.iheartradio.controller:id/spinner_item').click()
        time.sleep(3)
        self.driver.find_element_by_name('1999').click()
        time.sleep(2)
        self.driver.find_element_by_id('com.clearchannel.iheartradio.controller:id/male').click()
        self.driver.find_element_by_id('com.clearchannel.iheartradio.controller:id/tos').click()
        # submit form
        self.driver.find_element_by_id('com.clearchannel.iheartradio.controller:id/sign_up').click()
        time.sleep(3)

        # verify instructional text displays
        el = self.driver.find_element_by_xpath('//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]')
        assert_equals(el.text, 'Tell us what you like')

        # click "variety"
        self.driver.find_element_by_name('Top 40 & Pop').click()
        self.driver.find_element_by_name('Classic Rock').click()

        # click done
        self.driver.find_element_by_id('com.clearchannel.iheartradio.controller:id/done_btn').click()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSignUpEmail)
    unittest.TextTestRunner(verbosity=2).run(suite)