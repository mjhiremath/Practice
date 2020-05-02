class MyException(Exception):
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return (self.value)

try:
    num = input("Enter the number")
    if num == '2':
        raise MyException("You entered 2")
    else:
        print("Your entered number is not 2")
except MyException:
    print("My exception occured")