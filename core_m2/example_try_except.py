import time

import requests

users = {
    "Bob Sponge": ["098700", "06722222"],
    "Bill Murey": ["0766633"],
    "Ann Dou": []
}


def get_data(user_name, indx):
    try:
        return users[user_name][indx]
    except KeyError as key_error:
        print(f"Error: {key_error}")
        return f'{user_name} not found'
    except IndexError as endx_error:
        print(f"Error: {endx_error}")
        return f"User {user_name} dont have phone with index {indx}"
    except Exception as error:
        print(f"Error: {error.args}")


phone = get_data("Bob Sponge", 2)
print(phone)


def refresh_key():
    return 'new api key'


def get_response(api_key):
    try:
        response = requests.get("https://google.com", data={"api_key": api_key})
        if response.status_code == 200:
            print("OK: data is correct")
        elif response.status_code == 401:
            print("Not auth")
            api_key = refresh_key()
            get_response(api_key)
        elif response.status_code == 500:
            time.sleep(10)
            get_response(api_key)
    except Exception as error:
        return f"ERROR: {error}"
