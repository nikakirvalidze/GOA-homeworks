# 1) Slicing საშუალებას გვაძლევს სტრინგის ან ლისთის ნაწილის ამოღებას, თუმცა indexing-ისგან 
# განსხვავებით შეგვიძლია რამდენიმე ელემენტი ამოვიღოთ, შევცვალოთ ან წავშალოთ.

# 2) ფუნქცია არის კოდი, რომელსაც აქვს სახელი და იმისთვისაა, რომ ერთი და იგივე მოქმედების გამეორება ბევრჯერ არ მოგვიწიოს.

# 3)
currencies = ["dollar" "euro" "lari" "yen" "rupee"]
print (currencies[2:])
print (currencies[-1:2])
print (currencies[::-1])
print (currencies [::2])


# 4)
last_name = ["k" "i" "r" "v" "a" "l" "i" "d" "z" "e"]
print (last_name [5:0])
print (last_name [0:3])

# 5)
names = ["ana" "gio" "luka" "saba" "dato" "natali"]
names[-2] = "nika"

