# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 12:58:23 2019

@author: higupta
"""

class Automation(object):
    """
    Returns a `````` object with given name.

    """
    def __init__(self, name):
        self.name = name

    def get_details(self):
        "Returns a string containing name of the person"
        return self.name