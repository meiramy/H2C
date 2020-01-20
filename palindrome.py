
while True:
    word = input("Enter a phrase to test: ")
    word = word.replace(" ","")
    print()

    word = word.upper()
    if word == word[::-1]:
        print("The word is a palindrome")
    else:
        print("It is not a palindrome")
    print()

    another = input("Another test (Y/N)?")

    if (another == "N") or (another == "n"):
        print("Terminating the program")
        break
       
