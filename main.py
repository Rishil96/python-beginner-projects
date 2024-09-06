# Python Password Generator
import random

print("Welcome to the PyPassword Generator!")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+',
           '=', '[', ']', '{', '}', '|', ';', ':', '<', '>', '/', '?', '~']

letter_count = int(input("How many letters would you like in your password?\n"))
symbol_count = int(input("How many symbols would you like?\n"))
number_count = int(input("How many numbers would you like?\n"))

password_list = []

# Get random letters
for i in range(0, letter_count):
    random_letter = random.choice(letters)
    password_list.append(random_letter)

# Get random numbers
for i in range(0, number_count):
    random_number = random.choice(numbers)
    password_list.append(random_number)

# Get random symbols
for i in range(0, symbol_count):
    random_symbol = random.choice(symbols)
    password_list.append(random_symbol)

# Shuffle password characters
random.shuffle(password_list)

password = ''.join(password_list)

print(f"Your password is: {password}")
