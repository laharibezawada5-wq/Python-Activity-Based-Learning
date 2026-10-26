name = input("Enter patient name: ")
consultation = int(input("Enter consultation charges: "))
diagnosis = int(input("Enter diagnosis charges: "))
treatment = int(input("Enter treatment charges: "))

total = consultation + diagnosis + treatment

if total >= 4000:
    discount = total * 10 / 100
else:
    discount = 0

final_bill = total - discount

print("Patient Name:", name)
print("Total Bill:", total)
print("Discount:", discount)
print("Final Bill:", final_bill)

if final_bill >= 3000:
    print("High Bill")
else:
    print("Normal Bill")