#make sure the file actually exists first
#reading
file = open(r"C:\Users\esecr\demoFile.txt",'r') #need the r there to make sure the compiler knows that it is a raw string
#I got an error without the r in front
# might want to copy the path, reason 1 I like visual studio code better: you don't have to do this
# 'r' means we are reading the file
print(file.read())
#reading some character
file = open(r"C:\Users\esecr\demoFile.txt",'r') # apparently you do need to repeat this line to get the output
print(file.read(2))
#reading line by line
file = open(r"C:\Users\esecr\demoFile.txt",'r')
print(file.readline()) #just reads the first line since there is only one call here
file.close() # make sure to close the file when done