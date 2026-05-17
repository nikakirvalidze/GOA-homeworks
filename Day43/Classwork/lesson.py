
student = { "firstname" : "john", "lastname" : "doe", "age" : "18", "score" : "10/10" }

car = { "model" : "audi" }
car.update("color") = "black"
car("color") = "white"


fruits = { "orange" : "orange", "watermelon" : "green", "pear" : "IDontEvenKnow" }
for i in fruits:
    print(i.values)
    print(i.key)


store = {
    "laptop": {
        "price": 3200,
        "stock": 5,
        "rating": 4.7
    },
    "phone": {
        "price": 1800,
        "stock": 8,
        "rating": 4.5
    },
    "tablet": {
        "price": 1200,
        "stock": 3,
        "rating": 4.2
    }
}

# 5
store["headphones"] = {
    "price": 400,
    "stock": 12,
    "rating": 4.8
}

# 6
store("price") = store("price") * 1.1

# 7
high_rated = {}
for item, details in store.items():
    if details["rating"] > 4.5:
        high_rated[item] = details;