# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 14:44:50 2023

@author: Alessandro
"""
import logging
import sys
sys.path.insert(0, '../parsinggettingthingsdone')


class CSV:
    """ 
    Class about the file to write.
    """
    def __init__(self, new_date_time_obj, new_list_data):
        self.date_time_obj = new_date_time_obj
        self.list_data_to_print = new_list_data
        
    def row(self):
        """Return the built row"""
        return  [ x  for x in self.list_data_to_print ]
    
    def name(self):
        """Return the name of the report file"""
        return "-".join([self.date_time_obj.strftime("%Y-%m-%d"), "PROJECTS.csv"])
    
    def sort(self):
        """
        return the ordered rows in alphabetical criteria by
        - area
        - name
        """
        #key=lambda x: x.project_name(), reverse=True
        #logging.debug(str(self.row()))
        return self.row().sort()