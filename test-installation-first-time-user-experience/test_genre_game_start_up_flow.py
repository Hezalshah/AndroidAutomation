__author__ = '1111376'

import unittest
from appium import webdriver
import time
import os

class TestGenreGameStartUpFlow(unittest.TestCase):
    def setUp(self):

        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.2'
        desired_caps['deviceName'] = 'Android Emulator'
        #desired_caps['app'] = '/Users/1111096/workspace/android-flagship/iHeartRadio/gradle-build/outputs/apk/iHeartRadio-Google-Mobile-AMPProd-debug.apk'
        desired_caps['app'] = os.path.dirname(os.getcwd()) + '/iHeartRadio-Google-Mobile-AMPProd-release.apk'
        desired_caps['app'] = '/Users/1111376/Downloads/iHeartRadio-google-mobile-ampprod-debug.apk'

        # desired_caps['app'] = home + '/buildAgent/work/ed0abf3fb047da1a/iHeartRadio/gradle-build/outputs/apk/iHeartRadio-Google-Mobile-AMPProd-debug.apk'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_genre_game_start_up_flow(self):
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
        time.sleep(3)
        self.driver.find_element_by_id('com.clearchannel.iheartradio.controller:id/spinner_item').click()
        time.sleep(3)
        self.driver.find_element_by_name('2007').click()
        time.sleep(2)
        self.driver.find_element_by_id('com.clearchannel.iheartradio.controller:id/spinner_item').click()
        time.sleep(3)
        self.driver.find_element_by_name('1999').click()
        #self.driver.find_element_by_xpath("//android.widget.ListView[1]/android.widget.TextView[16]").click()
        self.driver.find_element_by_id('com.clearchannel.iheartradio.controller:id/male').click()
        self.driver.find_element_by_id('com.clearchannel.iheartradio.controller:id/tos').click()
        # submit form
        self.driver.find_element_by_id('com.clearchannel.iheartradio.controller:id/sign_up').click()
        time.sleep(3)
        # select 2 genres
        self.driver.find_element_by_name('Top 40 & Pop').click()
        self.driver.find_element_by_name('Classic Rock').click()
        #tap Done
        self.driver.find_element_by_id('com.clearchannel.iheartradio.controller:id/done_btn').click()

        time.sleep(2)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestGenreGameStartUpFlow)
    unittest.TextTestRunner(verbosity=2).run(suite)
