# -*- coding: utf-8 -*-
import logging
import sys
import xml.sax

sys.path.insert(0, '../parsinggettingthingsdone')

from projects import Project
from projects import Action


class MyHandler(xml.sax.handler.ContentHandler):
    """
        This class read, in SAX way, the single XML file where are the data of a project.
    """
    
    def __init__(self):
        """Init method"""
        self.current_project = ""
        self._charBuffer = []
        self.list_action = []
        self.list_project = []
        self.activity = ""
        self.start_prj = ""
        self.closedPrj = ""
        self.closed = ""
        self.context  = ""
        self.estimation = ""
        self.area = ""
        self.depends_prj = ""
        self.due_prj = ""
        self.due_action = ""
        self.goal = ""
        
    def _getCharacterData(self):
        """Read the character"""
        data = ''.join(self._charBuffer).strip()
        self._charBuffer = []
        return data.strip() #remove strip() if whitespace is important

    def parse(self, f):
        """
        Parse the file.
        Return the list of project
        """
        start = 'area-'
        end = '.xml'
        self.area = f[f.find(start) + len(start):f.rfind(end)]
        logging.debug("nome area:" + self.area)
        xml.sax.parse(f, self)
        return  self.list_action 

    def characters(self, data):
        """Read the characters"""
        self._charBuffer.append(data)
        self.activity = data
        
    def startElement(self, tagName, attrs):
        """Read the '<' character.
        It means the there's a new tag.
        """
        #logging.debug("startElement")

        tag_name = TagName(tagName)
        if tag_name.isProject():        
            self.current_project = attrs['name']
            self.important = attrs['important'] if 'important' in attrs else ''
            self.closedProject = attrs['closed'] if 'closed' in attrs else ''
            self.start_prj = attrs['start'] if 'start' in attrs else ''
            self.depends_prj = attrs['depends'] if 'depends' in attrs else ''
            self.due_prj = attrs['due'] if 'due' in attrs else ''
            self.goal = attrs['goal'] if 'goal' in attrs else ''
            self.prj =  Project(
                 self.current_project
                 , self.important
                 , self.closedProject
                 , self.list_action
                 , self.start_prj
                 , self.depends_prj
                 , self.area
                 , self.due_prj
                 , self.goal
                 );
        elif tag_name.isAction():
            self.closed = attrs['closed'] if 'closed' in attrs else ''
            self.context = attrs['context'] if 'context' in attrs else ''
            self.estimation = attrs['estimation'] if 'estimation' in attrs else ''
            self.depends = attrs['depends'] if 'depends' in attrs else ''
            self.due_action = attrs['due'] if 'due' in attrs else ''
        else:
           logging.warn("")#.join(["Unkown startElement(", tagName ,")"]))

    def endElement(self, tagName):
        """
        Read the '>' character.
        It means the the current tag is closed
        """
        #logging.debug("endElement")

        tag_name = TagName(tagName)
        if tag_name.isProject() : 
            self.prj = None
        elif tag_name.isAction():
          if (0 < len(self.activity.replace(" ", "")) and "" ==  self.closed.replace("", "" ) ):
              self.list_action.append( Action(  self.activity 
                             , self.prj                                           
                             , self.closed
                             , self.context
                             , self.estimation
                             , self.depends
                             , self.due_action
                             )
                                  )
        elif tag_name.isEndFile():
          logging.debug(" ")#.join(["chiudo projects:", str(self.list_project)]))
        else:
            logging.warn("")#.join(["Unkown endElement(", tagName ,")"]))

class TagName:
    """
    This class modelize the name of a tag.
    
    """
    def __init__(self, new_tag_name):
        self.tag_name = new_tag_name
        
    def isAction(self):
        """Return true if the tag is an Action."""
        return self.tag_name == 'action'
    
    def isProject(self):
        """Return true if the tag is an Project."""
        return self.tag_name == 'project'
    
        
    def isEndFile(self):
        """Return true if the tag closes a project file."""
        return self.tag_name == 'projects'
    
        
