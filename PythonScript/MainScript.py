# APS
import os
from dotenv import load_dotenv
load_dotenv()

#to trigger secret scanning
user = 'test'
password = 'Password1234'

google_api_token = "AIzaSyAQfxPJiounkhOjODEO5ZieffeBv6yft2Q"

def say_hello():
    print('hello world - test Ana 11')

    # critical vuln example
    user_input = input("Enter filename: ")
    with open(user_input, 'r') as file:  # Vulnerable to directory traversal
        content = file.read()

# main
if __name__ == '__main__':
    say_hello()


