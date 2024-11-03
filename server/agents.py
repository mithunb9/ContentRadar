from openai import OpenAI
from search import search_google
import os

client = OpenAI(
    api_key=('dc4d7e8c-98c0-4dc6-b6c6-67879269d31f'),
    base_url="https://api.sambanova.ai/v1",
)


def data_collection_agent(interests):
    # Use LLM to analyze and generate search queries
    response = client.chat.completions.create(
        model='Meta-Llama-3.1-405B-Instruct',
        messages=[
            {"role": "system", "content": """You are a precise data collector focused on gathering current information.
Analyze user interests to generate targeted search queries.
Your task:
1. Review user data patterns
2. Generate 2-3 specific search queries that will find current, factual information
3. Format each query on a new line
Focus on recent content and complementary topics."""},
            {"role": "user", "content": f"User Interests:\n{interests}"}
        ],
        temperature=0.3
    )

    # Get current data from search
    search_data = search_google({"q": response.choices[0].message.content})
    return search_data


def categorization_agent(interests, search_data):
    response = client.chat.completions.create(
        model='Meta-Llama-3.1-405B-Instruct',
        messages=[
            {"role": "system", "content": """Analyze and categorize the provided interests and data into a structured format.
Output format:
Primary Categories: [Gaming, Shows, Movies, News, Tech, Sports, Music]
Key Interests: [List 3-5 specific interests under each relevant category]
Cross-Category Connections: [List 2-3 strong connections between different categories]
Use bullet points and be specific."""},
            {"role": "user", "content": f"User Data:\n{interests}\nSearch Results:\n{search_data}"}
        ],
        temperature=0.3
    )
    return response.choices[0].message.content


def trend_analysis_agent(search_data):
    response = client.chat.completions.create(
        model='Meta-Llama-3.1-405B-Instruct',
        messages=[
            {"role": "system", "content": """Analyze the data to identify patterns and trends.
Focus on:
1. Consistent patterns in interests
2. Recent changes in behavior
3. Evolution of interests
Format your response as:
Current Trends:
- [Trend]: [Evidence]"""},
            {"role": "user", "content": f"Data to Analyze:\n{search_data}"}
        ],
        temperature=0.4
    )
    return response.choices[0].message.content


def recommendation_agent(interests, categories, trends):
    search_query_response = client.chat.completions.create(
        model='Meta-Llama-3.1-405B-Instruct',
        messages=[
            {"role": "system", "content": """Generate 3 highly specific search queries to find current recommendations.
Requirements:
- Each query should target different content types (e.g., games, shows, articles)
- Include release dates, ratings, or popularity metrics
- Focus on content released in the last 6 months
- Format each query on a new line"""},
            {"role": "user", "content": f"Interests: {interests}\nCategories: {categories}\nTrends: {trends}"}
        ],
        temperature=0.4
    )

    search_results = []
    for query in search_query_response.choices[0].message.content.split('\n'):
        if query.strip():  # Only search non-empty queries
            results = search_google({"q": query})
            search_results.append(results)

    response = client.chat.completions.create(
        model='Meta-Llama-3.1-405B-Instruct',
        messages=[
            {"role": "system", "content": """Generate 5 highly specific recommendations based on the user's profile.
Output format for each recommendation:
1. [Title] - [Type] - [Platform/Source] - link
   •confidence: [1.00-10.00]

Come up with a top 5 recommendations for all of the following: Gaming, Shows, Movies, News, Tech, Sports, Music

Ensure recommendations are:
- Currently available
- Use only real, non-hallucinated links
- From different categories
- Released or significantly updated in the last year
- Supported by actual metrics/ratings"""},
            {"role": "user",
             "content": f"Interests: {interests}\nCategories: {categories}\nTrends: {trends}\nCurrent Popular Content: {search_results}"}
        ],
        temperature=0.7
    )
    return response.choices[0].message.content