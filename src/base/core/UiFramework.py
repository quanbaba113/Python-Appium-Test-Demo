

from src.base.core.InitiaFramework import InitializeFramework
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from time import sleep
import time


class UIFramework(InitializeFramework):

    def __init__(self):
        InitializeFramework.__init__(self)
        self._driver = None

    def _getElementLocatorAttributes(self,elementName):

        attributes =  self._elements.get(elementName)
        if attributes == None:
            raise Exception("元素找不到在" + str(self._DefaultPage) + "page.")
        return attributes

    def _getElementType(self, elementName):
        return self._getElementLocatorAttributes(elementName).get("type")

    def _getElementValue(self, elementName):
        return self._getElementLocatorAttributes(elementName).get("value")

    def _getPage(self,elementName):
        return self._getElementLocatorAttributes(elementName).get("page")

    def __verifyIs(self,elementName, timeOut,isShow=True,itMatch=None):

        try:
            WebDriverWait(self._driver,timeOut,).until(
                lambda show:
                       self.isPresent(elementName,itMatch) if isShow else not self.isPresent(elementName,itMatch)
            )
        except TimeoutException:
            self.log("Element is not found in time out 30 seconds.")
            return False

        return True


    def _waitForElement(self,elementName, timeOut):
        try:
            WebDriverWait(self._driver,timeOut,).until(
                lambda the_driver:
                    self.isPresent(elementName)
            )
        except TimeoutException:
            self.log("Element is not found in time out %d seconds." %(timeOut,))
            return False

        return True

    def verifyIsNotShown(self,elementName, itMatch=None):
        self.log("Verify the element name " + elementName +" is not show.")
        returnValue= self.__verifyIs(elementName, 30,False,itMatch)
        if returnValue == True:
            return True
        else:
            raise NoSuchElementException("元素在制定的时间内没有消失")

    def verifyIsShown(self,elementName,itMatch=None):
        self.log("Verify the element name " + elementName + ".")
        returnValue= self.__verifyIs(elementName, 30,True,itMatch)
        if returnValue == True:
            return True
        else:
            raise NoSuchElementException("The element['"+elementName+"'] is not found on the 30'S")

    '''
    ID = "id"
    XPATH = "xpath"
    LINK_TEXT = "link text"
    PARTIAL_LINK_TEXT = "partial link text"
    NAME = "name"
    TAG_NAME = "tag name"
    CLASS_NAME = "class name"
    CSS_SELECTOR = "css selector"
    '''
    def _findElements(self,elementName):

        locatorType = self._getElementType(elementName)
        locatorStr = self._getElementValue(elementName)

        if locatorType == "id":
            return self._driver.find_elements(By.ID,locatorStr)
        elif locatorType == "name":
            return self._driver.find_elements(By.NAME,locatorStr)
        elif locatorType == "xpath":
            return self._driver.find_elements(By.XPATH,locatorStr)
        elif locatorType == "partial link text":
            return self._driver.find_elements(By.PARTIAL_LINK_TEXT,locatorStr)
        elif locatorType == "tag name":
            return self._driver.find_elements(By.TAG_NAME,locatorStr)
        elif locatorType == "class name":
            return self._driver.find_elements(By.CLASS_NAME,locatorStr)
        else:#  locatorType="css selector"
            return self._driver.find_elements(By.CSS_SELECTOR,locatorType)

    def isPresent(self,elementName,itMatch=None):
        try:
            return self.getElement(elementName,itMatch).is_displayed()
        except (IndexError,NoSuchElementException) as e:
            return False

    def clickOn(self, elementName,itMatch=None):
        self.log("Click element name " + elementName+ ".")
        try:
             element = self.getElement(elementName,itMatch)
             if element.is_enabled() == True:
                 element.click()
                 # update ui map
                 page = self._getPage(elementName)
                 if page == "" or page == None:
                     self.log("Page is not change.")
                 else:
                     self.log("Setting page to " + str(page))
                     self.UiMapSetPage(page)
                     self._DefaultPage = page
             else:
                 print("The element name " + elementName +" is not enabled.")
        except NoSuchElementException as e:
            self.log(e)
            raise Exception("Click element name " + elementName + "failed")

    def setValueTo(self, elementName,value, itMatch = None):
         try:
            element = self.getElement(elementName,itMatch)
            elementTagName = self._getElementTagName(element)
            if elementTagName == "input" or "text" or "password" or "email":
                try:
                    element.click()
                    element.clear()
                    element.send_keys(value)
                except WebDriverException:
                    element.send_keys(value)
            elif elementTagName == "select              ":
                select = Select(element)
                select.select_by_visible_text(value)
            elif elementTagName == "checkbox":
                positiveValues = ["y", "yes", "true", "on", "checked"]
                negativeValues = ["n", "no", "false", "off", "unchecked"]
                if positiveValues in value.lower():
                    if not element.is_selected():
                        element.click()
                if negativeValues in value.lower():
                    if element.is_selected():
                        element.click()
            self.log("Value \"" + value + "\" is set for element " + elementName)
         except NoSuchElementException as e:
            self.log("Value \"" + value + "\" is set for element " + elementName)


    def _getElementTagName(self, element):
        # get element tar name
        try:
            elementType = element.tag_name
            try:
                elementType += element.get_attribute("type")
            except NoSuchElementException as e:
                pass

            if elementType in "select":
                elementType = "select"
            elif elementType in "checkbox":
                elementType = "checkbox"
            elif elementType in "input":
                elementType = "input"
            else:
                elementType = "text"
            return elementType
        except Exception as e:
            #raise Exception("get element tag name failed.")
            return "text"

    def getValueOf(self,elementName,itMatch=None,attribute=None,):
        element = self.getElement(elementName,itMatch)
        returnVlaue = ""
        if(self.isPresent(elementName,itMatch)):
            if(attribute == None):
                elementType = self._getElementTagName(element)
                if "input" in elementType:
                    returnVlaue = element.get_attribute("value")
                if "text" in elementType:
                    returnVlaue = element.text
                if "checkbox" in elementType:
                    checkBoxClass = element.get_attribute("class")
                    if "checked" in checkBoxClass:
                        returnVlaue = "checked"
                    else:
                        returnVlaue = "unchecked"
                if "select" in elementType:
                    for index in range(self.getElementSize(elementName)):
                        selectItem =  element.find_elements(By.TAG_NAME("option")).get(index)
                        if selectItem.is_selected():
                            returnVlaue = selectItem.text
                if returnVlaue == None or returnVlaue == "":
                    returnVlaue = element.text
            else:
               returnVlaue =  element.get_attribute(attribute)
        return returnVlaue

    def getElements(self,elementName):
        return self._findElements(elementName)

    def getElementSize(self,elementName):
        return len(self.getElements(elementName))


    def getElement(self,elementName, itMatch = None):
        elements = self.getElements(elementName)
        if itMatch == None:
            if len(elements)!=1:
                raise IndexError("定位符不对,请检查元素名为" + str(elementName) +" 在 "+str(self._DefaultPage) +" page 下.")
            else:
                return elements[0]
        else:
            index = self.__getMatchingIndex(elements,itMatch)
            return elements[index]

    def __getMatchingIndex(self,elements, itMacth):
        index = 0
        if type(itMacth)==str:
            for i, element in enumerate(elements):
                getAttText = element.text
                if itMacth in getAttText:
                    index = i
                    break
        else:
            index = itMacth-1
        return index

    def _waitByTimeOut(self,timeOut):
        sleep(timeOut)

    def getNowTime(self):
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
