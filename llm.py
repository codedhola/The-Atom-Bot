
import requests
url = 'http://127.0.0.1:5000/'

def login(username, password):
    
    data = {
        'username': username,
        'password': password
    }
    headers = {'Content-Type': 'application/json'}
    r_url = url+"login"
    response = requests.get(r_url, json=data, headers=headers)
    return response.json()


class UserSession:
    def __init__(self, user=None):
        self.user_info=user

    def start_session(self):
        pass
        

    def ProcessPrompt(self, prompt):
        return f"hello {self.user_info}"