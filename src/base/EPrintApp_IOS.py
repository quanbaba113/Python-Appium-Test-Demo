# -*- coding: utf-8 -*-
import os
import time

from selenium.common.exceptions import NoSuchElementException
from .fwk.IOSFWK import IOS
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class ePrint_IOS(IOS):

    def __init__(self):
        IOS.__init__(self)

    def getAppName(self):
        return "ePrint"

    def getPrintTime(self):
        beginTime = time.time()
        self.verifyIsShown("printing")
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
