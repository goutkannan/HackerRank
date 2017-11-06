"""
Basic principle:
Every piece of code must do one and only one thing.

Let us consider case of Text Parsing, there could be different level of
string based parsing like, look for table, images, strip special char,
 basic regex.

 All these service can be requested by the sender and CoR pattern
 decouples the receiver from the sender.

Usually the references are passed from one service to another till completion.
"""
import re

def regexParser(text):
    return re.findall("\w+",text)

def imgParser(text):
     return text.replace(".img",".txt")

def xmlParser(text):
     return  "Not implemented"

class TextParser():
    def __init__(self,parsers=None):
        self.parsers = []
        for p in parsers:
            self.parsers.append(p)

    def parser(self,text):
        for parse in self.parsers:
            text  = parse(text)
        return  text


text="dfsdsfgsdfdf.imgfgfgdfgwdfg.fng,"
learner = TextParser([regexParser,xmlParser,imgParser])
filteredText = learner.parser(text)


