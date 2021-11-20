#combine two lists
listOne = [10,20,30,40]
listTwo = [50,60,70]
listAll = listOne + listTwo
print(listAll)

#this will repeat the list twice
listOne = listOne *2
print(listOne)

#slicing is inclusive on the left but exclusive on the right
print(listAll[1:3]) #prints [20,30]