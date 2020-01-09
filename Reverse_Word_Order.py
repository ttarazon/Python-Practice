# This script takes a string and reverses it


def reversed_func(arg_parm):
    arg_parm = arg_parm[::-1]
    return arg_parm

user_list = input("Please enter a sentence and I will reverse it : " )

print("The original string is :", end="")
print(user_list)

print("The reversed string is ", end="")
print(reversed_func(user_list))








