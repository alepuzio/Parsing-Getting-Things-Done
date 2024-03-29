# -*- coding: utf-8 -*
from datetime import datetime    
from datetime import date
import logging

class Project:
    """  Class about a Project,
    declared as a sequence of more steps direct to a goal.
    """
    def __init__(self, new_name, new_important , new_closed, new_list_actions, 
                 new_start ):
        self.name = new_name
        self.important = new_important
        self.closed = new_closed
        self.list_actions = new_list_actions
        self.start = new_start
    
    def nextAction(self):
        """ Return
        ----------
        the Next Actions.           
        """
        result = [ x  for x in self.list_actions if x.isNextAction ()]
        numberNA = len(result)
        
        if("" != self.start ):
            logging.debug("start:"
                          + self.start_formatted() > date.today().strftime('%Y-%m-%d')
                          + ">"+self.start_formatted()
                          + ">>"+date.today().strftime('%Y-%m-%d')
                          )
            result.append(Action( "".join(["This project will start in ", self.start_formatted() ]), 1))
            
        elif (0 == numberNA ) :
            result.append(Action( "This project has not any Action", 1))
        elif (1 < numberNA):
            result = []
            result.append(  Action (" ".join(['This project has ', str(numberNA) ,'Next Action: it has to be fixed']),1))
        return result[0] 
        
    def __eq__(self, other): 
        """Return True if the Next Actions have the same name."""
        if not isinstance(other, Project):
            # don't attempt to compare against unrelated types
            return NotImplemented
        return self.name == other.name 

    def __lt__(self, other): 
        """Return True if the Next Actions have the same name."""
        return self.name < other.name 
    
    def __str__(self):
        """Return the Next Action as string"""
        return  "".join([ProjectName(self.name).name() , "[" , str(len(self.list_actions)), "]"])

    def csv(self):
        """Return the Next Action as string for CSV file"""
        return  "".join([ self.project_name(), ";", self.data() ])

    def project_name(self):
        """
        Return name of the of the Project.
        - If it's Important there will be a mark
        - If it's closed there will be the finish date
        """
        return "".join([ self.important_mark(), self.closed_formatted(),  ProjectName(self.name).name()])
    
    def important_mark(self):
        """
        Return the string that indicates this project as Important in the CSV row
        """
        res =  None
        if  ("1" == str(self.important)) :
            res = "! "
        else:
            res = "non importante ["+self.important+"]"
        return res 
    
    def closed_formatted(self):
        """
        Return the optional finish date in the CSV row in format Y-m-d.
        """
        res =  ""
        if "" != str(self.closed):
            res = datetime.strptime(self.closed, '%Y-%m-%d').strftime('%Y-%m-%d')
        return res 
    
    def start_formatted(self):
        """
        Return the optional start date in the CSV row in format Y-m-d.
        """
        res =  ""
        if "" != str(self.start):
            res = datetime.strptime(self.start, '%Y-%m-%d').strftime('%Y-%m-%d')
        return res 
    
    
    def data(self):
        """
        Return the data of the Next Action
        """
        return str(self.nextAction().data())
        
class Action:
    """
    Class about a general Single Action.
    """
    
    def __init__(self, new_name, new_position, new_closed = '', 
                 new_context = '',
                 new_estimation =''):
        self.name = new_name
        self.position = new_position
        self.closed = new_closed
        self.context = new_context
        self.estimation = new_estimation
        #logging.debug("closed " + str(self.closed))
        
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
        true if self is a next action, that is self.position is the lowest and it's not finished. False otherwise
            
        Parameters
        ----------
        self: self
        """
        return (1 == int(self.position) )
    
    def data(self):
        """Return the name with no \r, \t or \n"""
        #logging.debug("".join(["chiuso:[", self.closed, "]"]))
        data_action = ""
        if("" != self.closed.replace(" ", "")):
            data_action = " ".join(["[", self.closed ,"]", self.name, "choose another NA"])
        elif("" != self.context.replace(" ", "")):
            list_context = self.context.split(",")
            data_action = " ".join([self.name, ",",", ".join(list_context)])
        if ("" != self.estimation.replace(" ", "")):
            data_action = " ".join([self.name, "," ,self.estimation , ", ".join(list_context)])
        else:
            data_action = self.name
        return data_action.replace("\r","").replace("\t","").replace("\n","")

    def __eq__(self, other): 
        """Return True if the Actions have the same name"""
        res = False
        if not isinstance(other, Action):
            # don't attempt to compare against unrelated types
            res = NotImplemented
        else :
            res = (self.name == other.name and self.name == other.name) 
        return res
    
    def __str__(self):
        return  " ".join([str(self.position), ">", self.name])
    
    def __repr__(self):
        """Return the representation of the Action for the CSV report"""
        return  " ".join([str(self.position),"[", str(self.closed),"]" , ">>", self.name])
        
class ProjectName:
    """Elaborate the name of the project in natural language"""
    def __init__(self, new_original_name):
        self.original_name = new_original_name
        
    def name2(self):
        length = len("progetto-")
        return self.original_name[length:].replace('-', ' ').title()
    
    def name(self):
        """Return the name of the Project for the CSV report"""
        return self.original_name.title()
    
    def __str__(self):
        return "".join(["ProjectName:", self.original_name])

    def __repr__(self):
        return self.original_name
