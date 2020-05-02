file_input = open("motivational.txt",'w')
file_input.write("Never give up")
file_input.write("\nRise above hate")
file_input.write("\nnobody remenbers second place")
file_input.close()
file_read = open("motivational.txt",'r')
for line in file_read:
    print(line)
#print(file_print)
file_input.close()


list1 = ["blood sweat and respect","\nThe first two you given"]

file_moti = open("moti.txt",'w')
file_moti.writelines(list1)
file_moti.close()
file_motiread = open("moti.txt",'r')
print(file_motiread.read())


file_read = open("motivational.txt",'r')
file_write = open("moti.txt",'a+')
file_write.write("\n")
for each in file_read:
    file_write.write(each)
file_read.close()
file_write.close()
print("readtinf the moti.txt file")
print("###########################################################")
read_file = open("moti.txt",'r')
for read in read_file:
    print(read)
#for i in file_motiread:
 #   print(i)