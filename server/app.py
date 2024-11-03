from flask import Flask, request
from flask_cors import CORS
import json
from ai import process_data

from util import get_link_data

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


@app.route('/embed', methods=['GET'])
def get_embed():
    link = request.args.get('link')
    if link:
        info = get_link_data(link)
        return info
    else:
        return "No link provided", 400
    
@app.route('/rec', methods=['GET'])
def get_rec():
    recommendations = {
        "gaming": [
            { "link": 'https://www.nichepursuits.com/popular-blogs/', "confidence": 0.9 },
            { "link": 'https://firstsiteguide.com/examples-of-blogs/', "confidence": 0.85 },
            { "link": 'https://masterblogging.com/best-blog-examples/', "confidence": 0.8 },
            { "link": 'https://www.wpbeginner.com/showcase/best-blog-examples/', "confidence": 0.75 },
            { "link": 'https://www.ryrob.com/blog-examples/', "confidence": 0.7 }
        ],
        "music": [
            { "link": 'https://www.nichepursuits.com/popular-blogs/', "confidence": 0.9 },
            { "link": 'https://firstsiteguide.com/examples-of-blogs/', "confidence": 0.85 },
            { "link": 'https://masterblogging.com/best-blog-examples/', "confidence": 0.8 },
            { "link": 'https://www.wpbeginner.com/showcase/best-blog-examples/', "confidence": 0.75 },
            { "link": 'https://www.ryrob.com/blog-examples/', "confidence": 0.7 }
            ],
        "shows": [
            { "link": 'https://www.nichepursuits.com/popular-blogs/', "confidence": 0.9 },
            { "link": 'https://firstsiteguide.com/examples-of-blogs/', "confidence": 0.85 },
            { "link": 'https://masterblogging.com/best-blog-examples/', "confidence": 0.8 },
            { "link": 'https://www.wpbeginner.com/showcase/best-blog-examples/', "confidence": 0.75 },
            { "link": 'https://www.ryrob.com/blog-examples/', "confidence": 0.7 }
            ],
        "movies": [
            { "link": 'https://www.nichepursuits.com/popular-blogs/', "confidence": 0.9 },
            { "link": 'https://firstsiteguide.com/examples-of-blogs/', "confidence": 0.85 },
            { "link": 'https://masterblogging.com/best-blog-examples/', "confidence": 0.8 },
            { "link": 'https://www.wpbeginner.com/showcase/best-blog-examples/', "confidence": 0.75 },
            { "link": 'https://www.ryrob.com/blog-examples/', "confidence": 0.7 }
            ],
        "news": [
            { "link": 'https://www.nichepursuits.com/popular-blogs/', "confidence": 0.9 },
            { "link": 'https://firstsiteguide.com/examples-of-blogs/', "confidence": 0.85 },
            { "link": 'https://masterblogging.com/best-blog-examples/', "confidence": 0.8 },
            { "link": 'https://www.wpbeginner.com/showcase/best-blog-examples/', "confidence": 0.75 },
            { "link": 'https://www.ryrob.com/blog-examples/', "confidence": 0.7 }
            ],
        "tech": [
            { "link": 'https://www.nichepursuits.com/popular-blogs/', "confidence": 0.9 },
            { "link": 'https://firstsiteguide.com/examples-of-blogs/', "confidence": 0.85 },
            { "link": 'https://masterblogging.com/best-blog-examples/', "confidence": 0.8 },
            { "link": 'https://www.wpbeginner.com/showcase/best-blog-examples/', "confidence": 0.75 },
            { "link": 'https://www.ryrob.com/blog-examples/', "confidence": 0.7 }
            ],
        "sports": [
            { "link": 'https://www.nichepursuits.com/popular-blogs/', "confidence": 0.9 },
            { "link": 'https://firstsiteguide.com/examples-of-blogs/', "confidence": 0.85 },
            { "link": 'https://masterblogging.com/best-blog-examples/', "confidence": 0.8 },
            { "link": 'https://www.wpbeginner.com/showcase/best-blog-examples/', "confidence": 0.75 },
            { "link": 'https://www.ryrob.com/blog-examples/', "confidence": 0.7 }
            ],
    }

    return recommendations

if __name__ == '__main__':
    app.run(debug=True)