import requests
from requests.exceptions import HTTPError
from util import get_code_list
import sys


# URL to access the API
URL = "https://www.random.org/integers/"

# API parameters

PARAMS = {
    'num': 4,  # num digits requested
    'min': 0,  # min int
    'max': 4,  # max int
    'col': 1,
    'base': 10,
    'format': 'plain',
    'rnd': 'new'
}

# function inside util.py accesses API to generate code list in string format
code_str_list = get_code_list(URL, PARAMS)
print(code_str_list)

code_str = "".join(code_str_list)

# 110

tries = 1
limit = 10

n = input(" Pick 4 numbers between 0 and 7 to guess the 4 digit code:")


while (n != code_str and tries < limit):

    # variable increments every time the loop
    # is executed, giving an idea of how many
    # guesses were made.
    tries += 1

# like the boardgame, black = count of correct number + location, white = correct # only
    black = 0
    white = 0

    # explicit type conversion of an integer to
    # a string in order to ease extraction of digits
    n = str(n)

    # explicit type conversion of a string to an integer
    # num = str(num)

    # # correct[] list stores digits which are correct
    # correct = ['X']*4

    # for loop runs 4 times since the number has 4 digits.
    black_temp_code = code_str_list.copy()
    white_temp_code = code_str_list.copy()
    for i in range(0, len(code_str_list)):
        # print('i', i)
        # print('n', n)
        # print('length n', len(n))
        # print('length code str list', len(code_str_list))

        # checking for equality of digits
        if (n[i] == black_temp_code[i]):
            # number of digits + locations guessed correctly increments
            black += 1

        if(n[i] in white_temp_code):
            white += 1
            # print('temp_code before white match', white_temp_code)
            # print('i', i)
            # print('n[i]', n[i])
            white_temp_code.remove(n[i])
            # print('temp_code after white match', white_temp_code)

    # print('white', white)
    # print('black', black)
    white = white-black

    # when not all the digits are guessed correctly.
    if (black != 4):
        if (white > 0):
            print(f"You got {white} digits correct")
        if (black > 0):
            print(f"You got {black} digits annd their location correct")

        print(f"you have {limit-tries} tries remaining")

        print('\n')
        print('\n')
        n = (input("Enter your next choice of numbers: "))

    # when none of the digits are guessed correctly.
    elif (black == '0' and white == '0'):
        print("None of the numbers in your input match.")
        n = (input("Enter your next choice of numbers: "))

# condition for equality.
if n == code_str:
    print("You've become a Mastermind!")
    print(f"It took you only {tries}, tries.")
else:
    print(
        f"I'm sorry, you've exceeded {limit} tries. The code is {code_str}. You'll get it next time!")
