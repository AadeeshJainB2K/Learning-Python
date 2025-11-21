userMarks = {}
meanMarks = 0
for i in range (0,3): 
    subject = input("Enter subject name: ")
    marks = float(input("Enter marks obtained in " + subject + ": "))
    userMarks[subject] = marks
    meanMarks += marks
meanMarks = meanMarks / 3
print("The mean marks obtained in the subjects is: ", meanMarks)

print("The marks obtained in the subjects are: ", userMarks)
