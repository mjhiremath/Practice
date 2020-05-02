'''name = input("Enter the name")
print(name)
print(name[::-1])
print(name)
'''

def reverse(s):
    str=""
    for i in s:
        str = i+str
    return str

print(reverse("Hello"))


def reverse1(s):
    if len(s) == 0:
        return s
    else:
        return reverse1(s[1:]) + s[0]
    return (reverse1(s[1:]))

print(reverse1("Hey"))

name ="MJ Hiremath"
print(name[1:])


#fibonacci series 1,1,2,3,5,8,11

#n = int(input("Enter the number fibonacci series to print"))
a = 0
b = 1
c = 0
for i in range(5):
    print(a, end=" ")
    c = a + b
    a = b
    b = c

print("\n")
n = 5

for i in range(n):
    for j in range(i):
        print("*",end ="")
    print("\n")