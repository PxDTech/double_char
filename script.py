# Double Char
# Codewars 8 kyu kata
# Given a string, you have to return a string in which each character (case-sensitive) is repeated once.
# Examples (Input -> Output):
# * "String"      -> "SSttrriinngg"
# * "Hello World" -> "HHeelllloo  WWoorrlldd"
# * "1234!_ "     -> "11223344!!__  "
# Good Luck!

def double_char(s):
    new_string = ""
    for c in s:
        new_string = new_string + c + c
    return new_string

print(double_char("1234!_ "))
