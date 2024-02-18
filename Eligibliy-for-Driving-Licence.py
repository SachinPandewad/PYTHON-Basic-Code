# Cheaking Eligiblity by agefor Driving License id.

def eligiblityDriving():
    if ((age)<18):
        print("You are not Eligible for Driving License.")
    else:
        print("You are eligible for Driving License .")

while True:
    age = int(input("Enter your age. "))

    eligiblityDriving()
        
    find_again = input("Want to find again? (y/n): ")
    if find_again.lower() != "y":
        break