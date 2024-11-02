from flask import Flask, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app) 

@app.route('/html', methods=['GET'])
def accept_html():
    html = request.args.get('html')
    return html

@app.route('/text', methods=['POST'])
def accept_text():
    text = request.data
    return text

if __name__ == '__main__':
    app.run(debug=True)
