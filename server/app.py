from flask import Flask, request
from util import get_link_data

app = Flask(__name__)

@app.route('/html', methods=['GET'])
def accept_html():
    html = request.args.get('html')
    return html

@app.route('/embed', methods=['GET'])
def get_embed():
    link = request.args.get('link')
    if link:
        info = get_link_data(link)
        return info
    else:
        return "No link provided", 400

if __name__ == '__main__':
    app.run(debug=True)
    