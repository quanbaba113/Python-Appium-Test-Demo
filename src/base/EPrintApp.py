# -*- coding: utf-8 -*-
import os
import time
from selenium.common.exceptions import NoSuchElementException
from .fwk.AndroidFWK import Android
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class ePrint(Android):

    def __init__(self):
        Android.__init__(self)

    def getAppName(self):
        return "ePrint"

    def loadingFiles(self,timeOut):
        self.verifyIsShown("loadingFiles",2)
        value = self.getValueOf("loadingFiles",2)
        beginTime = time.time()
        while ("Loading files"  in value):
            endTime = time.time()
            if endTime - beginTime > timeOut:
                self.log("一分钟类文件搜索失败.")
                break
            self._waitByTimeOut(2)
            value = self.getValueOf("loadingFiles",2)

    def getPrintTime(self):
        self.clickOn("printBtn")
        beginTime = time.time()
        self.verifyIsShown("printing")
        self.verifyIsShown("closePrint")
        self.verifyIsShown("hide")
        status = self.getValueOf("printing")
        endTime = 0
        while("Printing" in status or "Sending" in status):
             if self.isPresent("printing"):
                self._waitByTimeOut(1)
                try:
                    status = self.getValueOf("printing")
                except (IndexError,NoSuchElementException,Exception) as e:
                    break
        endTime = time.time()
        return round(endTime - beginTime,1)