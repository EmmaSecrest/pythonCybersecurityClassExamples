#keyword argument
#key pairs
def myFun(**kwargs):
    for key,value in kwargs.items():
        print("%s == %s"%(key,value))

myFun(first = "Geeks" ,mid = "for",last = "Geeks")

#example two
def displayKeywordArgs(firstNumber,**kwargs):
    for ar in kwargs:
        print(ar,kwargs[ar])

kwargs = {"appName": "Hello" , "appVers": 2.5}
displayKeywordArgs(100,**kwargs)
## passing in a dictionary in this case
