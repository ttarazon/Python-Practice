name = input("Please enter your name ")
age = int(input("Now tell me how old you are "))

current_year = 2019
difference = 100 - age
hundred_year = current_year + difference

print("Hello " + name)
print("You said you are " + str(age) + " years old")
print("You will turn 100 years old in " + str(hundred_year))

counter = int(input("Now enter a number between 1 and 10 "))
x = 0
while x < counter:
    print("You will turn 100 years old in " + str(hundred_year))
    x += 1

