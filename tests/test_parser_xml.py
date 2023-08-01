# -*- coding: utf-8 -*-
import pytest

import sys

sys.path.insert(0, '../parsinggettingthingsdone')
from parsinggettingthingsdone.parser_xml import TagName

class TestParserXML:
    
    actionTagName = ""
    projectTagName = ""
    projectsTagName = ""

    def test_parserxml_lambda_list(self):
        jobs = ["engineer","teacher","doctor"]
        for x in range(len(jobs)):
            assert (jobs[x] != "unkown")

#    def startElement(self, tagName, attrs):
    
#  def endElement(self, tagName):

    @pytest.fixture
    def data_action(self):
        self.actionTagName = TagName("action")
        self.projectTagName = TagName("project")
        self.projectsTagName = TagName("projects")

            
    def test_tag_name_isAction(self, data_action):
        assert True == self.actionTagName.isAction()
    
    def test_tag_name_isProject(self, data_action):
        assert  True == self.projectTagName.isProject()
    
    def test_tag_name_isEndFile(self, data_action):
        assert  True == self.projectsTagName.isEndFile()
