

import unittest
import sys

sys.path.append('/home/ubuntu/workspace/ePrint-Demo')

from src.base.EPrintApp_IOS import ePrint_IOS
#from src.base.Gmail import gmail

#printIp = sys.argv[1]
#pdfName = sys.argv[2]

ePrint = ePrint_IOS()
ePrint.openApp()

ePrint.verifyIsShown("HPePrint")
ePrint.verifyIsShown("notifications")
ePrint.verifyIsShown("settings")
ePrint.verifyIsShown("photosText")
ePrint.verifyIsShown("emailText")
ePrint.verifyIsShown("webText")
ePrint.verifyIsShown("cloudText")

ePrint.clickOn("photosText")
ePrint.verifyIsShown("blogs")
ePrint.clickOn("blogs")

ePrint.verifyIsShown("firstImage")
ePrint.clickOn("firstImage")


ePrint.verifyIsShown("previewText")
ePrint.verifyIsShown("print")
ePrint.verifyIsShown("printBtn")

ePrint.clickOn("print")

ePrint.verifyIsShown("addPirnt")
ePrint.clickOn("addPirnt")

ePrint.verifyIsShown("printertxtsearch")
ePrint.setValueTo("printertxtsearch","192.168.2.11")

ePrint.verifyIsShown("done")
ePrint.clickOn("done")

if ePrint._waitForElement("addPirnt", 10):
    ePrint.verifyIsShown("back")
    ePrint.clickOn("back")
else:
    ePrint.setPage("previewPage")

ePrint.verifyIsShown("printBtn")
ePrint.verifyIsShown("previewText")
ePrint.verifyIsShown("print")
ePrint.verifyIsShown("printBtn")
ePrint.clickOn("printBtn")

printTime = ePrint.getPrintTime()
ePrint.log("Print completed")
ePrint.close()
print("========================================")
print("Print picture by the time ---  " +str(printTime ) + "s")

