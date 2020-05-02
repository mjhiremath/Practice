import collections as c
emploee = c.namedtuple('emp','name,age,id')
record1 = emploee('MJ',34,1)
print("record",record1)
print("Name of the employee",record1.name, "age of the emploee",record1.age)
print("type is",type(record1))

list1 = ['Raj',50,1]
record2 = emploee._make(list1)
print(record2)
print(record2._asdict())

d = record1._replace(age=25)
print(d)
d = d._replace(id=2)
print(d)