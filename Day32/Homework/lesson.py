# 1)
def remove_chars(words, chars):
    result = []
    for word in words:
        new_word = ""
        for letter in word:
            if letter not in chars:
                new_word += letter
        result.append(new_word)
    return result

words = ["nika", "vano", "giorgi"]
chars = "abc"
print(remove_chars(words, chars))
# 2)
list = ["pizza", "harry potter", "blox fruits", "shaurma", "cake"]
print(list)
list.append("ice cream")
list.remove("cake")
print(list)
# 3)
numbers = (5, 10, 15, 20, 25)
print(numbers)
print(numbers[1])
print(numbers[-1])
print(10 in numbers)
# 4)
set = {1, 2, 3, 4, 4, 5}
print(set)
set.add(6)
set.remove(3)
set.discard(10)