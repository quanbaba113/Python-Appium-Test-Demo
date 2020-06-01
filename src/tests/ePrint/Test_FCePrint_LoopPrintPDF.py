

import unittest
import sys

sys.path.append('/home/ubuntu/workspace/ePrint-Demo')

from src.base.Gmail import gmail
from src.base.EPrintApp import ePrint

printIp = sys.argv[1]
pdfName = sys.argv[2]

pdfs = pdfName.split(",")
times = []
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
ePrint._waitByTimeOut(2)
ePrint.clickOn("pdfs")

ePrint.verifyIsShown("back")
ePrint.verifyIsShown("pdfText")
ePrint.verifyIsShown("firstPdfImg")

ePrint.verifyIsShown("firstPdfName")
#ePrint.verifyIsShown("allPDFName","0-blank.pdf")
#ePrint.clickOn("allPDFName","0-blank.pdf")
for i, name in enumerate(pdfs):
    if i ==0:
        ePrint.verifyIsShown("allPDFName",name)
        ePrint.clickOn("allPDFName",name)

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
    else:
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
        ePrint.verifyIsShown("allPDFName",name)
        ePrint.clickOn("allPDFName",name)
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
    ePrint.verifyIsShown("printFileName",i)
    ePrint.verifyIsShown("printStatus",i)
    ePrint.verifyIsShown("time",i)
    ePrint.clickOn("done")
    times.append(printTime)

ePrint.log("Print completed")
print("File Name            time used")
print("==============================")

for i in range(len(pdfs)):
    strName = pdfs[i]
    strTime =str(times[i])

    nameLen = len(strName)
    timeLen = len(strTime)
    if nameLen > 15:
        strName = strName[0:10]+"..."
        nameLen = len(str(strName))
    spanLen = 15 - nameLen
    span = ""
    for k in range(spanLen):
         span +=" "
    timeLen = len((strTime+"s"))
    spanLen = (15 - timeLen-1)
    spanTime = ""
    for j in range(spanLen):
         spanTime +=" "

    print(strName + span+ spanTime + strTime+"s")

ePrint.quit()
