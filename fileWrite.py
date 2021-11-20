#writing to files
file = open(r"C:\Users\esecr\demoFile.txt",'w')
file.write("Hello\nWorld")
#note the file wrote over what was there before
file.close() # close the file since we are done writing to it
file = open(r"C:\Users\esecr\demoFile.txt",'r') #opening it again to read it
print(file.read())
file.close()