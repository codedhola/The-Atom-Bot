from flask import Flask, request, jsonify

app = Flask(__name__)



@app.route('/register', methods=['POST'])
def register():
    pass

@app.route('/login', methods=['GET'])
def login():
    pass





if __name__ == '__main__':
    app.run(debug=True)












