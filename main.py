import llm

user=llm.login("atom101", "atom")
session = llm.UserSession(user)



while True:
    user_input = input("USER: ")
    response = session.ProcessPrompt(user_input)
    print(response)



