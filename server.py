from flask import Flask, jsonify, request
import json, os
from pyngrok import ngrok

app = Flask(__name__)

msg = []

@app.route('/', methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
        return jsonify(msg)
    elif request.method == 'POST':
        body = request.args.get('msg')
        msg.append(json.loads(body))
        return ''

@app.route('/delete', methods=['POST'])
def delete():
    global msg
    msg = []
    print(msg)
    return ''

http = ngrok.connect(5000)
http = http.public_url.strip('http://').strip('.ngrok.io')

print('Ngrok code: ' + http)

if __name__ == "__main__":
    app.run(debug=True)
