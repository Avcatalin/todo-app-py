password = input("Enter new password: ")

result = {}

# check length of the password
if len(password) >= 8:
    result["length"] = True
else:
    result["length"] = False

# check if isdigit
digit = False

for i in password:
    if i.isdigit():
        digit = True

result["digits"] = digit

# check if is uppercase
uppercase = False

for i in password:
    if i.isupper():
        uppercase = True

result["upper-case"] = uppercase

if all(result.values()):
    print("Strong Password")
else:
    print("Weak Password")