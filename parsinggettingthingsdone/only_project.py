# -*- coding: utf-8 -*
from datetime import date
from datetime import datetime  
import logging

class OnlyProject:
    """
    Class about a Project,
    declared as a sequence of more steps direct to a goal.
    This class has'nt the list of Action
    """
    def __init__(self, new_name, new_important , new_closed, 
                 new_start = '', new_depends = '', new_area = '',
                 new_due = '', new_goal =''):
        self.name = new_name
        self.important = new_important
        self.closed_in = new_closed
        self.start = new_start
        self.depends = new_depends
        self.area = new_area
        self.due = new_due
        self.goal = new_goal
        
    def __eq__(self, other): 
        """Return True if the OnlyProject have the same name."""
        if not isinstance(other, OnlyProject):
            # don't attempt to compare against unrelated types
            return NotImplemented
        return self.name == other.name 

    def __lt__(self, other): 
        """Return True if the OnlyProject has a minor name than other."""
        return self.name < other.name 
    
    def __str__(self):
        """Return the OnlyProject as uppercase string"""
        return self.name
    

  
    class Project_Csv:
        """
        Class about a single row in the Project file
        """
        
        def __init__(self, new_project):
            self.project = new_project
            
        def data(self):
            """Return the name with no \r, \t or \n"""
            data_project = None
            if("" != self.project.closed_in.strip()):
                data_project = " ".join([
                    "["
                    , self.project.closed_in 
                    , "]"
                    , self.project.name
                    , "Choose another Project"
                    ])
            else:
                data_project = ";".join([self.project.important
                                     , self.project.end
                                     , self.project.name
                                    ,  self.project.goal
                                  
                                    ] )
            logging.warn("data_project.data:" + data_project )
            return data_project.strip()

    class  Depends:
        
        def __init__(self, new_only_project ):
            self.only_project = new_only_project
        
        def list_comma(self):
            """
            Return the optional list of blocking actrivities or projects.
            """
            pass

        
    class Important:
        """
        Class describe the importance of a project
        """
        
        def __init__(self, new_only_project):
            self.only_project = new_only_project
            
        
        def mark(self):
            """
            Return the string that indicates this project as Important in the CSV row
            """
            pass
        
    class Date:
    
            
        def __init__(self, new_date):
            self.date = new_date
        
        
        def y_m_d(self):
            """
            Return the optional start date in the CSV row in format Y-m-d.
            """
            res =  ""
            if "" != str(self.date):
                res = datetime.strptime(self.date, '%Y-%m-%d').strftime('%Y-%m-%d')
            return res
   
    class Goal:
        """
        Goal of a project
        """
        def __init__(self, new_only_project):
            self.only_project = new_only_project
        
        def string(self):
            """
            Return the optional goal of the project in the CSV row 
            """
            pass
        
    class ProjectName:
        """
        Elaborate the name of the project in natural language
        """
        def __init__(self, new_only_project):
            self.original_name = new_only_project.name
            self.area = new_only_project.area
           
        
        def name(self):
            """Return the name of the Project for the CSV report"""
            return ";".join([self.area, self.original_name.title()])
        
        def __str__(self):
            return "".join(["ProjectName:", self.original_name])
        
        def __repr__(self):
            return self.original_name                            