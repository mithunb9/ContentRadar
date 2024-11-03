import os
from openai import OpenAI
from dotenv import load_dotenv
import json
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
            {"role":"system","content":"You are an assistant that generates insights about a topic given the original data and Google search results. Output should be in a consistent format. Also return some links to sources."},
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
    # print(json.dumps(query_obj))

    search_data = search_google(query_obj)
    # print(search_data)

    return generate_insight(data, search_data)


