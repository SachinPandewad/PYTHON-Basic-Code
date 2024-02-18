#Final Exam Eligiblity Criteria:

def examEligiblity():
    if attendance >= 75 and assignment_Submitted >= 70:
        if sports_Player == 'yes' or sports_Player == 'y':
            print("The Student is Eligible to Appear in Final Exam and he can get Extra Grace Marks = +10")
        else:
            print("The Student is Eligible to Appear in Final Exam but mot extra Grace Marks.")
    else:
            print("The Student is NOT Eligible For Final Exam.")


while True:
    attendance = float(input("Enter Attendace of Student: "))
    assignment_Submitted = float(input("Enter No. of Assignment Submitted by Student: "))
    sports_Player = str(input("Is Student Sport Player? : [y or yes, n or no]")) # not Mandatory

    print("Attendance of Student: ", attendance)
    print("No. of Assignment Submitted by Student are: ", assignment_Submitted)
    print("Is Student Sport Player? :", sports_Player)
    examEligiblity()

        
    find_again = input("Want to find again? (y/n): ")
    if find_again.lower() != "y":
        break