# -*- coding: utf-8 -*
from datetime import datetime    
from datetime import date
import logging

class Project:
    """  Class about a Project,
    declared as a sequence of more steps direct to a goal.
    """
    def __init__(self, new_name, new_important , new_closed, new_list_actions, 
                 new_start = '', new_depends = '', new_area = '',
                 new_due = '', new_goal =''):
        self.name = new_name
        self.important = new_important
        self.closed = new_closed
        self.list_actions = new_list_actions
        self.start = new_start
        self.depends = new_depends
        self.area = new_area
        self.due = new_due
        self.goal = new_goal
        
    def nextAction(self):
        """ Return
        ----------
        the Next Actions.           
        """
        result = []
        if("" != self.start ):
            logging.debug("start:"
                          + self.start_formatted() > date.today().strftime('%Y-%m-%d')
                          + ">"+self.start_formatted()
                          + ">>"+date.today().strftime('%Y-%m-%d')
                          )
            result.append(Action( "".join(["This project will start in ", self.start_formatted() ]), 1))
        elif (0 < len(self.depends) ) :
            result.append(
                Action(" ".join(["This project is blocked by ", self.depends_formatted() ]), 1)
                          )
            #logging.debug(result[0])
        else:
            result = [ x  for x in self.list_actions if x.isNextAction ()]         
            numberNA = len(result)
            if (0 == numberNA ) :
                result.append(Action( "This project has not any Action", 1))
            elif (1 < numberNA):
                result.append(  Action (" ".join(['This project has ', str(numberNA) ,'Next Action: it has to be fixed']),1))
            #else:
             #   logging.debug("This project has 1 NA")
        if("" != self.due ):
            logging.debug("due:"
                          + self.start_formatted() > date.today().strftime('%Y-%m-%d')
                          + ">"+self.start_formatted()
                          + ">>"+date.today().strftime('%Y-%m-%d')
                          )
            result[0] =  Action (" ".join( [result[0].data(), " before ", str(self.due)]), 1)
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
        - The life area of the project, if existing
        - Total number of the actions of the project

        """
        return ";".join([ self.important_mark(), self.closed_formatted(), self.due,  ProjectName(
            self.name, self.area).name(), self.goal_formatted(), self.progress_formatted()])
    
    
    def progress_formatted(self):
        """
        Return the percentage of the work to do
        """
        closed = [ x  for x in self.list_actions if x.closed ]   
        total = len(self.list_actions);
        if 0 == total:
            res = 100.0
        else:
            res = ((total - len(closed))/total)*100
            #logging.debug("progress("+str(total)+","+str(len(closed))+","+str((total - len(closed)))+"):" + str(res))
        return str(res)

    def important_mark(self):
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
    
    def closed_formatted(self):
        """
        Return the optional finish date in the CSV row in format Y-m-d.
        """
        res =  ""
        if "" != str(self.closed):
            res = datetime.strptime(self.closed, '%Y-%m-%d').strftime('%Y-%m-%d')
        return res 

    def depends_formatted(self):
        """
        Return the optional list of projects  date in the CSV row in format Y-m-d.
        """
        res =  ""
        if "" != str(self.depends):
            list_depends = self.depends.split(", ")
            res = " , ".join(list_depends)
        return res.upper()

    
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


    def goal_formatted(self):
        """
        Return the optional goal of the project in the CSV row 
        """
        res =  ""
        if "" != self.goal:
            res = "".join(["per ", self.goal])
        return res 
    
            
class Action:
    """
    Class about a general Single Action.
    """
    
    def __init__(self, new_name, new_position, new_closed = '', 
                 new_context = '',
                 new_estimation ='',
                 new_depends ='',
                 new_end = ''):
        self.name = new_name
        self.position = new_position
        self.closed = new_closed
        self.context = new_context
        self.estimation = new_estimation
        self.depends = new_depends
        self.end = new_end

    def end_formatted(self):
        """
        Return the optional end date in the CSV row in format Y-m-d.
        """
        res =  ""
        if "" != str(self.end):
            res = "".join([
                " entro il "
                , datetime.strptime(self.end, '%Y-%m-%d').strftime('%Y-%m-%d')
                ])
        return res 
        
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
        data_action = None
        list_context = []
        if("" != self.closed.replace(" ", "")):
            data_action = " ".join(["[", self.closed ,"]", self.name, "choose another NA"])
        elif("" != self.context.replace(" ", "")):
            list_context = self.context.split(",")
        
        data_action = " ".join([self.name + self.end_formatted(), 
                                ";", self.end, 
                                ";" , ";".join(list_context),
                               ";", self.depends_formatted()])
        return data_action.replace("\r","").replace("\t","").replace("\n","")

    def depends_formatted(self):
        """
        Return the optional list of projects  date in the CSV row in format Y-m-d.
        """
        res =  ""
        if "" != str(self.depends):
            list_depends = self.depends.split(", ")
            res = " , ".join(list_depends)
        return res.upper()

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
