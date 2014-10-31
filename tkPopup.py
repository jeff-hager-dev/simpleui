#!/usr/bin/env python
#title           :TkPopUp.py
#description     : A collection of python helprs for dealing with TKinter and
#                :  pop ups.
#usage           :
#python_version  :
#=============================================================================
__author__ = "J. Nolan Hager (NHager)"
__email__ = "jeffrey.hager.dev@gmail.com"
__version__ = "1.0.0"

import tkinter as tk
import sys, os

class tkPopUpEntry(object):
  """
    A basic popup window that a user can enter in a value.
  """
  def __init__(self, master):
    super(tkPopUpEntry, self).__init__()
    self.master = master
    
  def configureUI(self):
    pass