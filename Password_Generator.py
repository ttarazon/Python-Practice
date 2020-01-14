import string
import random

length_var = input("How many characters do you want your password to be : ")


def rando_pass_func(length_var):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(alphabet) for i in range(int(length_var)))
    print(password)


rando_pass_func(length_var)

