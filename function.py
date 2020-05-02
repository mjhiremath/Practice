def function(name):
    print("Hello World, This is function example")
    print(name)

function("MJ")
#function()

def add(a,b):
    c = a+b
    return c
   # print(c)
x=10
y=9
print("Sum of 2 numbers", add(x,y))


def info(name,age=30):
    print("Name",name)
    print("Age",age)

info("MJ")
info("Raj",45)

def variable_argument(var1,*vari):
    print("output is:",var1)
    for var in vari:
        print(var, end=" ")

variable_argument(89)
variable_argument(90,56,3543,34,23,434,342)
print("\n")
print("#################################################################################")

def infocity(**var):
    print(var)
    for key,value in var.items():
        print("%s==%s" %(key,value))

infocity(name="14w",age=20,city="America Duluth")
infocity(naem="MJ",age=56,city="London",mdedals=30)

print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

def pass_ref(list9):
    list9.extend([70,90])
    print("List inside the function",list9)


list9=[10,20,30,40,50]
print("List before pass",list9)
pass_ref(list9)
print("list outside the functions",list9)

def func(a):
    a+=4
    print("Values of a inside function",a)
a=10
func(10)
print("value of a outside a function",a)

def scope():
    global k
    k = k+7
    print("value of k Inside the function",k)
k=10
scope()
print("Value of k outside the function",k)


