#handles a simple error without crashing the program
a = [1,2,3]
try:
    print('Second element = %d'  %a[1])
    print("fourth element = %d" % a[3])
except IndexError:
    print('an Error has Occured')

#another example
try:
    a = 3
    if a <4:
        b = a/(a-3)
    print("value of b = " ,b)
except(ZeroDivisionError,NameError):
    print("\nError Ocurred and Handled")


