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

import unittest


class TestProject(unittest.TestCase):

    def test_nextAction(self):
        action_first = Action("first action",1)
        action_second = Action("second action" , 2)
        list_actions = []
        list_actions.append(action_first)
        list_actions.append(action_second)
        project_single = Project("project", list_actions)
        result = project_single.nextAction()  
        logging.debug("next actions: " + str(result))
        assert result == action_first
    
class TestImportantProject(unittest.TestCase):

    def test_isImportant(self):
        action_first = Action("first action",1)
        action_second = Action("second action" , 2)
        list_actions = []
        list_actions.append(action_first)
        list_actions.append(action_second)
        project_single = ImportantProject(Project("importantProject", list_actions), 1)
        result = project_single.isImportant()  
        logging.debug("ImportantProject: " + str(result))
        assert result == "! " 

class TestAction(unittest.TestCase):

    def test_isMoreImportantThan(self):
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
                          
