from flask import Flask, request

app = Flask(__name__)

@app.route('/html', methods=['GET'])
def accept_html():
    html = request.args.get('html')
    return html

if __name__ == '__main__':
    app.run(debug=True)
