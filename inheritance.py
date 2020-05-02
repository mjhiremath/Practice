class A():

    def add(self,a,b):
        c = a +b
        return c
class B(A):
    pass
    #def __init__(self,a,b):

obj = B()
print(obj.add(10,20))