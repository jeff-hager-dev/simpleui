#!/usr/bin/env python
#title           :
#description     :
#usage           :
#python_version  :
#=============================================================================
__author__ = "J. Nolan Hager (NHager)"
__email__ = "jeffrey.hager.dev@gmail.com"
__version__ = "1.0.0"

import tkinter as tk
import sys, os

class overrideStdOut(object):
  def __init__(self, widget, tag='stdout'):
    self.widget = widget
    self.tag = tag
    
  def write(self, text):
    self.widget.configure(state='normal')
    self.widget.insert('end', text, (self.tag)) 
    self.widget.configure(state='disabled')   

  def flush(self):
    pass

  def errors(self):
    pass

  def encoding(self):
    pass