# -*- coding: utf-8 -*-
import unittest

from parser_xml import TagName

class TestParserXML(unittest.TestCase):
    
    def test_lambda_list(self):
        jobs = ["engineer","teacher","doctor"]
        for x in range(len(jobs)):
            assert (jobs[x] != "unkown")

#    def startElement(self, tagName, attrs):
    
#  def endElement(self, tagName):

class  TestTagName(unittest.TestCase):

            
    def test_isAction(self):
        tagName = TagName("action")
        res = tagName.isAction()
        assert True == res
    
    def test_isProject(self):
        tagName = TagName("project")
        res = tagName.isProject()
        assert  True == res
    
    def test_isEndFile(self):
        tagName = TagName("projects")
        res = tagName.isEndFile()
        assert  True == res
