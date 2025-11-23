
fruits = ["Apple", "Banana", "Orange", "Grapes", "Pineapple"]
print( fruits[0])
print( fruits[-1])


fruits[-1] = ("Mango")
print("ლისთა 'Mango'-ის დამატების შემდეგ:", fruits)
fruits[2] = "Kiwi"
# 2)
numbers = [10, 20, 30, 40, 50, 60, 70]


print( numbers[:3])
print( numbers[-2:])
print( numbers[2:6])
print( numbers[::2])


# 3)
surname = "kirvalidze"
reversed_surname = surname[::-1]


# 4) Slicing საშუალებას გვაძლევს სტრინგის ან ლისთის ნაწილის ამოღებას, თუმცა indexing-ისგან 
# განსხვავებით შეგვიძლია რამდენიმე ელემენტი ამოვიღოთ, შევცვალოთ ან წავშალოთ.

# 5)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
total = 0 
for num in numbers:
    if num % 2 != 0: 
        total = total + num  

# 6)
text = input("შეიყვანეთ ტექსტი: ")
if text == text[::-1]:
    print("Text is Palindrome")
else:
    print("not palindrome")