#Show Pass-Fail status of students 

while True:
    average = float(input('Enter Average Marks : '))
    if (float(average)>= 50):
        print("PASSED")
    else:
        print("FAILED")
    find_again = input("Want to find again? (y/n): ")
    if find_again.lower() != "y":
        break