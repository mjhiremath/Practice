password = input("Enter the password")
if password == "MJ":
    print("Welcome to MJ palace")
else:
    print("Access denied to MJ Palace")

num = int(input("Enter the number"))
if num >= 4:
    letter = "A"
elif num >= 3:
    letter = "B"
elif num >= 2:
    letter = "c"
else:
    letter = "D"
print("Your grade is :",letter)


for a in range(4):
    print(a, end= " ")
print("\n")

for each in "MJ Hiremath":
    print(each, end = " ")

sum=0
counter =1
while (counter < 10):
    sum +=counter
    print(sum)
    counter+=1