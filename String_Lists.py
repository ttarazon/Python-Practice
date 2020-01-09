
def reverse(placeholder):
    placeholder = "".join(reversed(placeholder))
    return placeholder

list_var = input("Please enter a phrase to see if it is a palindrome ")

print("Your word is : ", end="")
print(list_var)

print("The reversed word is  ", end="")
print(reverse(list_var))

if list_var == reverse(list_var):
    print("Your word is a palindrome")
else:
    print("Your word isn't a palindrome, try again")


