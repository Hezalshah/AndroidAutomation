__author__ = '1111376'

import unittest
from appium import webdriver
import time
import os

class TestLiveStation(unittest.TestCase):
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

    def test_live_station(self):
        time.sleep(10)
        # select skip button
        self.driver.find_element_by_id('android:id/button2').click()
        # select ok button to the Settings pop up
        self.driver.find_element_by_id('android:id/button1').click()
        # select Login
        self.driver.find_element_by_id('com.clearchannel.iheartradio.controller:id/login_gate_log_in').click()
        # enter email
        self.driver.find_element_by_id('com.clearchannel.iheartradio.controller:id/email').send_keys('iheartmediatester@mailinator.com')
        # enter password
        self.driver.find_element_by_id('com.clearchannel.iheartradio.controller:id/password').send_keys('things')
        # submit form
        self.driver.find_element_by_id('com.clearchannel.iheartradio.controller:id/email_login').click()

        time.sleep(2)

        # click search
        self.driver.find_element_by_xpath('//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.support.v4.widget.DrawerLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.support.v7.widget.LinearLayoutCompat[1]/android.widget.TextView[1]').click()

        # search: Z100
        self.driver.find_element_by_xpath('//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.support.v7.widget.LinearLayoutCompat[1]/android.support.v7.widget.LinearLayoutCompat[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.EditText[1]').send_keys('Z100')

        time.sleep(2)

        # click the first item returned (Z100)
        self.driver.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.6, "x": 482, "y": 634})
        time.sleep(3)

        # currently playing
        play_pause = self.driver.find_element_by_id('com.clearchannel.iheartradio.controller:id/playPauseProgress')

        # pausing
        play_pause.click()
        time.sleep(3)

        # play again
        play_pause.click()

         # thumbdown
        scan_btn = self.driver.find_element_by_id('com.clearchannel.iheartradio.controller:id/button_player_thumbdown')
        scan_btn.click()
        time.sleep(2)

        # Thumbup
        scan_btn = self.driver.find_element_by_id('com.clearchannel.iheartradio.controller:id/button_player_thumbup')
        scan_btn.click()
        time.sleep(2)

        # scan the station
        scan_btn = self.driver.find_element_by_id('com.clearchannel.iheartradio.controller:id/button_player_next')
        scan_btn.click()
        time.sleep(2)

        # Favoriting the station
        self.driver.find_element_by_id('com.clearchannel.iheartradio.controller:id/button_player_favorite').click()
        time.sleep(2)

        self.driver.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5612890625, "x": 218, "y": 410})

         #Unfavorite the station
        self.driver.find_element_by_id('com.clearchannel.iheartradio.controller:id/button_player_favorite').click()
        time.sleep(2)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestLiveStation)
    unittest.TextTestRunner(verbosity=2).run(suite)
