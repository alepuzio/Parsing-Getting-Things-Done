# -*- coding: utf-8 -*-
"""

Test Class from module "projects" 
"""

import sys

sys.path.insert(0, '../parsinggettingthingsdone')
from parsinggettingthingsdone.projects import Action
#from projects import Action

from parsinggettingthingsdone.projects import Project
from parsinggettingthingsdone.projects import ImportantProject
from parsinggettingthingsdone.projects import ClosedProject
import logging

import pytest


class TestProject:
    
    list_actions = []
    
    @pytest.fixture
    def all_data(self):
        '''
        Function to prepare data used by the tests
        '''
        action_first = Action("first action", 1)
        action_second = Action("second action" , 2)   
        self.list_actions.append(action_first)
        self.list_actions.append(action_second)
            
        
    def test_project_nextAction(self, all_data):
        project_single = Project("project", self.list_actions)
        result = project_single.nextAction()  
        logging.debug("next actions: " + str(result))
        self.list_action = []
        assert result == Action("first action", 1)
    
    def test_project_isImportant(self, all_data):
        project_single = ImportantProject(Project("importantProject", self.list_actions), 1)
        result = project_single.isImportant()  
        logging.debug("ImportantProject: " + str(result))
        assert result == "! " 

    def test_project_closed(self, all_data):
        project_single = Project(Project("ClosedProject", "","2020-09-08",self.list_actions))
        result = project_single.closed()  
        logging.debug("ClosedProject at " + str(result))
        assert result == "2020-09-08" 
        
    def test_action_isMoreImportantThan(self, all_data):
       res =  self.list_actions[0].isMoreImportantThan(self.list_actions[1])
       assert (True == res)
    
    def test_isNextAction(self, all_data):
        res = self.list_actions[0].isNextAction()
        assert (True == res)
    
    def test_data(self):
        res = Action("first action\n\r",1).data()
        assert ("first action" == res)
                          
