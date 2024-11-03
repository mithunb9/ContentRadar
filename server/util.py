import requests
from bs4 import BeautifulSoup

def get_link_data(url):
    # Fetch the HTML content of the URL
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract Open Graph metadata
    og_data = {
        "title": soup.find("meta", property="og:title")["content"] if soup.find("meta", property="og:title") else None,
        "description": soup.find("meta", property="og:description")["content"] if soup.find("meta", property="og:description") else None,
        "image": soup.find("meta", property="og:image")["content"] if soup.find("meta", property="og:image") else None,
        "url": soup.find("meta", property="og:url")["content"] if soup.find("meta", property="og:url") else url,
        "site_name": soup.find("meta", property="og:site_name")["content"] if soup.find("meta", property="og:site_name") else None
    }
    
    return og_data
