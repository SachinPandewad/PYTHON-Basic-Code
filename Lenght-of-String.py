# to find lenth of string..-

while True:
    a=input("Enter string :- ")
    count = 0
    for x in a:
        count+=1
    print("length of strring : ",count)

    find_again = input("Want to find again? (y/n): ")
    if find_again.lower() != "y":
        break