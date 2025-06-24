# 6. Transportation Mode Selection

# Problem: Choose a mode of transportation based on the distance (e.g., <3 km: Walk, 3-15 km: Bike, >15 km: Car).

distance = 50

if distance < 3:
    transport = "Wolk"
elif distance <= 15:
    transport = "bike"
else:
    transport = "Car"
print("Ai is recommended you the transport of :", transport)
