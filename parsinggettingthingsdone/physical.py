# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 14:44:50 2023

@author: Alessandro
"""
"""TODO cambiare nome da physical in input o read"""

import logging
import os

from parser_xml import MyHandler
from formatter import CSV


class Directory:
    """ 
    Class of the directory to read
    """
    def __init__(self, new_complete_path):
        self.complete_path = new_complete_path
    
    def xml(self):
        """Return the list of XML files inside"""
        projectList = []
        for file in os.listdir(self.complete_path):
            if file.endswith(".xml"):
                projectList.append(
                    MyHandler().parse(
                        os.path.join(
                            self.complete_path, file
                            )
                        )
                    )
        #logging.debug("Project's list:" + repr(projectList))
        return projectList

    
class Filesystem:
    """
    Class about the filesystem 
    write to the disk
    """
    
    def __init__(self, new_path_complete_file, new_csv):
        """
        param: new_path_complete_file: directory where wirte the CSV file
        param: new_csv: CSV filename
        """
        self.path_complete_file = new_path_complete_file
        self.csv = new_csv
            
    def directory(self):
        """Make the directory with complete path if not existing"""
        if(not os.path.exists(self.path_complete_file) ):
            logging.debug( " ".join([ "make dir :", self.path_complete_file]))
            os.mkdir(self.path_complete_file)
            logging.debug(" ".join(["Successfull make: ", self.path_complete_file]))
        return self.path_complete_file
    
    def file(self):
        """write (updating, if it exists) the physical file in the hard disk"""
        report_name = "".join([ self.directory(), os.sep, self.csv.name() ]);
        if (os.path.exists(report_name)) :
            os.remove(report_name)	
        f = open(report_name, "a")
        row_list = self.csv.row()
        if not row_list:
            f.write(" ".join( ["Every project","has no Next Action","\n"] ))
        else:
            f.write(";".join ( ["Important","Closed at","To finish before","Area","Project", "Goal", "Work To Do [%]","NextAction","\n"]) )
            for areas in row_list:
                for project_next_Action in areas:
                    f.write("".join([(project_next_Action.csv()), "\n" ]))
        f.close()
        