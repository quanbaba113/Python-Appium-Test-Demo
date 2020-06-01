__author__ = 'Justin'

import os

from src.base.core.UiFramework import UIFramework
from selenium.common.exceptions import NoSuchElementException
from appium import webdriver

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class Android(UIFramework):

    def __init__(self):
        UIFramework.__init__(self)

    def getAppType(self):
        return "Android"


    def __launch_app(self):
        #os.system(r'taskkill /f /im node.exe')
        #os.system(r'start E:\Autotest\Tools\Appium_1_4_6\Appium\node.exe E:\Autotest\Tools\Appium_1_4_6\Appium\node_modules\appium\lib\server\main.js --address 127.0.0.1 --port 4723 --no-reset --platform-name Android')
        desired_caps = {}
        desired_caps['platformName']= self._getSutFullFileName("app.device.platformName")
        desired_caps['browserName'] = ''
        desired_caps['deviceName'] = self._getSutFullFileName("app.device.name")
        desired_caps['version'] = self._getSutFullFileName("app.device.version")
        desired_caps['newCommandTimeout'] = self._getSutFullFileName("app.command.timeout")
        desired_caps['app'] = PATH(self._getSutFullFileName("app.path"))
        desired_caps['app-package'] = self._getSutFullFileName("app.package")
        desired_caps['app-activity'] = self._getSutFullFileName("app.activity")
        self._driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
        self._waitByTimeOut(5)


    def openApp(self, page = ""):
        self.UiMapSetPage(page)
        self.__launch_app()


    def getX(self):
        width = self._driver.get_window_size()['width']
        return width

    def getY(self):
        height = self._driver.get_window_size()['height']
        return height

    def swipeOfType(self,type):
        self.waitForTimeOut(500)
        self.log("Swiping " + type + ".")
        windows_x = self.getX()
        windows_y = self.getY()

        swipeLeft = "left"
        swipeLeftSide = "leftSide"
        swipeRight = "right"
        swipeRightSide = "rightSide"
        swipeUp = "up"
        swipeTop = "top"
        swipeDown = "down"
        swipeBottom = "bottom"

        # Sliding screen to the left
        if type.lower() == swipeLeft.lower():
            self._driver.swipe((windows_x * 0.9), (windows_y * 0.5),(windows_x * 0.2), (windows_y * 0.5),1500)
        # From the left of screen to began to slip
        if type.lower() == swipeLeftSide.lower():
            self._driver.swipe(1, (windows_y * 0.5),(windows_x * 0.9), (windows_y * 0.5),1500)
        # Sliding screen to the right
        if type.lower() == swipeRight.lower():
            self._driver.swipe((windows_x * 0.2), (windows_y * 0.5),(windows_x * 0.9), (windows_y * 0.5),1500)
        # From the right of screen to began to slip
        if type.lower() == swipeRightSide.lower():
            self._driver.swipe((windows_x * 0.9), (windows_y * 0.5),(windows_x * 0.2), (windows_y * 0.5),1500)
        # Screen upward sliding
        if type.lower() == swipeUp.lower():
            self._driver.swipe((windows_x * 0.5), (windows_y * 0.9),(windows_x * 0.5), (windows_y * 0.4),1500)
        # From the top of screen to began to slip
        if type.lower() == swipeTop.lower():
            self._driver.swipe((windows_x * 0.5),0 ,(windows_x * 0.5), (windows_y * 0.8),1500)
        # Slide down the screen
        if type.lower() == swipeDown.lower():
            self._driver.swipe((windows_x * 0.5), (windows_y * 0.4),(windows_x * 0.5), (windows_y * 0.9),1500)
        # From the bottom of screen to began to slip
        if type.lower() == swipeBottom.lower():
            self._driver.swipe((windows_x * 0.5), (windows_y * 0.9),(windows_x * 0.5), (windows_y * 0.1),1500)

    def swipeTo(self, begin_x,begin_y,end_x,end_y,duration=500):
        self._driver.swipe(begin_x,begin_y,end_x,end_y,duration)

    # x and y (1-10)
    def swipe(self,start_x,start_y,end_x,end_y):
        self.log("Swipe from [" + start_x + ":" + start_y + "] to [" + end_x + ":" + end_y + "].")
        windowlenX = self.getX()
        windowlenY = self.getY()
        self.swipeTo((windowlenX * start_x / 10), (windowlenY * start_y / 10),(windowlenX * end_x / 10),(windowlenY * end_y / 10), 1500)

    def tap(self,x, y,duration=500):
        width = self.getX()
        height = self.getY()
        self._driver.tap([(width * x,height * y)], duration)

    def back(self):
        self._driver.back()

    def quit(self):
        self._driver.quit()