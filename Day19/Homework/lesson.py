# 1)
letters = ['a','b','c','d','e','f','g','h']
print(letters[:4])
print(letters[2:7])
print(letters[::2])
print(letters[::-1])

# 2)
nums = [10,20,30,40,50,60,70,80,90,100]
nums[-2:] = [111, 222]
print(nums)

# 3)
numbers = list(range(1,21))
even_sum = sum([n for n in numbers if n % 2 == 0])

new_list = [even_sum]
print(new_list)

# 4)
nums = [1,2,3,4,5,6,7,8]
middle_four = nums[2:6]
last_three = nums[-3:]
print(middle_four)
print(last_three)

# 5)
letters = list("abcdefghij")
print(letters[1::2])

# 6)
nums = [1,2,3,4,5,6,7,8,9]

for n in nums:
    if n % 2 == 0:
        print(n, "→ Your Number is even")
    else:
        print(n, "→ Your Number is Odd")

# 7)
lst = [1,2,3,2,1]

if lst == lst[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

# 8)
items = ["hello", 10, 3.14, "test", 2.71, 5]

floats_only = [x for x in items if type(x) == float]
print(floats_only)

# 9)
nums = [1,2,3,4,5,6,7,8,9,10]
nums.sort(reverse=True)
print(nums)