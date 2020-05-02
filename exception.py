'''
def add(a,b):
    try:
        c = a+b
        return c
    except:
        print("Error in adding two numbers")
        if(b == 0):
            exit()
        #y= int(input("Enter the number other than y"))

def div(a,b):
    try:
        c = a/b
        return c
    except:
        print("You are trying to divide the number with zero")

x = int(input("Enter the number x"))
y = int(input("Enter the number y"))
print(add(x,y))
print(div(x,y))
'''

def divide1():
    try:

        num1 = int(input("Enter the num1"))
        num2 = int(input("Enter the num2"))
        c = num1/num2
        #print("Result is :",c)
    #except ValueError :
    except Exception as e :
        print(e,type(e))
        #print("value is not int type")
    #except ZeroDivisionError :
        #print("Don't divide the num1 by 0")
    else :
        print("Result is :",c)
    finally:
        print("Program ends here")
        

divide1()

raise IOError("Hello exception raised throuhg programe")