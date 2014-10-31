#!/usr/bin/env python
#title           : Simple UI
#description     : A really simple wrapper for the python terminal
#python_version  : 3.4.1
#=============================================================================
__author__ = "J. Nolan Hager (NHager)"
__email__ = "jeffrey.hager.dev@gmail.com"
__version__ = "1.0.0"


import tkinter as tk
import sys, os
import inputoverride as inputOR
import outputoverride as outputOR

        
class wrapCLI(tk.Tk):
  """
    SimpleUI is a quick and dirty wrapper for the pythion terminal. Basically
    when you create an instance of this class and pass in a method it will
    run that function upon hitting start and 
  """
  def __init__(self, userMethod):
    super(wrapCLI, self).__init__()
    self.userMethod = userMethod
    self.configToolBar()
    self.configTxtArea()
    self.redirectInput()
    self.redirectOutput()
    #end __init__
  
  def configToolBar(self):
    toolbar = tk.Frame(self)
    toolbar.pack(side='top', fill='x')
    
    fnMethodBtn = tk.Button(self, text='Run Method', command=self.ExecuteUserMethod)
    fnMethodBtn.pack(in_=toolbar, side='left')

    quitBtn = tk.Button(self, text='Quit', command=self.exitProgram)
    quitBtn.pack(in_=toolbar, side='right')
  
  def configTxtArea(self):  
    self.text = tk.Text(self, wrap='word',bg='black', height= 10, fg='green', relief=tk.SUNKEN, yscrollcommand='TRUE')
    self.text.pack(side='top', fill='both', expand=True)
    #Configure tag colors
    self.text.tag_configure('stderr', foreground='#FF0000')
    self.text.tag_configure('stdout', foreground='#008000')
    self.text.tag_configure('input', foreground='#008000')
  
  def redirectOutput(self):
    sys.stdout = outputOR.overrideStdOut(self.text, 'stdout')    
    sys.stderr = outputOR.overrideStdOut(self.text, 'stderr')
  
  def redirectInput(self): 
    sys.stdin = inputOR.stdin_override(self)

  def exitProgram(self):
    self.destroy()

  def methodDetails(self):
    return "TODO Implement"

  def ExecuteUserMethod(self):
    print(self.methodDetails())
    print('Wrapping CLI for '+self.userMethod.__name__+'\n')
    self.userMethod()
    print('\n\n'+ self.userMethod.__name__+' has finished running...\n')
  