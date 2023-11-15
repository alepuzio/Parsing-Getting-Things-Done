# -*- coding: utf-8 -*-
import logging
import sys
import xml.sax

sys.path.insert(0, '../parsinggettingthingsdone')

from only_project import OnlyProject


class MyHandlerProject(xml.sax.handler.ContentHandler):
    """
        This class read, in SAX way, the single XML file where are the data of a project.
    """
    
    def __init__(self):
        """Init method"""
        self.current_project = ""
        self._charBuffer = []
        self.list_project = []
        self.start_prj = ""
        self.closedPrj = ""
        self.closed = ""
        self.estimation = ""
        self.area = ""
        self.depends_prj = ""
        self.due_prj = ""
        self.goal = ""
        #self.list_project = []
        
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
        self.area = f[f.find(start)+len(start):f.rfind(end)]
        logging.info("area:" + self.area )
        xml.sax.parse(f, self)
        return  self.list_project 

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
            self.prj =  OnlyProject(
                 self.current_project
                 , self.important
                 , self.closedProject
                 , self.start_prj
                 , self.depends_prj
                 , self.area
                 , self.due_prj
                 , self.goal
                 );
            logging.debug("onlyProject: " + str(self.prj))
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
          if (0 < len(self.activity.strip()) and "" ==  self.closed.strip() ):
              self.list_project.append(self.prj)
              logging.debug("progetti: " + str(self.list_project))
        elif tag_name.isEndFile():
          logging.debug(" ")
        else:
            logging.warn("")

class TagName:
    """
    This class modelize the name of a tag.
    
    """
    def __init__(self, new_tag_name):
        self.tag_name = new_tag_name
        
  
    
    def isProject(self):
        """Return true if the tag is an Project."""
        logging.debug("isProject:"+ self.tag_name)
        return self.tag_name == 'project'
    
        
    def isEndFile(self):
        """Return true if the tag closes a project file."""
        return self.tag_name == 'projects'
    
        
