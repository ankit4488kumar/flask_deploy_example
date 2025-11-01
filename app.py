from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Flask on the intranet!"

if __name__ == '__main__':
    # Listen on all IPs so other devices can access it
    app.run(host='0.0.0.0', port=5000, debug=True)
`
