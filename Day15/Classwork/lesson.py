# == ამოწმებს, არის თუ არა ორი მნიშვნელობა ტოლი

# != ამოწმებს, არის თუ არა ორი მნიშვნელობა არატოლი

print(5 == 5)
print("hi" == "hi")
print(3 + 2 == 5)

print(4 != 5)
print("cat" != "dog")
print(10 != 10)

# Conditional statement გამოიყენება იმისათვის, რომ პროგრამამ შეასრულოს სხვადასხვა ქმედება პირობების მიხედვით.
# keyword-ები არის- 1)if თუ პირობა ჭეშმარიტია, elif-დამატებითი პირობა თუ წინა პირობა მცდარია, else-თუ არც ერთი პირობა არაა ჭეშმარიტი(ანყ if და elif-ები)


# მესამე დავალება
age = int(input("Enter your age: "))

if age > 18:
    print("You are an adult!")
elif age == 18:
    print("You are 18yo!")
else:
    print("You are teenager")

# მეოთხე დავალება
name = "Nika"
count = 0

while count < 5:
    print(name)
    count = count + 1
    


# მეხუთე დავალება
total = 0

for i in range(1, 7):
    total += i
print("total is:" , total)


# მეექვსე დავალება

user_name = input("Enter your name: ")
my_name = "Nika"

if user_name == my_name:
    print("The names are the same")
else:
    print("The names are different")