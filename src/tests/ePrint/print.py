import sys
from src.base.Gmail import gmail
from src.base.Outlook import outLook

gmail = gmail()
gmail.log("test")
outLook = outLook()
outLook.log("test")