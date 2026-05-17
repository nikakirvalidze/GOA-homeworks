students = {
    "ანა": {"score": 95, "attendance": 90},
    "გიორგი": {"score": 88, "attendance": 85},
    "ნინო": {"score": 98, "attendance": 95},
    "ლუკა": {"score": 75, "attendance": 80}
}
highest_score = 0
best_student = ""
total_score = 0

for name, details in students.items():
    total_score += details["score"]
    if details["score"] > highest_score:
        highest_score = details["score"]
        best_student = name
average_score = total_score / len(students)

# 2
products = {
    "laptop": {"price": 3000, "stock": 4},
    "phone": {"price": 1500, "stock": 10},
    "tablet": {"price": 1200, "stock": 0}
}

for prod, info in products.items():
    if info["stock"] > 0:
        print("- " + prod)

total_value = 0
for prod, info in products.items():
    total_value += info["price"] * info["stock"]

# 3

football_players = {
    "Cristiano Ronaldo": {"goals": 1000, "assists": 100},
    "Lionel Messi": {"goals": 700, "assists": 90}
}
football_players["Neymar"] = {"goals": 550, "assists": 150}
football_players["Lionel Messi"]["goals"] += 5
most_goals = -1
best_footballer = ""

for name, info in football_players.items():
    if info["goals"] > most_goals:
        most_goals = info["goals"]
        best_footballer = name

# 4
employees = {
    "Giorgi": {"salary": 2500, "position": "Manager"},
    "Nika": {"salary": 1800, "position": "Developer"},
    "Luka": {"salary": 1500, "position": "Designer"}
}

employees("salary") = employees("salary") * 1.1
for breh, bruh in employees.items():
    total_score += bruh["score"]
    if bruh["score"] > highest_score:
        highest_score = bruh["score"]
        best_student = name
