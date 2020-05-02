import collections
co = collections.Counter([1,2,3,4,5,6,6,7,6,4])
print(co)

co1 = collections.Counter(['MJ Hiremath',"HEllo", "hi","HI"])
print(co1)

co2 = collections.Counter("MJ Hiremath")
print(co2)
co2.update("Mrityunjaya")
print(co2)
co2.update({'a':2,'j':3})
print(co2)

c = collections.Counter("King MJ was the youngest entrepreneurs of the world")
#print(c)

for letter in 'King of world':
    print("%s : %d" %(letter,c[letter]), end = " ")

print("\n")
print("##################################################\n")
print(co1)
print(co2)
print("additon of two collections",co1 + co2 )
print("substractions of collections", co1 - co2)
print("Union of collections", co1 | co2)
print("Interseactions of collections", co1 & co2)