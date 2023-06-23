# Cheaking Eligiblity by agefor Driving License id.


while True:
    age = int(input("Enter your age. "))

    if ((age)<18):
        print("You are not Eligible for Driving License.")
    else:
        print("You are eligible for Driving License .")
        
    find_again = input("Want to find again? (y/n): ")
    if find_again.lower() != "y":
        break