MIN_LENGTH = 3

password = str(input("Enter a password: "))
while len(password) < MIN_LENGTH:
    print("Password should be longer than {} characters.".format(MIN_LENGTH))
    password = str(input("Enter a password: "))

for i in password:
    print("*", end=' ')


