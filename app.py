from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to my Flask app deployed on Render!"

@app.route('/hello')
def hello():
    return "Hello, Ankit!"

if __name__ == '__main__':
    app.run(debug=True)
