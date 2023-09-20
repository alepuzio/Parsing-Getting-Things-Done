# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 14:44:50 2023

@author: Alessandro
"""
"""TODO cambiare nome da physical in input o read"""

import logging
import os
from formatter import Next_Action_CSV
from parser_xml import MyHandler


class Directory:
    """ 
    Class of the directory to read
    """
    def __init__(self, new_complete_path):
        self.complete_path = new_complete_path
    
    def xml(self):
        """Return the list of the content of XML files"""
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
        """
        Create the file on the filesystem
        """        
        logging.debug("self.csv.name():"+self.csv.name())
        report_name = "".join([ self.directory(), os.sep, self.csv.name() ]);
        if (os.path.exists(report_name)) :
            os.remove(report_name)	
        return report_name
    
    
    def next_actions_file(self):
        """write (updating, if it exists) the physical file in the hard disk"""
        f = open(self.file(), "a")
        row_list = self.csv.row()
        if not row_list:
            f.write(" ".join( ["No project","has any Next Action","\n"] ))
        else:
            f.write(";".join ( ["Area","Project", "Goal", "Work To Do [%]","NextAction","Context", "Blocked by","\n"]) )
            for areas in row_list:
                for project_next_Action in areas:
                    f.write("".join([(
                        Next_Action_CSV(project_next_Action).data()), "\n" ]))
        f.close()
        
    def next_actions_console(self):
           """
           write the data int the console
           """
           row_list = self.csv.row()
           if not row_list:
               logging.debug(" ".join( ["Every project","has no Next Action","\n"] ))
           else:
               counter = 0
               logging.debug(";".join ( ["Project", "NextAction","Context", "Estimated Time","To finish before","Blocked by","\n"]) )
               for areas in row_list:
                   for project_next_Action in areas:
                       counter = counter +1
                       logging.debug("".join([ str(counter) ,">", (project_next_Action.data()), "\n" ]))
        
    def project_console(self):
            """
            write the data in the console
            """
            row_list = self.csv.row()
            if not row_list:
                logging.debug(" ".join( ["Every project","has no Next Action","\n"] ))
            else:
                counter = 0
                logging.debug(";".join ( ["Area","Project", "Goal", "Work To Do [%]","NextAction","Importance","\n"]) )
                for areas in row_list:
                    for project_next_Action in areas:
                        counter = counter +1
                        logging.debug("".join([ str(counter) ,">", (project_next_Action.data()), "\n" ]))
            
              
        
        
    def context(self):
         """
         write (updating, if it exists) 
         the physical file 
         in the hard disk"""
         report_name = "".join([ self.directory(), os.sep, self.csv.name() ]);
         if (os.path.exists(report_name)) :
             os.remove(report_name)	
             f = open(report_name, "a")
         row_list = self.csv.row()
         if not row_list:
             f.write(" ".join( ["Every project","has no Next Action","\n"] ))
         else:
             f.write(";".join ( ["Important","To finish before","Area","Project", "Goal", "Work To Do [%]","NextAction","\n"]) )
             for areas in row_list:
                 for project_next_Action in areas:
                     f.write("".join([project_next_Action.data(), "\n" ]))
         f.close()
        