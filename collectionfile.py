import collections
co = collections.Counter()
file_read = open("moti.txt",'r')

for letter in file_read:
    co.update(letter.lower())
print(co)

for letter,count in co.most_common(5):
    print("%s : %d" %(letter,count))


