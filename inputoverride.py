#!/usr/bin/env python
#title           : inputoverride.py
#description     : This is a file that can be used to override the Sys.stdin
#                : in order to use with TKInter interface
#python_version  : 3.4.1
#=============================================================================
__author__ = "J. Nolan Hager (NHager)"
__email__ = "jeffrey.hager.dev@gmail.com"
__version__ = "1.0.0"

class stdin_override(object):
  """docstring for stdin_override"""
  def __init__(self, master):
    super(stdin_override, self).__init__()
    self.master = master
  def readline(self):
    return "test  output"
    

        
        