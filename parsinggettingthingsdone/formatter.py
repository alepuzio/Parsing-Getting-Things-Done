# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 14:44:50 2023

@author: Alessandro
"""
import sys
sys.path.insert(0, '../parsinggettingthingsdone')

from datetime import datetime    
import logging

class Next_Action_CSV:
    """ 
    Class about the data of the CSV file to write.
    """
    def __init__(self, new_date_time_obj, new_list_data):
        self.date_time_obj = new_date_time_obj
        self.list_data_to_print = new_list_data
        
    def row(self):
        """
        Return the built row
        """
        return  [ x  for x in self.list_data_to_print ]
    
    def name(self):
        """
        Return the name of the report file
        """
        return "-".join([self.date_time_obj.strftime("%Y-%m-%d"), "NEXT_ACTION.csv"])
    
    def sort(self):
        """
        Return the ordered rows in alphabetical criteria by
        - area
        - name
        """
        #key=lambda x: x.project_name(), reverse=True
        #logging.debug(str(self.row()))
        return self.row().sort()
    
    
    
class ProjectName:
    """Elaborate the name of the project in natural language"""
    def __init__(self, new_original_name, new_area = ''):
        self.original_name = new_original_name
        self.area = new_area
       

    def name(self):
        """Return the name of the Project for the CSV report"""
        return ";".join([self.area, self.original_name.title()])

    def __str__(self):
        return "".join(["ProjectName:", self.original_name])

    def __repr__(self):
        return self.original_name

class Progress:
    
    def __init__(self, new_list_action):
        self.list_actions = new_list_action
    
    def integer(self):
        """
        Return the percentage of the work to do with no decimal digit
        """
        closed = [ x  for x in self.list_actions if x.closed ]
        total = len(self.list_actions);
        if 0 == total:
            res = 100.0
        else:
            res = round( ((total - len(closed))/total)*100, 1)
        return str(res)
    
    
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
    
class Important:
    
    
    def __init__(self, new_important, new_goal = '', new_closed = ''):
        self.important = new_important
        self.goal= new_goal
        self.closed = new_closed
   
    
    def mark(self):
        """
        Return the string that indicates this project as Important in the CSV row
        """
        res =  None
        if  ("1" == str(self.important) ):
            res = "For me"
            #logging.debug(self.name +" e "+ self.important)
        elif (""!= self.closed.replace(" ","") or ""!= self.goal.replace(" ","")):
            res = "Mandatory"
        else:
            res = ""
        return res
    
    
class  Depends:
    
    def __init__(self, new_depends ):
        self.depends = new_depends
    
    def list_comma(self):
        """
        Return the optional list of blocking actrivities or projects.
        """
        res =  ""
        if "" != str(self.depends):
            list_depends = self.depends.split(", ")
            res = " , ".join(list_depends)
        return res.upper()
    
    
    
class Goal:
    
    def __init__(self, new_goal):
        self.goal = new_goal
    
    def string(self):
        """
        Return the optional goal of the project in the CSV row 
        """
        res =  ""
        if "" != self.goal:
            res = "".join(["for ", self.goal])
        return res 
    
    
class Next_Action_Csv:
    """
    Class about a single row in the NExt Action file
    """
    
    def __init__(self, new_action):
        self.action = new_action
        
    def data(self):
        """Return the name with no \r, \t or \n"""
        data_action = None
        if("" != self.action.closed.replace(" ", "")):
            data_action = " ".join([
                "["
                , self.action.closed 
                , "]"
                , self.action.name, "choose another NA"
                ])
        data_action = ";".join([
                                Important(self.action.prj.important).mark()
                                , Date(self.action.end).y_m_d()
                                , self.action.prj.project_name()
                                ,  Goal(self.action.prj.goal).string()
                                , Progress(self.action.prj.list_actions).integer()
                                , self.action.name
                                , self.action.context
                                , Depends(self.action.depends).list_comma()
                              
                                ] )
        logging.warn("Action.data:" + str(data_action) )
        return data_action.replace("\r","").replace("\t","").replace("\n","")
    
class Project_Csv:
    """
    Class about a single row in the Project file
    """
    
    def __init__(self, new_action):
        self.action = new_action
        
    def data(self):
        """Return the name with no \r, \t or \n"""
        data_action = None
        if("" != self.action.closed.replace(" ", "")):
            data_action = " ".join([
                "["
                , self.action.closed 
                , "]"
                , self.action.name, "choose another NA"
                ])
        data_action = ";".join([
                                Important(self.action.prj.important).mark()
                                , Date(self.action.end).y_m_d()
                                , self.action.prj.project_name()
                                ,  Goal(self.action.prj.goal).string()
                                , Progress(self.action.prj.list_actions).integer()
                                , self.action.name
                                , Depends(self.action.depends).list_comma()
                              
                                ] )
        logging.warn("Project.data:" + str(data_action) )
        return data_action.replace("\r","").replace("\t","").replace("\n","")