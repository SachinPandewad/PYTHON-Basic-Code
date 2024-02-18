# Printing list in range by user inputs


while True:
    a = int(input("Enter Range Starts From Number."))
    b = int(input("Enter Range Ends at Number."))

    for i in range (a, b+1):
        print(i)

    find_again = input("Want to find again? (y/n): ")
    if find_again.lower() != "y":
        break