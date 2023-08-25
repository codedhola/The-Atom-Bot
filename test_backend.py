import requests
import json

# Specify the URL for the POST request
register_url = 'http://127.0.0.1:5000/register'
login_url = 'http://127.0.0.1:5000/login'




###REGISTER
# Create a dictionary with the data you want to send
payload = {
    'username': 'my_username',
    'password': 'my_password',
    'first_name': 'John',
    'last_name': 'Doe'
}

# # Make the POST request with JSON data
# response = requests.post(register_url, json=payload)

# print(response.text)
# response_data = json.loads(response.text)
# print(response_data["message"])

######LOGIN
# Create a dictionary with the data you want to send
payload = {
    'username': 'my_username',
    'password': 'my_password',
    'first_name': 'John',
    'last_name': 'Doe'
}

# Make the POST request with JSON data
response = requests.post(register_url, json=payload)

print(response.text)
response_data = json.loads(response.text)


print(response_data)
