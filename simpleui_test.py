import simpleui as sui
import sys

def input_test():
  def testMethod(test=None, test2=3, test4={}):
    inputVar = input("Entery Your name: ")
    print(inputVar)

  testApp = sui.wrapCLI(testMethod)
  testApp.mainloop()

def output_test():
  def testMethod(test=None, test2=3, test4={}):
    print('This is a standard out put (print)')
    sys.stdout.write('This is also a standard output (sys.stdout)')
    sys.stderr.write('This is a standard error output (sys.stderr)')

  testApp = sui.wrapCLI(testMethod)
  testApp.mainloop()
  #end output_test():

if __name__ == '__main__':
  input_test()