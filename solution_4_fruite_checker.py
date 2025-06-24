# 4. Fruit Ripeness Checker

# Problem: Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)


# 💡 Problem 1: Apple Ripeness Detection
# Determine if an apple is unripe, ripe, or overripe based on its color.

# Green → Unripe

# Red → Ripe

# Dark Brown/Black Spots → Overripe

# 💡 Problem 2: Mango Ripeness Detection
# Given the color of a mango, identify its ripeness status.

# Green → Unripe

# Yellow → Ripe

# Orange/Brown → Overripe

# 💡 Problem 4: Strawberry Ripeness
# Check the ripeness of a strawberry using its color.

# Green or White → Unripe

# Bright Red → Ripe

# Dark Red with soft spots → Overripe




fruite=input("Enter your Fruite Name ").capitalize()

color=input("Give your Fruit Color ").capitalize()


if fruite== "Banana":
    if color == "Yellow":
        print("Ripe")
    elif color == "Green":
        print("Unripe")
    elif color == "Brown":
        print("Overripe")
        
elif fruite == "Apple":
    if color == "Red":
        print("Ripe")
    elif color == "Green":
        print("Unripe")
    elif color == "Dark Brown/Black ":
        print("Overripe")
        
elif fruite == "Mango":
    if color == "Yellow":
        print("Ripe")
    elif color == "Green":
        print("Unripe")
    elif color == "Orange/Brown":
        print("Overripe")
        
elif fruite == "Strawberry":
    if color == "Bright Red":
        print("Ripe")
    elif color == "Green or White":
        print("Unripe")
    elif color == "Dark Red with soft spots":
        print("Overripe")
      