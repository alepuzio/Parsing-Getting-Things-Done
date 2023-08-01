# -*- coding: utf-8 -*-
import pytest

import sys

sys.path.insert(0, '../parsinggettingthingsdone')
from parser_xml import TagName

class TestParserXML:
    
    def test_parserxml_lambda_list(self):
        jobs = ["engineer","teacher","doctor"]
        for x in range(len(jobs)):
            assert (jobs[x] != "unkown")

#    def startElement(self, tagName, attrs):
    
#  def endElement(self, tagName):

            
    def test_tag_name_isAction(self):
        tagName = TagName("action")
        res = tagName.isAction()
        assert True == res
    
    def test_tag_name_isProject(self):
        tagName = TagName("project")
        res = tagName.isProject()
        assert  True == res
    
    def test_tag_name_isEndFile(self):
        tagName = TagName("projects")
        res = tagName.isEndFile()
        assert  True == res
