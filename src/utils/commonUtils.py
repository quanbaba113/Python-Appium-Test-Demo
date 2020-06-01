

import sys
import os

import codecs
from configparser import ConfigParser
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__),p)
)


class Common():
    def getRoot(self):
         rootPath_ = os.getcwd()+os.sep
         print(rootPath_)
         return rootPath_

    @staticmethod
    def configParser(path):
        try:
            conf = ConfigParser()
            conf.read(path,"utf-8")
            return conf
        except FileNotFoundError as e:
            raise Exception("解析文件失败")

    @staticmethod
    def getSection(conf):
        return conf.sections()


    @staticmethod
    def getMainValue(mainConf,section,key):
        return mainConf.get(section,key)

    @staticmethod
    def getTree(xml_path):
        tree = ET.parse(xml_path)
        return tree

    @staticmethod
    def getRootElement(tree):
        return tree.getroot()

    @staticmethod
    def getTagName(element):
        return element.tag

    @staticmethod
    def getAttribute(element):
        return element.attrib

    @staticmethod
    def getEelements(element,xpath):
        return element.findall(xpath)

    @staticmethod
    def getElementByXpath(root,xpath):
        """Find all matching subelements by tag name or path.

        *path* is a string having either an element tag or an XPath,
        *namespaces* is an optional mapping from namespace prefix to full name.

        Returns list containing all matching elements in document order.

        """

        list = root.findall(xpath)

        if len(list) > 1:
            print("存在相同节点")
        else:
            return list[0]

    @staticmethod
    def getEelmentText(element):
        return element.text


'''config = Common.configParser("D:/localGit/repositories/Python/ePint-Demo/resources/conf/main.conf")
value = config.get("ePrint","conf.ePrint.Android")
print(value)
tree = Common.getTree("D:/localGit/repositories/Python/ePint-Demo/resources/conf/ePrint/ui/Android/ePrint.xml")
root = Common.getRootElement(tree)
list = Common.getElementByXpath(root,".//AppName")
print(list.text)'''
'''
for index in range(len(list)):
    element = list[index]
    name = element.get("name")
    type = element.get("type")
    value = element.get("value")
    print(name)
    print(type)
    print(value)'''

'''tree = Common.getTree("D:/localGit/repositories/Python/ePint-Demo/resources/conf/ePrint/ui/Android/ePrint.xml")
root = Common.getRootElement(tree)
list = Common.getEelements(root,".//page[@name='登录页面2']/element")
print(len(list))'''