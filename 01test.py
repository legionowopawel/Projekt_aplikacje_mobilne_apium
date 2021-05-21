import unittest
import os
from appium import webdriver
from time import sleep

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__),p)
)

class Test1Appium(unittest.TestCase):
    def setUp(self):
        desired_caps={}
        desired_caps['app'] = PATH('ContactManager.apk') #https://appium.io/docs/en/writing-running-appium/caps/
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = 'Genymotion Cloud' #bo jest w chmurze
        desired_caps['udid'] = 'localhost:10000' # do uzupelnia gdyby nie byl staly
        desired_caps['appPackages'] = 'com.example.android.contactmanager'
        desired_caps['appActivity'] = 'com.example.android.contactmanager.ContactManager'
        #https://support.testsigma.com/support/solutions/articles/32000019977-how-to-find-app-package-and-app-activity-of-your-android-app

        # polaczenie z Appium
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
        self.driver.implicitly_wait(2)

    def tearDown(self):
        self.driver.quit()

    def testForm(self):
        self.assertTrue(True)
        self.driver.is_app_installed('com.example.android.contactmanager')    #sprawdzenie czy zainstalowana. dokumentacja http://appium.io/docs/en/commands/element/find-elements/index.html#selector-strategies
        

if __name__ == 'main':
    suite = unittest.TestLoader().loadTestsFromTestCase(Test1Appium)
    unittest.TextTestRunner(verbosity=2).run(suite)