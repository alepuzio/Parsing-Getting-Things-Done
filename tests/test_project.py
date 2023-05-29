# -*- coding: utf-8 -*-
"""
Created on Thu May  4 10:09:37 2023

@author: Alessandro
Test Class from module "projects" 
"""
from projects import Action

from projects import Project
import logging

def test_nextAction():
    action_first = Action("first action",1)
    action_second = Action("second action" , 2)
    list_actions = []
    list_actions.append(action_first)
    list_actions.append(action_second)
    project_single = Project("project", list_actions)
    result = project_single.nextAction()  
    logging.debug("next actions: " + str(result))
    assert result[0] == action_first
    
    

def test_equal_number():
    action_first = Action("first action test_equal_number",1)
    logging.debug("next actions: " + str(action_first))
    assert 1 == action_first.position
    
def test_project_str():
    list_actions = []
    action_first = Action("first test_project_str",1)
    list_actions.append(action_first)
    action_second = Action("second test_project_str", 2)
    list_actions.append(action_second)
    p = Project("project", list_actions)
    logging.debug("Project: " + str(p))
    assert "Progetto:project;first test_project_str" == str(p)