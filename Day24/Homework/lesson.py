# 1)
s = input()
print(s.upper())
print(s.lower())

# 2)
s = input()
print(len(s))

# 3)
nums = [1, 2, 3]
nums.append(4)
nums.pop()
print(nums)

# 4)
items = ["apple", "banana", "apple", "orange"]
count = 0
for i in items:
    if i == "apple":
        count += 1
print(count)

# 5)
s = input()
print(s.swapcase())

# 6)
nums = [1, 2, 3, 4, 5]
n = int(input())
nums.append(n)
print(nums)