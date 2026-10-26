name = input("Enter passenger name: ")
age = int(input("Enter passenger age: "))
distance = int(input("Enter distance in km: "))

if distance <= 100:
    fare = distance * 1
elif distance <= 300:
    fare = distance * 1.5
else:
    fare = distance * 2

if age >= 60:
    fare = fare * 80 / 100
elif age <= 12:
    fare = fare * 50 / 100

total = fare + 30

print("Passenger:", name)
print("Basic Fare:", fare)
print("Reservation Fee: 30")
print("Total Fare:", total)