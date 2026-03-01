# 4)
numbers = (1, 2, 3, 4, 5, 6, 7, 8)
numbers = list(numbers)
numbers[4] = 14
numbers = tuple(numbers)
print(numbers)
# 5) (asterisk) ოპერატორი გამოიყენება unpacking-ის დროს, რომ ერთ ცვლადში შევინახოთ რამდენიმე მნიშვნელობა  ერთად.

# 6)
items = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
v1, v2, *v3, v4, v5 = items

# 3)
names = ("Nika", "Giorgi", "Ana")
name1, name2, name3 = names
print(name1)
print(name2)
print(name3)

# 1)
def join(x, y):
    result = ""
    for i in x:
        result += "idk" + "idk2"
    return result[:-1]

# 2)