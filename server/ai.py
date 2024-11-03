import os

from dotenv import load_dotenv
from openai import OpenAI

from search import search_google

load_dotenv()

client = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY'),
    base_url=os.getenv('OPENAI_API_URL'),
)

def generate_query(data):
    response = client.chat.completions.create(
        model='Meta-Llama-3.1-8B-Instruct',
        messages=[{"role":"system","content":"You are an assistant that determines given the data what is the best Google search query that you need to learn more about the topic. Output should be one line formatted like a google query."},{"role":"user","content":data}],
        temperature =  0.1,
        top_p = 0.1
    )

    query = response.choices[0].message.content

    # Remove any non-alphanumeric characters from the query
    query = ''.join([c for c in query if c.isalnum() or c.isspace()])
    return {"q": query}

def generate_insight(data, search_data):
    response = client.chat.completions.create(
        model='Meta-Llama-3.2-3B-Instruct',
        messages=[
            {"role":"system","content":"""
             Summarize the given data and Google search results in a structured format. Use the following guidelines to ensure consistency:

            - **Data Summary**: Analyze and summarize the provided data in 5 sentences.
            - **Google Search Results**: Provide a separate 5-sentence summary for each search result, clearly separated by a newline.

            - Ensure there are no duplicates and no other text or labels. """},
            {"role":"user","content":f"Original Data: {data}"},
            {"role":"user","content":f"Serper Search Results: {search_data}"}
        ],
        temperature=0.1,
        top_p=0.1
    )

    insight = response.choices[0].message.content
    return insight
    
def process_data(data):
    query_obj = generate_query(data)

    search_data = search_google(query_obj)  

    from datetime import datetime
    insight_lines = generate_insight(data, search_data).replace("**Google Search Results**", "").replace("**Data Summary**", "").split("\n")
    filtered_lines = [line for line in insight_lines if line.strip() != ""]
    
    return [{"content": line, "platform": "web", "time": datetime.now().isoformat()} for line in filtered_lines]




