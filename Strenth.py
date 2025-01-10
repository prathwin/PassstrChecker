import string

# Predefined password for testing
password = input("Enter the password: ")

upper_case = any(c in string.ascii_uppercase for c in password)
lower_case = any(c in string.ascii_lowercase for c in password)
special = any(c in string.punctuation for c in password)
digits = any(c in string.digits for c in password)

characters = [upper_case, lower_case, special, digits]

length = len(password)

score = 0

# Check if the password is in the common password list
try:
    with open('common.txt', 'r') as f:
        common = f.read().splitlines()
    if password in common:
        print("Password found in common list. Score: 0/7")
        exit()
except FileNotFoundError:
    print("Warning: common.txt file not found. Skipping common password check.")

# Scoring based on length
if length > 8:
    score += 1
if length > 12:
    score += 1
if length > 17:
    score += 1
if length > 20:
    score += 1

print(f"Password length is {length}, adding {score} points.")

# Scoring based on character types
if sum(characters) > 1:
    score += 1
if sum(characters) > 2:
    score += 1
if sum(characters) > 3:
    score += 1

print(f"Password has {sum(characters)} different character types, adding {sum(characters) - 1} points.")

# Final evaluation
if score < 4:
    print(f"The password is quite weak! Score: {score}/7")
elif score == 4:
    print(f"The password is ok! Score: {score}/7")
elif score > 4 and score < 6:
    print(f"The password is pretty good! Score: {score}/7")
else:
    print(f"The password is strong! Score: {score}/7")
