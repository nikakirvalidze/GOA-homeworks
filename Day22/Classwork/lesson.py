# print ეკრანზე აჩვენებს ინფორმაციას.
# type აბრუნებს მონაცემთა ტიპს.
# range ჩამოთვლის რიცხვებს ან სიტყვებს რაც ცვლადშია ციკლებისთვის.
# str გარდაქმნის ტექსტად (string)
# int გარდაქმნის მთელ რიცხვად (integer).
# float გარდაქმნის ათწილადად.
# bool გარდაქმნის True/False-ად.
# upper ტექსტს აქცევს დიდ ასოებად.
# lower ტექსტს აქცევს პატარა ასოებად.
# capitalize მხოლოდ პირველ ასოს ადიდებს.
# find სტრინგში ეძებს კონკრეტულ სიმბოლოს და აბრუნებს პირველ შემხვედრს
# swapcase დიდ ასოებს აპატარავებს და პატარა ასოებს ადიდებს
result = 0

for i in range (0, 31, 2):
    print(i)
    result += 1

# არგუმენტი არის მონაცემი რაც ფუნქციას გადაეცემა სამუშაოდ.
print(10, 3.14, "text", True, [1,2])



lastname = "kirvalidze"
print(lastname.upper())
print(lastname.lower())
print(lastname.capitalize())
print(lastname.find("b"))
print(lastname.swapcase())