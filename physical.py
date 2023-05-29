# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 14:44:50 2023

@author: Alessandro
"""
"""TODO cambiare nome da physical in input o read"""

from projects import XML
import logging

import os


class Directory:
    """ directory to read"""
    def __init__(self, new_complete_path):
        self.complete_path = new_complete_path
    
        
    def xml(self):
        """return the list of XML files"""
        lista = []
        for file in os.listdir(self.complete_path):
            if file.endswith(".xml"):
                lista.append(XML(os.path.join(self.complete_path, file)).project_data())
        return lista
    

class CSV:
    
    """ File to write"""
    def __init__(self, new_date_time_obj, new_list_data):
        self.date_time_obj = new_date_time_obj
        self.list_data_to_print = new_list_data
        
    def row(self):
        """return the built row: project+next action"""
        return  [ x  for x in self.list_data_to_print ]
    
    def name(self):
        """return the name of the file"""
        timestampStr = self.date_time_obj.strftime("%Y-%m-%d")#-%H%M%S-%f
        return timestampStr + "-PROJECTS.csv"
    
    
class Filesystem:
    """write to the disk"""
    
    def __init__(self, new_path_complete_file, new_csv):
        """or directory and namefile"""
        self.path_complete_file = new_path_complete_file
        self.csv = new_csv
            
    def directory(self):
        """make the directory with complete path if not existing"""
        if(not os.path.exists(self.path_complete_file) ):
            logging.debug("make dir : "+ self.path_complete_file)
            os.mkdir(self.path_complete_file)
            logging.debug("make: "+ self.path_complete_file)
        return self.path_complete_file
    
    def file(self):
        """write the physical file in the hard disk"""
        f = open(self.directory() + os.sep + self.csv.name(), "a")
        lista = self.csv.row()
        f.write("\n".join(str(item) for item in lista))
        f.close()
        
        #logging.debug("str: " + (*lista, sep = "\n"))
