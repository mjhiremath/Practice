#import sys
import os
#sys.path.append("D:/")
path = 'D:\Python\MJ1.txt'
file_object = open(path,'r')
for each in file_object:
    print(each)


#file_read = file_object.read()
#print(file_read)
print("##################################")
'''readt first 10 characters'''
#character_10=file_object.read(10)
#print(file_object.read(20))
#print(character_10)
word = input("Enter the word")
word = word.lower()
count=0
for each in file_object:
    if word in each.lower():
        count+=1
print("The",word,"occured",count,"times")
    #print(each)
#print(file_object.readline())
#print(file_object.readline())
#print(file_object.readlines())
file_object.close()
