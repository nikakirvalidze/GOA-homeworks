# Logical operators გამოიყენება პირობის შედარებისას True/False მნიშვნელობების მისანიჭებლად.
# 1-ლი არის and, რომელიც აბრუნებს True-ს მაშინ, როცა ორივე პირობა არის True და თუ ერთი პირობა მაინცაა False-ი შედეგიც False იქნება.
# მე-2 არის or, რომელიც აბრუნებს True-ს თუ ერთი პირობა მაინცააა შესრულებული და აბრუნებს False-ს თუ არცერთი პირობა არაა შესრულებული


name = input("შეიყვანე სახელი: ")
print(name == "იხვი")



age = input("შეიყვანე ასაკი: ")
print(age == 50)



fav_toy = input("შეიყვანე შენი საყვარელი სათამაშო: ")
print(fav_toy == "yoyo")


print(True and False and True or False and True and False and True and False or True and False or True or False)
# ჩემი აზრით აზრზე არ ვარ რას მივიღებთ



print(5 == 5)
print(7 == 3)
print(10 < 20)
print(15 > 30)
print(8 <= 8)



print(True and False)
print(True or False)