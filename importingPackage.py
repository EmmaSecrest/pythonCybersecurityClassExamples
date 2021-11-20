#importing a package example
import os
print(os.path.isdir('c:\\data'))
print(os.path.isdir('c:\\foobar'))
#both resulted in false for me since neither of these are a full path
print(os.path.isdir(r'C:\Users\esecr')) #while this came back true since it is a directory

#printing a list of directories
print(os.listdir(r'C:\Users\esecr'))

#get working directory
print(os.getcwd())