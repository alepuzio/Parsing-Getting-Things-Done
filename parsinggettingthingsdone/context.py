# -*- coding: utf-8 -*-
import datetime

class Context:
    """
    Class about a general Context in a Next Action.
    """
    
    def __init__(self, new_context):
        self.context = new_context

    
    def place(self):
        """
        Return the place where the Action will be executed
        """
        place = ""
        if("@" in self.context):
            place = self.context.replace("@","")
        return place
    
    def date_hour(self):
        """
        Return the estimated time when the Action will be executed
        """
        date_hour = ""
        if("*" in self.context):
            date_hour = datetime.strptime(self.context.replace("*",""), '%Y-%m-%d').strftime('%Y-%m-%d')
        return date_hour

    def temporal_moment(self):
        """
        Return the estimated moment (afternoon, morning, next week, etc) when the Action will be executed
        """
        return None

    def tool(self):
        """
        Return the mandatory tools to do the Action
        """
        return None
        
    def data(self):
        """
        Return the data of the Context
        """
        time = ""
        if ("" == self.temporal_moment()):
            time = self.temporal_moment()
        else:
            time = self.date_hour()
            
        return ";".join[self.place(), time, self.tool()]