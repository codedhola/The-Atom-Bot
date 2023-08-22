import openai
import os
import json
from typing import List
from pydantic import BaseModel, Field, validator


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
    if username == None or password == None:
        return {"message": "missing password or username"}
    else:
        id = "4dfghj678"
        return json.dumps({"message": f"User {username} resgistered succesfully with ID {id}"})


# Schemas
class FuctionRegister(BaseModel):
    username: str = Field(description="username of new user")
    password: str = Field(description="password for user")
    
    
    def to_json(self):
        return json.dumps(self.dict())
    
class FuctionWeather(BaseModel):
    location: str = Field(description="message to send to person")
    unit: str = Field(description="unit ceilsuis or fahrenheit")
    
    
    def to_json(self):
        return json.dumps(self.dict())
    


# Fuctions Description
functions=[
                {
                    "name": "register_new_user",
                    "description": "create a new user with password",
                    "parameters": FuctionRegister.schema()
                },
                {
                    "name": "get_current_weather",
                    "description": "get weather of a location",
                    "parameters": FuctionWeather.schema()
                },
        ]

def run_conversation():
    messages = []

    while True:
        # Capture user message
        user_message_content = input("You: ")
        
        if user_message_content.lower() == "exit":
            print("Exiting the conversation.")
            break
        
        messages.append({"role": "user", "content": user_message_content})

        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            functions=functions,
            function_call="auto",
        )
        response_message = response["choices"][0]["message"]
        print("GPT:", response_message["content"])

        # Check if GPT wanted to call a function
        if response_message.get("function_call"):
            # Call the function
            available_functions = {
                "get_current_weather": get_current_weather,
                "register_new_user": register_new_user,
            } 
            function_name = response_message["function_call"]["name"]
            function_to_call = available_functions[function_name]
            function_args = json.loads(response_message["function_call"]["arguments"])
            function_response = function_to_call(**function_args)
            
            print("response from function:", function_response)

            # Send the info on the function call and function response to GPT
            messages.append(response_message)
            messages.append(
                {
                    "role": "function",
                    "name": function_name,
                    "content": function_response,
                }
            )

# Note: Ensure that `model`, `functions`, `get_current_weather`, and `register_new_user` are defined 
# somewhere in your code, as they are being referenced in the above code.

run_conversation()