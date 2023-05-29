# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from pathlib import Path

import xml.etree.ElementTree as ET

class XML:
    """ File to read"""
    def __init__(self, new_path_single_file):
        """or directory and filename"""
        self.path_single_file = new_path_single_file
    
    def project_data(self):
        """return the data of a Project(name, listactions, etc)"""        
        name = Path(self.path_single_file).stem
       
        tree = ET.parse(self.path_single_file)
        root = tree.getroot() 
        list_action = []
        for child in root:
            if ("action"  == str(child.tag)):	
                list_action.append(  Action(str(child.text), str(child.attrib['number']) ) )
        return Project(name, list_action)
        
        

    
class Project:
    """ A sequence of more steps direct to a goal"""
    def __init__(self, new_name, new_list_actions):
        self.name = new_name
        self.list_actions = new_list_actions
    
    def nextAction(self):
        """
        Return
        ----------
        the Next Actions
               
        """
        result = [ x  for x in self.list_actions if x.isNextAction ()]
        return result[0]
        
    def __eq__(self, other): 
        if not isinstance(other, Project):
            # don't attempt to compare against unrelated types
            return NotImplemented
        return self.name == other.name 
    
    def __str__(self):
        return  ProjectName(self.name).name()  + ";" + str(self.nextAction().data())
    
class Action:
    """Single Action"""
    
    def __init__(self, new_name, new_position):
        self.name = new_name
        self.position = new_position
    
    def isMoreImportantThan(self, a):
        """
    
        Returns
        -------
        true if self is more important then a, that is self.position is lower then a.position. False otherwise
        
        Parameters
        ----------
        a : Action, mandatory
            The Action to compare
        """
        res = False
        if not isinstance(a, Action):
            # don't attempt to compare against unrelated types
            res =  NotImplemented
        else :
            res =  self.position < a.position 
        return res
    def isNextAction(self):
        """
        Returns
        -------
        true if self is a next action, that is self.position is the lowest. False otherwise
            
        Parameters
        ----------
        self: self
        """
        return (1 == int(self.position))
    
    def data(self):
        return  self.name

    def __eq__(self, other): 
        res = False
        if not isinstance(other, Action):
            # don't attempt to compare against unrelated types
            res =  NotImplemented
        else :
            res =  self.name == other.name and self.name == other.name 
        return res
    
    def __str__(self):
        return  str(self.position) + ";" + self.name
    
class ProjectName:
    """Elaborate the name of the project in natural language"""
    def __init__(self, new_original_name):
        self.original_name = new_original_name
        
    def name(self):
        length = len("progetto-")
        return self.original_name[length:].replace('-', ' ').title()