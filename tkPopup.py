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
  __masterTK = None
  __top = None

  def __init__(self, masterTK):
    self.__masterTK = masterTK
    self.configureUI()
    
  def configureUI(self):    
    self.__top=tk.Toplevel(self.__masterTK)
    self.e=tk.Entry(self.__top)
    self.e.pack()
    self.b=tk.Button(self.__top,text='Ok',command=self.cleanup)
    self.b.pack()

  def cleanup(self):
    self.value=self.e.get()
    self.__top.destroy()
