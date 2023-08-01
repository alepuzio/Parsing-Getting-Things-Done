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
        self._charBuffer = []
        self.list_action = []
        self.list_project = []
        self.priority = -1
        self.activity = ""
        
    def _getCharacterData(self):
        """Read the character"""
        data = ''.join(self._charBuffer).strip()
        self._charBuffer = []
        return data.strip() #remove strip() if whitespace is important

    def parse(self, f):
        """
        Parse the file.
        Returnr the list of project
        """
        xml.sax.parse(f, self)
        return  self.list_project 

    def characters(self, data):
        """Read the characters"""
        self._charBuffer.append(data)
        self.activity = str( self._charBuffer)
        logging.debug("data:"+ self.activity)
        
        
    def startElement(self, tagName, attrs):
        """Read the '<' character.
        It means the there's a new tag.
        """
        tag_name = TagName(tagName)
        if tag_name.isProject():
            logging.debug(" ".join(["apro  isProject:", str(tag_name)]))
        
            self.current_project = attrs['name']
            self.list_action = []
            self.priority  = -1
            self.important = attrs['important'] if 'important' in tagName else ''
            self.closed = attrs['closed'] if 'closed' in tagName else ''
        elif tag_name.isAction():
            self.priority = attrs['number'] if 'number' in tagName else '0'
            self.closed = attrs['closed'] if 'closed' in tagName else ''
            logging.debug(" ".join(["apro  isAction:", str( self.activity)]))
        else:
           logging.warn("".join(["Unkown startElement(", tagName ,")"]))

    def endElement(self, tagName):
        """
        Read the '>' character.
        It means the the current tag is closed
        """
        tag_name = TagName(tagName)
        if tag_name.isProject() : 
            self.list_project.append(
                Project(
                    self.current_project, 
                    self.list_action
                    )
                )
            #self.list_action = []
            logging.debug(" ".join(["chiudo Project:", str(self.list_project)]))
        elif tag_name.isAction():
          logging.debug(" ".join(["1chiudo action:", str(self.list_project)]))
          self.list_action.append( 
                Action(   str(self.activity ), str(  self.priority)   )    
                )
          logging.debug(" ".join(["2chiudo action:", str(self.list_project)]))
        elif tag_name.isEndFile():
          logging.debug(" ".join(["chiudo projects:", str(self.list_project)]))
        
        else:
            logging.warn("".join(["Unkown endElement(", tagName ,")"]))

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
    
        
