# -1) ლისტის შეცვლა შეგიცლია თაფლის არა,ხოლო სეტში ერთნაირი ელემენტები წაიშლება
# 0)
# add-სეტში ელემენტებს ამატებს
# update-ელემენტბებს გადაუვლის და სეტში ჩაამატებს სათითაოდ
# remove-ელემენტებს შლის სეტიდან(თუ ვერ იპოფის ერორი)
# discard-იგივე რაც remove ოღონდ თუ ვერ იპოვის არაფერს იზამს
# union-სეტებს აერთიანებს და ახალ სეტს გვიბრუნებს
# update-სეტში ამატებს სხვა სეტის ელემენტებს
group1 = {"chicken", "banana", "hehehehe"}
group2 = {"doggy", "toilet"}
# 1)
group1.add("idk")
# 2) 
group2.update(["simba", "nadiri_var_bijooo", "fatass"])
# 3)
group1.remove("banana")
# 4)
group2.discard("simba")
# 5)
group3 = group1.union(group2)
# 6)
print(group1)
pring(group2)
print(group3)
# 7) 
numbers = (5, 12, 5, 7, 12, 9, 3, 3)
# 8)
print(numbers[2])
print(numbers[6])
# 9)
print(numbers[1:6])
# 10)
print(numbers.count(3))
# 12)
numbers2 = (20, 25, 30)
orive_numbers = numbers + numbers2
# 13)
lemmecook_list = list(numbers)
lemmecook_list.append(10000000)
tuple = tuple(lemmecook_list)
# 11)
print(numbers.index(3))
