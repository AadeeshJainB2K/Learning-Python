#Write a user-defined function FindTopScorer(StudentDict) that accepts a dictionary where keys are student names (strings) and values are their total marks (integers). The function should calculate and return a tuple containing the name of the top scorer and the class average marks. (3 Marks)
import statistics as stats

student_data = {
    "Liam": 85,
    "Sophia": 98,
    "Ethan": 72,
    "Ava": 93,
    "Oliver": 88
}

def FindTopScorer(StudentDict):
    maxMarks = max(StudentDict.values())
    avgMarks = stats.mean(StudentDict.values())
    for k , v in StudentDict.items() :
        if (v == maxMarks):
            print (k)
    print (maxMarks)
    print(avgMarks)

FindTopScorer(student_data)
