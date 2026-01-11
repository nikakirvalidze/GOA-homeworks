# 2) ფუნქცია არის კოდი, რომელიც ასრულებს კონკრეტულ დავალებას. custom ფუნქცია არის მომხმარებლის მიერ შექმნილი ფუნქცია.
def hello(name):
    return "Hello " + name


def count(numbers):
    return len([i for i in numbers if i % 2 == 0])


def greet(first_name, last_name):
    return "Hello " + first_name + " " + last_name


def even(number):
    if number % 2 == 0:
        return True
    else:
        return False


# 6) return keywork-ი პასუხს აუტომატურად გვიბრუნებს, ხოლო print მხოლოდ მაშინ როდესაც დავწერთ.  