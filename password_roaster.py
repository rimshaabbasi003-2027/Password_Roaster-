
#RoastMyPassword 
#Created by Rimsha Gul Niaz 
def password_checker(password):

    common_passwords = [
        "123456",
        "12345678",
        "password",
        "password123",
        "Hello",
        "admin"
    ]

    score = 0
    roasts = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        roasts.append("That password is shorter than my patience.")

    # Uppercase check
    if any(char.isupper() for char in password):
        score += 1
    else:
        roasts.append("No uppercase letters? Your password is whispering.")

    # Lowercase check
    if any(char.islower() for char in password):
        score += 1
    else:
        roasts.append("No lowercase letters? Are we shouting at the computer?")

    # Number check
    if any(char.isdigit() for char in password):
        score += 1
    else:
        roasts.append("Not a single digit? Bold strategy.")

    # Symbol check
    symbols = "!@#$%^&*()-_=+[]{};:,<.>/?"

    if any(char in symbols for char in password):
        score += 1
    else:
        roasts.append("No symbols? Thank you for keeping things easy for Hackers.")

    # Common password check
    if password.lower() in common_passwords:
        roasts.append("Originality has left the chat.")

    # Display score
    print("\n-------------------------")
    print("Password Strength:", score, "/ 5")

    if score <= 2:
        print("Overall: Weak")

    elif score <= 4:
        print("Overall: Medium")

    else:
        print("Overall: Strong")

    # Smug compliment
    if score == 5 and password.lower() not in common_passwords:
        print("You understood the assignment.")
    else:
        print("\n Roasts:")

        for roast in roasts:
            print("-", roast)


# Main loop

while True:

    password = input(
         "\n Enter a password (or type 'quit' to exit):"
    )

    if password.lower() == "quit":
        print("\n Goodbye!")
        break

    password_checker(password)
