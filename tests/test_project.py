# -*- coding: utf-8 -*-
"""

Test Class from module "projects" 
"""

import sys

sys.path.insert(0, '../parsinggettingthingsdone')
#from parsinggettingthingsdone.projects import Action
from projects import Action

from projects import Project
from projects import ImportantProject
import logging

import pytest


class TestProject:
    
    list_actions = []
    
    @pytest.fixture(scope="session")
    def prepare_data(self)    
        action_first = Action("first action", 1)
        action_second = Action("second action" , 2)   
        self.list_actions.append(action_first)
        self.list_actions.append(action_second)
        
        
    def test_project_nextAction(self):
        project_single = Project("project", self.list_actions)
        result = project_single.nextAction()  
        logging.debug("next actions: " + str(result))
        self.list_action = []
        assert result == Action("first action", 1)
    
    def test_project_isImportant(self):
        action_first = Action("first action",1)
        action_second = Action("second action" , 2)
        list_actions = []
        list_actions.append(action_first)
        list_actions.append(action_second)
        project_single = ImportantProject(Project("importantProject", list_actions), 1)
        result = project_single.isImportant()  
        logging.debug("ImportantProject: " + str(result))
        assert result == "! " 


    def test_action_isMoreImportantThan(self):
        action_first = Action("first action",1)
        action_second = Action("second action" , 2)
        res = action_first.isMoreImportantThan(action_second)
        assert (True == res)
    
    def test_isNextAction(self):
        action_first = Action("first action",1)
        res = action_first.isNextAction()
        assert (True == res)
    
    def test_data(self):
        action_first = Action("first action\n\r",1)
        res = action_first.data()
        assert ("first action" == res)
                          
