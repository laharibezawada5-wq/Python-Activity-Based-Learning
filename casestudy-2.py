budget = int(input("Enter your budget: "))
usage = int(input("Enter required daily data in GB: "))
days = int(input("Enter required validity in days: "))

if budget >= 199 and usage <= 2 and days <= 28:
    print("Plan A is suitable")
elif budget >= 299 and usage <= 3 and days <= 56:
    print("Plan B is suitable")
elif budget >= 399 and usage <= 4 and days <= 84:
    print("Plan C is suitable")
else:
    print("No suitable plan available")