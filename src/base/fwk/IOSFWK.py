__author__ = 'Justin'
import os
from appium import webdriver
from src.base.core.UiFramework import UIFramework


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class IOS(UIFramework):

    def __init__(self):
        UIFramework.__init__(self)


    def getAppType(self):
        return "IOS"

    def __launch_app(self):
        #os.system(r'taskkill /f /im node.exe')
        #os.system(r'start E:\Autotest\Tools\Appium_1_4_6\Appium\node.exe E:\Autotest\Tools\Appium_1_4_6\Appium\node_modules\appium\lib\server\main.js --address 127.0.0.1 --port 4723 --no-reset --platform-name Android')
        desired_caps = {}
        desired_caps['platformVersion']= self._getSutFullFileName("app.device.version")
        desired_caps['deviceName'] = self._getSutFullFileName("app.device.name")
        desired_caps['platform'] = self._getSutFullFileName("app.os.platform")
        desired_caps['newCommandTimeout'] = self._getSutFullFileName("app.command.timeout")
        desired_caps['udid'] = self._getSutFullFileName("app.device.udid")
        desired_caps['platformName'] = self._getSutFullFileName("app.device.platformName")
        desired_caps['app'] = self._getSutFullFileName("app.name")
        self._driver = webdriver.Remote('http://'+str(self._getSutFullFileName("app.appium.serverIP"))+'/wd/hub',desired_caps)
        self._waitByTimeOut(5)


    def openApp(self, page = ""):
        self.UiMapSetPage(page)
        self.__launch_app()

    def close(self):
        self._driver.close()
