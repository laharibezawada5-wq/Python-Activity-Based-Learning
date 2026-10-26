marks = int(input("Enter aggregate marks: "))
attendance = int(input("Enter attendance percentage: "))
income = int(input("Enter annual family income: "))

if marks >= 75 and attendance >= 75 and income <= 200000:
    print("Eligible for scholarship")
else:
    print("Not eligible for scholarship")