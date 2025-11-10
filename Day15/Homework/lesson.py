score = int(input("შეიყვანეთ სტუდენტის ქულა (0-100): "))

if 90 <= score <= 100:
    print("ნიშანი: A")
elif 80 <= score <= 89:
    print("ნიშანი: B")
elif 70 <= score <= 79:
    print("ნიშანი: C")
elif 60 <= score <= 69:
    print("ნიშანი: D")
elif 0 <= score <= 59:
    print("ნიშანი: F")
else:
    print("არასწორი ქულა! შეიყვანეთ 0-100 შორის რიცხვი.")


num = float(input("შეიყვანეთ რიცხვი: "))

if num > 0:
    print("რიცხვი დადებითია ")
elif num < 0:
    print("რიცხვი უარყოფითია ")
else:
    print("რიცხვი ნულია ")


num1 = float(input("შეიყვანეთ პირველი რიცხვი: "))
num2 = float(input("შეიყვანეთ მეორე რიცხვი: "))

if num1 > num2:
    print("First Number is Greater than second one")
elif num1 < num2:
    print("Second Number is Greater than first one")
else:
    print("ორივე რიცხვი ტოლია")


num = int(input("შეიყვანეთ რიცხვი: "))

if num % 2 == 0:
    print("რიცხვი ლუწია ")
else:
    print("რიცხვი კენტია ")


temp = float(input("შეიყვანეთ ტემპერატურა ცელსიუსში: "))

if temp < 0:
    print("Cold ")
elif 0 <= temp <= 30:
    print("Normal ")
else:
    print("Hot ")