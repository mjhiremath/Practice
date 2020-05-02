class leapx_org():
    mul_num = 1.2
    count = 0
    def __init__(self,first,last,pay):
        self.f_name = first
        self.l_name = last
        self.pay_amt = pay
        self.full_name = first+ " " +last
        leapx_org.count = leapx_org.count+1
    def make_email(self):
        return self.f_name+ "."+self.l_name+"@fast.com"
    def increment_pay(self):
        self.pay_amt = self.pay_amt*self.mul_num
        return self.pay_amt

class instructor(leapx_org) :
    def __init__(self,first,last,pay,subject):
        pass
    pass
    leapx_org.__init__(self,first,last,pay)
    self.subject = subject


l_obj1 = leapx_org("MJ","Hiremath",130000)
#l_obj2 = leapx_org()
l_obj1.mul_num = 1.3
in_obj = instructor("MJ","Hiremath",4343443,"Science")
print(in_obj.subject)
print(l_obj1.make_email())
print(l_obj1.increment_pay())
print("Number of emploees", leapx_org.count)
print(l_obj1.__dict__)
print(leapx_org.__dict__)
