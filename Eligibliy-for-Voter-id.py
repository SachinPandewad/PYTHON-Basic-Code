# Cheaking Eligiblity by agefor Voter id.

while True:
    age =int(input("Enter Your Age. "))
    if((age),18):
        print("You are NOT ELIGIBLE for Voter id.")
    else:
        print("You are ELIGIBLE for Voter id.")

        find_again = input("Want to find again? (y/n): ")
        if find_again.lower() != "y":
            break