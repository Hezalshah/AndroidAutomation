__author__ = '1111376'

import unittest
from appium import webdriver
import time
from os.path import expanduser

class TestSearchArtist(unittest.TestCase):
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

    def test_search_artist(self):
         time.sleep(10)
         self.driver.find_element_by_id('com.clearchannel.iheartradio.controller:id/zipcode_promt_edit_text').send_keys('10013')
         self.driver.find_element_by_name('Set Location').click()
         self.driver.find_element_by_name('Log In').click()

         #self.driver.find_element_by_id('com.clearchannel.iheartradio.controller:id/login_gate_log_in').click()
         #enter email
         self.driver.find_element_by_id('com.clearchannel.iheartradio.controller:id/email').send_keys('android7@mailinator.com')
         #enter password
         self.driver.find_element_by_id('com.clearchannel.iheartradio.controller:id/password').send_keys('tester')
         self.driver.find_element_by_id('com.clearchannel.iheartradio.controller:id/email_login').click()

         time.sleep(5)

         self.driver.find_element_by_xpath('//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.support.v4.widget.DrawerLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.support.v7.widget.LinearLayoutCompat[1]/android.widget.TextView[1]').click()
         self.driver.find_element_by_xpath('//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.support.v7.widget.LinearLayoutCompat[1]/android.support.v7.widget.LinearLayoutCompat[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.EditText[1]').send_keys('Pink')
         time.sleep(2)

         self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.support.v4.view.ViewPager[1]/android.widget.FrameLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]").click()
         time.sleep(5)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSearchArtist)
    unittest.TextTestRunner(verbosity=2).run(suite)