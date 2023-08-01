# -*- coding: utf-8 -*-
"""
Created on Wed May  3 12:07:14 2023

@author: Alessandro
"""
import sys
from physical import Directory
from physical import CSV
from physical import Filesystem
from datetime import datetime
import logging

class Main:
    """Main class"""
    
        
    def projects(args):
        """Return the list of projects and Next Action"""
        Filesystem( args[2], 
                   CSV (
                       datetime.now(), 
                       Directory( args[1] ).xml() 
                       )
                   ).file()
        
        
    if __name__ == '__main__':
        """Run elaboration"""
        logging.basicConfig(level=logging.DEBUG)
        logging.debug('Begin')
        args = sys.argv
        if( 3 != len(args) ) :
            raise Exception("Usage: main.py input_path output_path")
        projects(args)
        logging.info('End')