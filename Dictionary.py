
boys = {'MJ':26,'Su':26,'Kiran':27}
girls = {'Reena':30,'Rutu':25}

studentx = boys.copy()
studentY = girls.copy()

print(studentx)
print(studentY)

Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
Dict.update({"Sarah":9})
print (Dict)

del Dict['Tim']
print(Dict)

print("Dictionary name %s" %Dict.items())

DictA = {'Science':90,'Maths':100,'Kannada':95}
DictB = {'Science':90,'Kannada':89,'Maths':100}

for Marks in DictA.keys() :
    if Marks in list(DictB.keys()) : print(Marks)
    else : print("Nothing matched")

    