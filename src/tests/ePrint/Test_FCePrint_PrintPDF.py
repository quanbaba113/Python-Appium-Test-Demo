

import unittest
import sys

sys.path.append('/home/ubuntu/workspace/ePrint-Demo')

from src.base.EPrintApp import ePrint
from src.base.Gmail import gmail

printIp = sys.argv[1]
pdfName = sys.argv[2]

ePrint = ePrint()
ePrint.openApp()
# go to welcome page
ePrint.verifyIsShown("skipButton")
# click skip button
ePrint.clickOn("skipButton")

ePrint.verifyIsShown("done")
ePrint.clickOn("done")
ePrint.verifyIsShown("gotIt")
ePrint.clickOn("gotIt")
# verify all elements on the ePrint home page.
ePrint.verifyIsShown("HPePrint")
ePrint.verifyIsShown("notifications")
ePrint.verifyIsShown("settings")
ePrint.verifyIsShown("photosImg")
ePrint.verifyIsShown("filesImg")
ePrint.verifyIsShown("webImg")
ePrint.verifyIsShown("emailImg")
ePrint.verifyIsShown("photosText")
ePrint.verifyIsShown("filesText")
ePrint.verifyIsShown("webText")
ePrint.verifyIsShown("emailText")

ePrint.clickOn("filesImg")
#ePrint.waitForTimeOut(3000)
ePrint.verifyIsShown("searchFile")
ePrint.verifyIsShown("deviceStorage")
ePrint.verifyIsShown("pdfs")
ePrint.verifyIsShown("ppts")

ePrint.loadingFiles(120)
ePrint.clickOn("pdfs")

ePrint.verifyIsShown("back")
ePrint.verifyIsShown("pdfText")
ePrint.verifyIsShown("firstPdfImg")

ePrint.verifyIsShown("firstPdfName")
#ePrint.verifyIsShown("allPDFName","0-blank.pdf")
#ePrint.clickOn("allPDFName","0-blank.pdf")

ePrint.verifyIsShown("allPDFName",pdfName)
ePrint.clickOn("allPDFName",pdfName)

ePrint.waitForTimeOut(2)
ePrint.tap(0.5,0.5)

ePrint.verifyIsShown("print")
ePrint.clickOn("print")
ePrint._waitByTimeOut(2)
ePrint.tap(0.5,0.5)
ePrint.verifyIsShown("addPirnt")
ePrint.clickOn("addPirnt")

ePrint.verifyIsShown("printertxtsearch")
ePrint.verifyIsShown("addButton")
#ePrint.setValueTo("printertxtsearch","10.10.60.53")
ePrint.setValueTo("printertxtsearch",printIp)
ePrint.clickOn("addButton")

ePrint.verifyIsNotShown("pleaseWait")
if ePrint._waitForElement("useButton",10):
    ePrint.clickOn("useButton")
else:
    ePrint.setPage("previewPage")
ePrint.verifyIsShown("print")
printTime = ePrint.getPrintTime()
# verify  print result
ePrint.setPage("homePage")
ePrint.verifyIsShown("notifications")
ePrint.clickOn("notifications")
ePrint.verifyIsShown("back")
ePrint.verifyIsShown("pdfName")
ePrint.verifyIsShown("message")
ePrint.verifyIsShown("printedMsg")
ePrint.verifyIsShown("where")
ePrint.verifyIsShown("printName")
ePrint.verifyIsShown("printIp")
ePrint.verifyIsShown("removeNotiflcation")

ePrint.clickOn("back")
ePrint.verifyIsShown("notiflcations")
ePrint.verifyIsShown("done")
ePrint.verifyIsShown("printFileName")
ePrint.verifyIsShown("printStatus")
ePrint.verifyIsShown("time")
ePrint.clickOn("done")
ePrint.log("Pint Completed")
ePrint.log(str(pdfName) + "   -----   " + str(printTime))
ePrint.quit()

