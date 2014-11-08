#!/usr/bin/env python
#title           : inputoverride.py
#description     : This is a file that can be used to override the Sys.stdin
#                : in order to use with TKInter interface
#python_version  : 3.4.1
#=============================================================================
__author__ = "J. Nolan Hager (NHager)"
__email__ = "jeffrey.hager.dev@gmail.com"
__version__ = "1.0.0"

import tkPopup as tkP

class stdin_override(object):
  """
    Redirects the sys.stdin to use a pop up window.
  """
  
  __masterTK = None

  def __init__(self, masterTK):
    super(stdin_override, self).__init__()
    self.__masterTK = masterTK

  def dataEntry(self):
    self.__masterTK.popW = tkP.tkPopUpEntry(self.__masterTK)
    self.__masterTK.wait_window(self.__masterTK.popW)
    print('test')
    return self.getData()

  def getData(self):
    return self.__masterTK.popW.value

  def readline(self):
    return self.dataEntry()
    