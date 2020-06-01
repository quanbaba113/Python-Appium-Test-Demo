
#coding=utf-8
import os
import logging
import logging.config
from src.utils.commonUtils import Common
from time import sleep
from abc import ABCMeta,abstractmethod

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class InitializeFramework(object):

    #__mainConfigFileName = os.environ("AutoConfigFile")
    # 定义字典保存 当前page 所有的element
    # 保存结构 {key(name):value(key(type):value(id),key(value):value(com.beyondsoft.ep2p.home)
    #elements = {"test":"test"}
    def __init__(self, IndicatedSutFileName = None):
        #定义全局变量
        # 当前测试类型, web ios android
        self._appType = self.getAppType()
        # 当前app 名字
        self._appName = self.getAppName()

        self._resourcesFile = PATH("../../../resources")
        self._dataFile = self._resourcesFile+"/data"
        self._confFile = self._resourcesFile+"/conf"
        self.logger = None
        # 保存所有main.conf 所有的信息
        self._mainConfig = None
        # 保存sut 文件所有的信息
        self._sutConfig = None
        # 保存xml 结构
        self._xmlTree = None
        #定义节点对应的element对象
        self._root = None
        #XML 默认配置的page
        self._DefaultPage = None
        # 全局变量 current page 当前所在的page 页面
        self._CurrentPage = None

        self._elements = None
        # 默认元素等待超时时间
        self._elementTimeOut = None
        self.__initializeLogging()
        self.__framework(IndicatedSutFileName)
        self.__getConfigurationParameters()

    def __initializeLogging(self):
        logging.config.fileConfig(self._confFile + "/log.conf")  # 采用配置文件
        # create logger
        self.logger = logging.getLogger("simpleExample")


    def __framework(self , IndicatedSutFileName):
        # 判断conf是否为空,如果为空解析main.conf 来读取相应的配置信息.
        # 读取方式 resources/conf/main.conf , Section=sut, key =conf._appName._appType
        self._mainConfig = self.__getConfigFormatData(self._confFile + "/main.conf")
        self._projectLevelSutConfigPath = self._confFile+"/" + self._appName + "/sut"
        self._sutFileName = self.__defaultIfEmpty(IndicatedSutFileName, self.__getDefaultSutFileName())

        self._sutConfig = self.__getConfigFormatData(self._projectLevelSutConfigPath + "/" + self._sutFileName)


    # 读取配置文件(conf, xml)数据
    def __getConfigurationParameters(self):
        # 获取xml路径
        self._projectLevelUiPath = self._confFile + "/" + self._appName+"/ui"
        self._uiPath = self._projectLevelUiPath + "/" + self._appType + "/" + self._getSutFullFileName("app."+self._appName +"."+ self._appType+".ui")
        self._xmlTree = Common.getTree(self._uiPath)
        self._root = Common.getRootElement(self._xmlTree)
        self._elementTimeOut = self._getSutFullFileName("test.timeout.element")
        self._getAppInfo()

    def _getAppInfo(self):

        self._DefaultPage = Common.getEelmentText(Common.getElementByXpath(self._root,".//DefaultPage"))
        self.__AppName = Common.getEelmentText(Common.getElementByXpath(self._root,".//AppName"))
        self.__Version = Common.getEelmentText(Common.getElementByXpath(self._root,".//Version"))
        self.__Environment = Common.getEelmentText(Common.getElementByXpath(self._root,".//Environment"))
        self.__TestCategory = Common.getEelmentText(Common.getElementByXpath(self._root,".//TestCategory"))
        self.__NetWork = Common.getEelmentText(Common.getElementByXpath(self._root,".//NetWork"))
        self.__Description = Common.getEelmentText(Common.getElementByXpath(self._root,".//Description"))

        self.log("Default Page : " + self._DefaultPage)
        self.log("App Name : " + self.__AppName)
        self.log("App Version : " + self.__Version)
        self.log("Test Environment : "+ self.__Environment)
        self.log(self.__TestCategory)
        self.log("Test NewWork : " + self.__NetWork)
        self.log("Description : " + self.__Description)


    def __getConfigFormatData(self,configFileName):
        return Common.configParser(configFileName)

    # 获取main.conf 当前测试appName 节点下的值
    def _getAppMainConfig(self, key):
        return self._mainConfig.get(self._appName, key)

    # 获取main.conf default 节点下面的值
    def _getDefaultMainConfig(self, key):
        return self._mainConfig.get("defaule", key)

    # 获取sut 文件里面的值
    def _getSutFullFileName(self,key):
        try:
             return self._sutConfig.get("sut",key)
        except Exception as e:
             self.log("get value failed.")
             return ""

    def __getDefaultSutFileName(self):
        coreFileKey = ("conf."+self._appName+"."+self._appType+".file")
        rtn = self._getAppMainConfig(coreFileKey)
        if rtn == "":
            raise Exception("!Warning: can't find any key " + coreFileKey + " in the initial config file. ")
        return rtn

    def __defaultIfEmpty(self,str,defaultStr):
        if str == "" or str == None:
            return defaultStr
        else:
            return str

    @abstractmethod
    def getAppType(self):
        pass

    @abstractmethod
    def getAppName(self):
        pass

    # Wait for time out
    # timeOut Second
    def waitForTimeOut(self,time):
        try:
            sleep(time)
        except TimeoutError as e:
            print(e)


    def UiMapSetPage(self,page):

        if page == "" or page == None:
            self._CurrentPage = self._DefaultPage
        else:
            self._CurrentPage = page
        self.getUiMap(self._CurrentPage)

    def setPage(self,page):
        self.getUiMap(page)

    def getUiMap(self,page):

        currentElements = {}
        name = ""
        list = Common.getEelements(self._root, ".//page[@name='"+page+"']/element")

        for index in range(len(list)):
            attributes = Common.getAttribute(list[index])
            name = attributes.get("name")
            currentElements[name] = attributes

        print(len(currentElements))
        #print(currentElements)

        if len(list) == len(currentElements):

            #global elements
            self._elements = currentElements
            #print(self.elements.get("手机号码").get("type"))
            #print(self.elements.get("手机号码").get("value"))
            self.log(self._elements)
        else:
            print("page 节点下面存在相同的元素名字")


    def log(self,message,level=1):
        if level == 1:
            self.logger.info(message)
        if level == 2:
            self.logger.warning(message)
        if level == 3:
            self.logger.debug(message)
        if level == 4:
            self.logger.error(message)