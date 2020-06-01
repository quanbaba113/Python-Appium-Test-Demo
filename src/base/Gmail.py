# -*- coding: utf-8 -*-
import os
from .fwk.WebFWK import WebFramework
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class gmail(WebFramework):

    def __init__(self):
        WebFramework.__init__(self)

    def getAppName(self):
        return "gmail"






