# -*- coding: utf-8 -*
   
class Project:
    """ 
    Class about a Project,
    declared as a sequence of more steps direct to a goal.
    """
    def __init__(self, new_name, new_list_actions):
        self.name = new_name
        self.list_actions = new_list_actions
    
    def nextAction(self):
        """
        Return
        ----------
        the Next Actions.           
        """
        result = [ x  for x in self.list_actions if x.isNextAction ()]
        numberNA = len(result)
        if (0 == numberNA ) :
            result.append(Action( "This project has not any Action", 1))
        elif (1 < numberNA):
            result = []
            result.append(  Action (" ".join(['Forbitten more than 1 Next Action, there are', str(numberNA) ,'NA']),1))
        return result[0] 
        
    def __eq__(self, other): 
        """Return True if the Next Actions have the same name."""
        if not isinstance(other, Project):
            # don't attempt to compare against unrelated types
            return NotImplemented
        return self.name == other.name 
    
    def __str__(self):
        """Return the Next Action as string"""
        return  "".join([ProjectName(self.name).name() , "[" , str(len(self.list_actions)), "]"])

    def __repr__(self):
        """Return the Next Action as string for CSV file"""
        return  "".join([ProjectName(self.name).name(), ";", str(self.nextAction().data()) ])

class ImportantProject:
    """ 
    Class about the Project with flag 'important'.
    """
    
    def __init__(self, new_project, new_important):
            self.project = new_project
            self.important = new_important

    def isImportant(self):
        """Return True if the Project is important"""
        res = ""
        if  (1 == self.important) :
           res = "! " 
        return res  

    def __repr__(self):
        """Return the important Project as string (begin '1') for CSV file"""
        return  "".join([ str(self.isImportant()) , ProjectName(self.name).name(), ";", str(self.nextAction().data()) ])

        
class Action:
    """
    Class about a general Single Action.
    """
    
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
        """Return the name with no \r, \t or \n"""
        return  self.name.replace("\r","").replace("\t","").replace("\n","")

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
        return  " ".join([str(self.position), ">>", self.name])
    
    def __repr__(self):
        """Return the representation of the Action for the CSV report"""
        return  " ".join([str(self.position), ">", self.name])
        
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
