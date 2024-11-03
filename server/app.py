from flask import Flask, request
from flask_cors import CORS
import json
from ai import process_data


app = Flask(__name__)
CORS(app) 

@app.route('/html', methods=['GET'])
def accept_html():
    html = request.args.get('html')
    return html

@app.route('/text', methods=['POST'])
def accept_text():
    print("REQUEST RECIEVED")
    # Decode the byte data and then parse it as JSON
    data = json.loads(request.data.decode("utf-8"))
    text = data.get("text")  # Extract the "text" field from the JSON object
    url = data.get("url")
    timestamp = data.get("timestamp")

    print(process_data(text))
    return "text"


if __name__ == '__main__':
    app.run(debug=True)
    