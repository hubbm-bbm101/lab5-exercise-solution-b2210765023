def emailcheck(email):
    x = 0
    for chr in email:
        if chr == "@":
            x += 1
        if chr == ".":
            x += 1
        if x == 2:
            return True

if emailcheck(input("Please enter an e-mail: ")) == True:
    print("It is a valid e-mail")
else:
    print("It is not a valid e-mail")


