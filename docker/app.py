from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, this is simple web app!'

@app.route('/health')
def health():
    return {"status": "okay"}

@app.route('/api/data')
def data():
    return 'this is the data'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
