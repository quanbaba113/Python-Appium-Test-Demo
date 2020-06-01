__author__ = 'Justin'

from src.base.core.UiFramework import UIFramework
from selenium import webdriver


class WebFramework(UIFramework):

    def __init__(self):
        UIFramework.__init__(self)

    def getAppType(self):
        return "Web"

    def get(self,url):
        self.log("Open the URL : " + url)
        self._driver.get(url)

    def openApp(self,page = ""):
        profile = self._dataFile + "/profile/firefox/default"
        profile = webdriver.FirefoxProfile(profile)
        self._driver = webdriver.Firefox(profile)
        self.get(self._getSutFullFileName("app."+self.getAppName()+"."+self.getAppType()+".url"))
        self.UiMapSetPage(page)

    def close(self):
        self._driver.close()