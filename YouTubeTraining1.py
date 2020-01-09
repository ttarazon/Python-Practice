def translate(phrase):
    xlate_var = ""
    for letter_var in phrase:
        if letter_var.lower() in "aeiou":
            if letter_var.isupper():
                xlate_var = xlate_var + "G"
            else:
                xlate_var = xlate_var + "g"
        else:
            xlate_var = xlate_var + letter_var
    return xlate_var


print(translate(input("Enter a phrase: ")))