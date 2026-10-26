participants = int(input("Enter number of participants: "))
fee = int(input("Enter registration fee per person: "))
sponsorship = int(input("Enter sponsorship amount: "))

venue = 10000
equipment = 5000
transport = 3000

catering = participants * 150
certificates = participants * 20

total_cost = venue + equipment + transport + catering + certificates
registration = participants * fee
total_income = registration + sponsorship

balance = total_income - total_cost

print("Total Cost:", total_cost)
print("Registration Income:", registration)
print("Sponsorship:", sponsorship)
print("Total Income:", total_income)
print("Final Balance:", balance)

if balance >= 0:
    print("Event is Profitable")
else:
    print("Event has a Shortfall")