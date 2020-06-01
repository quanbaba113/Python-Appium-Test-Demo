

import sys
from src.base.EPrintApp import ePrint
from src.base.Outlook import outLook
ePrint = ePrint()
ePrint.openApp()
username = ePrint._getSutFullFileName("app.outlook.userName")
# go to welcome page
ePrint.verifyIsShown("welcomeTitle")
ePrint.verifyIsShown("HPePrint")
ePrint.verifyIsShown("skipButton")
ePrint.verifyIsShown("activated")
ePrint.clickOn("activated")

ePrint.verifyIsShown("activateText")
ePrint.verifyIsShown("activateButton")
ePrint.verifyIsShown("email")
ePrint.setValueTo("email",username)
ePrint.clickOn("activateButton")

ePrint.log(ePrint.getNowTime())
ePrint.waitForTimeOut(4)
ePrint.verifyIsShown("alertTitle")
ePrint.verifyIsShown("message")
alertTitle = ePrint.getValueOf("alertTitle")
ePrint.log(alertTitle)
while ("Activation Code Sent" not in alertTitle):
    ePrint._waitByTimeOut(1)
    alertTitle = ePrint.getValueOf("alertTitle")
#ePrint.tap(0.5, 0.7)
ePrint.back()
ePrint.verifyIsShown("activateText")
ePrint.verifyIsShown("activateButton")
ePrint.verifyIsShown("codeText")

outlook = outLook()
outlook.openApp()
# get username and password
username = outlook._getSutFullFileName("app.outlook.userName")
password = outlook._getSutFullFileName("app.outlook.password")
outlook.verifyIsShown("logo")
outlook.verifyIsShown("email")
outlook.verifyIsShown("password")
outlook.verifyIsShown("loginButton")
outlook.setValueTo("email",username)
outlook.setValueTo("password",password)
outlook.clickOn("loginButton")
outlook.waitForTimeOut(10)
outlook.verifyIsShown("outlookMail")
outlook.verifyIsShown("newEmail")
outlook.verifyIsShown("time")
time = outlook.getValueOf("time")

outlook.clickOn("newEmail")

outlook.verifyIsShown("title")
pincode = outlook.getcode()
outlook.log(time)
outlook.log(pincode)

ePrint.setValueTo("codeText",pincode)
ePrint.clickOn("activateButton")
ePrint.setPage("registerSuccess")
ePrint.verifyIsShown("done")
ePrint.clickOn("done")
ePrint.verifyIsShown("usage")
ePrint.verifyIsShown("usageDonw")
ePrint.clickOn("usageDonw")
ePrint.verifyIsShown("gotIt")
ePrint.clickOn("gotIt")
ePrint.waitForTimeOut(5)
outlook.close()
ePrint.quit()