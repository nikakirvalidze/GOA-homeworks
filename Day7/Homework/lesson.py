
name = input("შეიყვანეთ თქვენი სახელი: ")
print("გამარჯობა,", name)

# 2) კონკატინაცია არის ორი ან მეტი string-ის გაერთიანება ერთ სთრინგში.
greeting = "გამარჯობა, "
full_greeting = greeting + name 
print(full_greeting)

# 3)
str_number = "10"
int_number = 5 
str_number_int = int(str_number)
result1 = str_number_int + int_number
result2 = str_number_int - int_number
result3 = str_number_int * int_number
result4 = str_number_int / int_number



height = input("შეიყვანეთ თქვენი სიმაღლე მეტრებში: ")
height_float = float(height)
print(type(height_float))

# 5)Data Conversion არის პროცესი როდესაც მონაცემთა ტიპი ერთ ტიპიდან სხვა ტიპში გარდაიქმნება. მაგალითად, string-იდან int, int-იდან float და ა.შ.

# 6)Implicit  - ავტომატურად ხდება Python-ის მიერ, როდესაც პროგრამას სჭირდება  სხვა ტიპის მონაცემი სხვა ტიპთან ოპერაციისთვის.
# Explicit Conversion - ჩვენ ხელით ვცვლით მონაცემთა ტიპს.
# ფუნქციები:
# int  -> გარდაქმნის integer ტიპში
# float-> გარდაქმნის float ტიპში
# str -> გარდაქმნის string ტიპში
# bool -> გარდაქმნის boolean ტიპში

num_str = "123"
num_int = int(num_str) 
num_float = float(num_str)
num_back_str = str(num_int)
is_true = bool(num_int)