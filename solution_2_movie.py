# 2. Movie Ticket Pricing

# Problem: Movie tickets are priced based on age: $12 for adults (18 and over),
# $8 for children. Everyone gets a $2 discount on Wednesday.

import random

age = 20

price = 12 if age >= 18 else 8

days = ["Suturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]


day = random.choice(days)
print(day)
if day == "Wednesday":
    price -= 2
    print(f"Ticket Price is {day}", price)

else:
    print("Your Ticket Price is ", price)
