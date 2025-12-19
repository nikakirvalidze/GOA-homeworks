#1)
surname = "kirvalidze"
result = 0
for i in range(0, 10):
    print(i)
    result += 1
print(result)
#2)
name = input("შეიყვანე სახელი: ")
print(name.upper())
print(name.lower())
print(name.capitalize())
print(name.find(name[5]))
print(name[::-1].upper())
print(name.swapcase())