import openai
import json
from pydantic import BaseModel, Field
import uuid

model = "gpt-3.5-turbo-0613"
api_key = ""
openai.api_key =api_key

# Function Definitions
def get_current_weather(location=None, unit="fahrenheit"):
    """Get the current weather in a given location"""
    weather_info = {
        "location": location,
        "temperature": "72",
        "unit": unit,
        "forecast": ["sunny", "windy"],
    }
    return json.dumps(weather_info)

def register_new_user(username=None, password=None):
    if username is None or password is None:
        return {"message": "missing password or username"}
    else:
        id = str(uuid.uuid4())[:8]  # Generate a random 8-character ID for users
        return json.dumps({"message": f"User {username} registered successfully with ID {id}"})

# Schemas
class FuctionRegister(BaseModel):
    username: str = Field(description="username of new user")
    password: str = Field(description="password for user")
    
    def to_json(self):
        return json.dumps(self.dict())

class FuctionWeather(BaseModel):
    location: str = Field(description="message to send to person")
    unit: str = Field(description="unit Celsius or fahrenheit")
    
    def to_json(self):
        return json.dumps(self.dict())

class LLM:
    def __init__(self, user_info=None, functions=None, model="gpt-3.5-turbo-0613"):
        self.user_info = user_info
        
        self.model = model
        self.messages = [
                # {
                # "role": "system",
                # "content": "You are helpful assitant called Atom. You can use your functions to execute the user request when needed, however you can also have regular conversation when a request is not made"
                # }
      ]

        if functions:
            self.functions = functions[0] 
            self.available_functions = functions[1]
        else:
            self.functions = []
            self.available_functions = {}

    def run_conversation(self):
        if not self.user_info:
            user_response = input("Do you want to (1) login or (2) register? ")
            # You can extend the user login/registration logic here.
            if user_response == "1":
                username = input("Enter your username: ")
                self.user_info = {"username": username}
            elif user_response == "2":
                username = input("Enter a new username: ")
                password = input("Enter a password: ")
                print(register_new_user(username, password))
                self.user_info = {"username": username}
            else:
                print("Invalid choice. Exiting.")
                return

        while True:
            user_message_content = input(f"{self.user_info['username']}: ")
            if user_message_content.lower() == "exit":
                print("Exiting the conversation.")
                break

            self.messages.append({"role": "user", "content": user_message_content})

            response = openai.ChatCompletion.create(
                model=self.model,
                messages=self.messages,
                functions=self.functions,
                function_call="auto",
            )
            response_message = response["choices"][0]["message"]
            print("GPT:", response_message["content"])

            if response_message.get("function_call"):
               
                function_name = response_message["function_call"]["name"]
                function_to_call = self.available_functions[function_name]
                function_args = json.loads(response_message["function_call"]["arguments"])
                function_response = function_to_call(**function_args)

                print("response from function:", function_response)
                self.messages.append(response_message)
                self.messages.append(
                    {
                        "role": "function",
                        "name": function_name,
                        "content": function_response,
                    }
                )

class Tooling:
    def __init__(self):
        self.functions = []
        self.actual_fuction_objects = {}

    def add_function(self, name, description, parameters_schema, the_function, required):
        function_info = {
            "name": name,
            "description": description,
            "parameters": parameters_schema,
            "required": required
        }
        self.functions.append(function_info)
        self.actual_fuction_objects.update({
            name:the_function
        })
        

    def get_all_functions(self):
        return self.functions, self.actual_fuction_objects

# Example of Usage:
tooling = Tooling()
# tooling.add_function("register_new_user", "create a new user with password", FuctionRegister.schema(), register_new_user, ["username", "password"])
tooling.add_function("get_current_weather", "get weather of a location", FuctionWeather.schema(), get_current_weather, ["location"])

chat = LLM(functions=tooling.get_all_functions())
chat.run_conversation()
