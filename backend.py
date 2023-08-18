from flask import Flask, request, jsonify
import uuid

def generate_unique_id():
    return str(uuid.uuid4())


app = Flask(__name__)

# In-memory database
users = []
products = []
orders = []
appointments = []



@app.route('/register', methods=['POST']) #one endpoint/route
def register():
    data = request.json
    username = data['username']
    password = data['password']


    # Check if user already exists
    if username in users:
        return jsonify({"message": "User already exists!"}), 400

    users.append({
        'username': username,
        'password': password,
        'id': generate_unique_id()
    })

    return jsonify({"message": "User registered successfully!"})





if __name__ == '__main__':
    app.run(debug=True)












