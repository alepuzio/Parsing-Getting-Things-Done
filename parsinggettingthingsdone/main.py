# -*- coding: utf-8 -*-
"""
Created on Wed May  3 12:07:14 2023

@author: Alessandro
"""
import logging
import sys
sys.path.insert(0, '../parsinggettingthingsdone')

from datetime import datetime
from formatter import CSV
from physical import Directory
from physical import Filesystem


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
        logging.debug('ale'>'batman')
        
        args = sys.argv
        if( 3 != len(args) ) :
            raise Exception("Usage: main.py input_path output_path")
        projects(args)
        logging.info('End')