#1)
age = int(input("შეიყვანე შენი ასაკი: "))
if age >= 18:
    print("შენ შეგიძლია არჩევნებზე წასვლა და ხმის მიცემა!")
else:
    print("სამწუხაროდ, შენ ჯერ ვერ შეძლებ არჩევნებში მონაწილეობას.")


#2)
number = (input("შეიყვანე რიცხვი: "))
if number % 2 == 0:
    print("ეს რიცხვი ლუწია.")
else:
    print("ეს რიცხვი კენტია.")


#3)
cars = ["BMW", "Mercedes", "Toyota", "Audi", "Honda"]
first_car = cars[0]
last_car = cars[-1]

print("პირველი მოდელია:", first_car)
print("ბოლო მოდელია:", last_car)
print("პირველი მოდელის პირველი ასო:", first_car[0])
print("ბოლო მოდელის პირველი ასო:", last_car[0])

#4)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    if num % 2 == 0:
        print(num)