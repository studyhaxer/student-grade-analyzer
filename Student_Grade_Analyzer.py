def main():
#empty students list is created 
    students = []
#Calculate average score by using function
    def calc_average (marks):
        return sum(marks) / len(marks)
#get grades
    def calc_grades(perc):
        if perc > 90:
            return "A+ Grade"
        elif perc > 80:
            return "A Grade"
        elif perc > 70:
            return "B Grade"
        elif perc > 60:
            return "C Grade"
        elif perc > 50:
            return "D Grade"
        elif perc > 40:
            return "E Grade"
        else:
            return "F Grade"
#looping to get students data as dict, append in list 
    for i in range(0,5):
        stdname = input("Please enter your Name : ")
        phy_marks = int(input("Please enter your physics marks out of 100 : "))
        com_marks = int(input("Please enter your computer marks out of 100 : "))
        eng_marks = int(input("Please Enter your English Marks out of 100 : "))
        student_dict = {
            "name" : stdname,
            "marks" : [phy_marks,com_marks,eng_marks]
        }
        students.append(student_dict)
#topper data by default
    top_avg  = 0
    topper = ""
#print students data 
    print("============GRADE BOOK============")
    for student in students:
        avg = calc_average(student['marks'])
        if avg > top_avg :
            top_avg  = avg
            topper = student["name"]
        grade = calc_grades(avg)
        print(f"{student['name']:<15} | {round(avg, 2):<6} | {grade}")
#Topper of Class
    print(f"Topper is: {topper} with Percentage: {round(top_avg ,2)}")
if __name__ == "__main__":
    main()