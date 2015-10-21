__author__ = '1111376'

import unittest
from appium import webdriver
import time
import os

class TestPodcastStation(unittest.TestCase):
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

    def test_podcast_station(self):
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

         # podcast station
        self.driver.find_element_by_name("Navigate up").click()
        self.driver.find_element_by_name('Podcasts').click()
        time.sleep(2)
        self.driver.find_element_by_name('The Breakfast Club').click()
        time.sleep(5)

        # currently playing
        play_pause = self.driver.find_element_by_id('com.clearchannel.iheartradio.controller:id/playPauseProgress')

        # pausing
        play_pause.click()
        time.sleep(3)

        # play again
        play_pause.click()
        time.sleep(3)

        #skip episode
        self.driver.find_element_by_id('com.clearchannel.iheartradio.controller:id/button_player_next').click()
        time.sleep(4)

        # thumbdown
        self.driver.find_element_by_id('com.clearchannel.iheartradio.controller:id/button_player_thumbdown').click()
        time.sleep(2)

        # thumbup
        self.driver.find_element_by_id('com.clearchannel.iheartradio.controller:id/button_player_thumbup').click()
        time.sleep(2)

        # Favoriting the station
        self.driver.find_element_by_id('com.clearchannel.iheartradio.controller:id/button_player_favorite').click()
        time.sleep(2)

        self.driver.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5612890625, "x": 218, "y": 410})

        #Unfavorite the station
        self.driver.find_element_by_id('com.clearchannel.iheartradio.controller:id/button_player_favorite').click()
        time.sleep(2)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPodcastStation)
    unittest.TextTestRunner(verbosity=2).run(suite)
