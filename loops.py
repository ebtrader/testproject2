raw = 'asdfaab'
functions = [str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper]

for func in functions:
    print (any (func(letter) for letter in raw))





