"""this code will ask the user to enter password and chaeck if the password is up
to 8 characters, contains letters and numbers"""


# 1. define my function
# def get_password(password):

# 2. Assign what i want to see in the password
#has_numbers = False
#has_letters = False

# 3. Check the length of the password using python inbuilt function len()
# if len(password) < 8:
#   return "password must be 8 characters long"

# 4. loop through each character using for loop and use if statement if it met my standard
# for char in password:
#    if char.isdigit():
#      has_numbers = True
# elif char.isalph():
#      has_letters = True


# 5. using if statement to return message based on what was found, still in the for loop
# if has_numbers and has_letters:
#     return "Strong password"
# elif has_numbers or has_letters:
#     return "Medium password, please add letters and numbers"
# else 
#   return " Weak password try again"

# Add a while True loop so that it will keep asking until is true"
# while True:
#      user_input = input("Enter your password")
#      result = get_password(user_input)
#      print(result)

# break the while True loop using if statement
# if result == "Strong password"
#    break





def get_password(password):
    has_numbers = False
    has_letters = False

    if len(password) < 8:
        return "Password must be 8 characters long"

    for char in password:
        if char.isdigit():
            has_numbers = True
        elif char.isalpha():
            has_letters = True

    if has_numbers and has_letters:
        return "Strong password"
    elif has_numbers or has_letters:
        return "Medium password, please add letters and numbers"
    else:
        return "Weak password! Try again"


while True:
    user_input = input("Enter your password: ")
    result = get_password(user_input)
    print(result)

    if result == "Strong password":
        break