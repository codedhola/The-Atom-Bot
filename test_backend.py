import requests
import json

# Specify the URL for the POST request
register_url = 'http://127.0.0.1:5000/register'
login_url = 'http://127.0.0.1:5000/login'


#Solution to Assignment
inventory_url = 'http://127.0.0.1:5000/inventory'




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
 #  'first_name': 'John',
# 'last_name': 'Doe'
}


######Solution for the Assignment
# Create a dictionary with the data you want to send
payload = {
    'product_name': 'ACE_LAPTOP',
    'product_price': '$500',
    'product_description': 'This is an ACE_Embedded Laptop'   
}






# Make the POST request with JSON data
response = requests.get(login_url, json=payload)

print(response.text)
response_data = json.loads(response.text)


print(response_data)
