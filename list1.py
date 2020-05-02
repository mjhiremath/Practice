list1 = [10,9,3,7,2,1,21,1,561,1,1,96,1]

list1.sort()
print(list1)
list1.reverse()
print(list1)

list1 = [1,2,3,4,5,6]
list2 = []
for each in list1:
    if each%2==0:

        list2.append(each*each)
print(list2)

port = [[80,'http'],[20,'ftp'],[23,'telnet'],[443,'https'],[53,'DNS']]
port1 = dict(port)
for key in port1.keys():
    print(key)
print(port1.keys())
print(port1.values())
#print(port1.keys())
port2={22:"SSH"}
port1.update(port2)
print(port1)

print(port1.items())

for k,v in port1.items():
    print(k, " :" ,v)

list4 = [1,2,3,4,5]
list5 = ["a","b","c","d","e"]
#print(len(list4))
dict2={}
for index in range(len(list4)):
    dict2[list4[index]]=list5[index]
print(dict2)


list6 = ["Londo","New yyork","Paris","Hyderbad"]

for each in list6:
    str1 = each
    print(each)
    for s in str1:
        if s == 'o':
            break
        print(s,end="")
    print("\n")

for each in list6:
    if each== "Paris":
        continue
    print(each)

