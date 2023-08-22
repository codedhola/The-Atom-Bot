from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

# In-memory database
users = []
products = []
orders = []
appointments = []



# functions
def generate_unique_id():
    return str(uuid.uuid4())

def get_user_by_id(username, password):
    for user in users:
        if user['username'] == username and user['password'] == password:
            return user
    return None  # Return None if no user is found


@app.route('/register', methods=['POST']) #one endpoint/route
def register():
    data = request.json
    username = data['username']
    password = data['password']
    first_name = data['first_name']
    last_name = data['last_name']



    # Check if user already exists
    usernames = [u["username"] for u in users] #taking all usernames
    if username in usernames:
        return jsonify({"message": "User already exists!"}), 400

    users.append({
        'username': username,
        'password': password,
        'first_name':first_name,
        'last_name':last_name,
        'id': generate_unique_id()
    })

    return jsonify({"message": "User registered successfully!"})



@app.route('/', methods=['GET']) #one endpoint/route
def home():
    return jsonify({"message": "Hello there!"})


@app.route('/login', methods=['GET']) #one endpoint/route
def login():
    data = request.json
    username = data['username']
    password = data['password']
   

    # Check if user already exists
    usernames = [u["username"] for u in users]
    if username not in usernames:
        return jsonify({"message": "User dont  exist!"}), 400

    # Get user ID
    user = get_user_by_id(username, password)
    if user is None:
       return jsonify({"message": "User not found or incorrect credentials."}), 400
    print(user)
    return jsonify(user)



if __name__ == '__main__':
    app.run(debug=True)












