string = input("Enter a word to check whether it is a palindrome or not :")
string = string.casefold()
reverse = reversed(string)

if list(string) == list(reverse):
    print("The String is a palindrome")
else:
    print("The String is not a palindrome")
