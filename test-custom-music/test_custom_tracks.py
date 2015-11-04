__author__ = '1111376'

import unittest
from appium import webdriver
import time
from nose.tools import assert_equals
from os.path import expanduser

class TestCustomStation(unittest.TestCase):
    def setUp(self):
        home = expanduser('~')
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.2'
        desired_caps['deviceName'] = 'Android Emulator'
        ##desired_caps['app'] = home + '/buildAgent/work/ed0abf3fb047da1a/iHeartRadio/gradle-build/outputs/apk/iHeartRadio-Google-Mobile-AMPProd-debug.apk'
        desired_caps['app'] = '/Users/1111376/Downloads/iHeartRadio-google-mobile-ampprod-debug.apk'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
         self.driver.quit()

    def test_custom_track(self):
         time.sleep(10)
         self.driver.find_element_by_id('com.clearchannel.iheartradio.controller:id/zipcode_promt_edit_text').send_keys('10013')
         self.driver.find_element_by_name('Set Location').click()

         self.driver.find_element_by_name('Log In').click()
         #enter email
         self.driver.find_element_by_id('com.clearchannel.iheartradio.controller:id/email').send_keys('android7@mailinator.com')
         #enter password
         self.driver.find_element_by_id('com.clearchannel.iheartradio.controller:id/password').send_keys('tester')
         self.driver.find_element_by_id('com.clearchannel.iheartradio.controller:id/email_login').click()
         time.sleep(5)

         #search the artist
         self.driver.find_element_by_name("Navigate up").click()
         self.driver.find_element_by_name('Artist Radio').click()
         time.sleep(2)

         self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.support.v4.widget.DrawerLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.ListView[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ImageView[1]").click()

         time.sleep(5)

         #play/pause
         self.driver.find_element_by_id('com.clearchannel.iheartradio.controller:id/playPauseProgress').click()
         time.sleep(4)
         self.driver.find_element_by_id('com.clearchannel.iheartradio.controller:id/playPauseProgress').click()
         time.sleep(2)

         #Skip the song
         self.driver.find_element_by_id('com.clearchannel.iheartradio.controller:id/button_player_next').click()
         time.sleep(2)

         # Thumb down playing
         self.driver.find_element_by_id('com.clearchannel.iheartradio.controller:id/button_player_thumbdown').click()
         time.sleep(2)

         self.driver.find_element_by_name('GOT IT').click()
         time.sleep(2)

          # Thumb up playing
         self.driver.find_element_by_id('com.clearchannel.iheartradio.controller:id/button_player_thumbup').click()
         time.sleep(2)

        # verify instructional text displays
        #el = self.driver.find_element_by_xpath('//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.ImageView[1]')
        # assert_equals(el.text, 'Great, we'll play you more songs like this.')

         # Favoriting the station
         self.driver.find_element_by_id('com.clearchannel.iheartradio.controller:id/button_player_favorite').click()
         time.sleep(2)

          # verify instructional text displays
        # el = self.driver.find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]')
        # assert_equals(el.text, 'Favorite station added')

         self.driver.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5612890625, "x": 218, "y": 410})

         #Unfavorite the station
         self.driver.find_element_by_id('com.clearchannel.iheartradio.controller:id/button_player_favorite').click()
         time.sleep(2)
        
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCustomStation)
    unittest.TextTestRunner(verbosity=2).run(suite)