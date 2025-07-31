score = float(input("Enter Score between 0.0 and 1.0: "))
if score >= 0.9 and score <= 1.0:
    grade = "A"
elif score >= 0.8 and score < 0.9:
    grade = "B"
elif score >= 0.7 and score < 0.8:
    grade = "C"
elif score >= 0.6 and score < 0.7:
    grade = "D"
elif score >= 0.0 and score < 0.6:
    grade = "F"
else:
    print("out of range")
    quit()
print(grade)