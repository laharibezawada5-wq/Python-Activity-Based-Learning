total_classes = int(input("Enter total classes: "))
attended = int(input("Enter classes attended: "))

attendance = attended * 100 / total_classes

print("Attendance:", attendance, "%")

if attendance >= 75:
    print("Attendance is sufficient")
else:
    needed = (0.75 * total_classes - attended) / 0.25
    print("Extra classes to attend approximately:", int(needed) + 1)