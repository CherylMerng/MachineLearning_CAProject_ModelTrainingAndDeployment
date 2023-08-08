from flask import Flask, request, jsonify
from waitress import serve


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello world!"

@app.route('/sayhello/', methods=['GET','POST'])
def say_hello():
    name = request.args.get('name') or request.form.get('name')    
    return "Hello " + str(name or '')

# run the server
if __name__ == '__main__':
    print("Starting the server.....")
    serve(app, host="0.0.0.0", port=8070)
