import requests
from requests.exceptions import HTTPError
import sys


# takes a url and parameters to make a GET request to the integers API and return the response
def get_code_list(URL, PARAMS):
    # getting the response with the 4 random numbers from then API:
    try:
        response = requests.get(
            url=URL, params=PARAMS)
        # If the response was successful, no Exception will be raised
        response.raise_for_status()
    except HTTPError as http_err:
        sys.exit(f'HTTP error occurred : {http_err}')  # Python 3.6
    except Exception as err:
        sys.exit(f'Other error occurred: {err}')  # Python 3.6

    # a list of number strings from the response
    num_str_list = response.text.splitlines()
    # converting num_strings to  integers
    # code_list = [int(num) for num in num_str_list]

    return num_str_list


def count_white(x):
    pass


def count_black(x):
    pass
