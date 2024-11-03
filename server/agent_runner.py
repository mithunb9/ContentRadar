import os
from openai import OpenAI
from dotenv import load_dotenv
import json
from search import search_google
from agents import (data_collection_agent, categorization_agent,
                    trend_analysis_agent, recommendation_agent)


print("Starting recommendation system...")
load_dotenv()

# Create two separate clients for different APIs
client = OpenAI(
    api_key=('dc4d7e8c-98c0-4dc6-b6c6-67879269d31f'),
    base_url="https://api.sambanova.ai/v1",
)



def analyze_interests(data):
    print("Analyzing user interests...")
    response = client.chat.completions.create(
        model='Meta-Llama-3.1-8B-Instruct',
        messages=[
            {"role": "system", "content": """You are an expert interest analyzer. Extract key interests, 
            preferences, and patterns from user data. Focus on:
            1. Main topics of interest
            2. prefrences
            3. Content consumption patterns
            4. Level of expertise in different areas
            Output should be structured and concise."""},
            {"role": "user", "content": data}
        ],
        temperature=0.3,
        top_p=0.1
    )
    print("Interest analysis completed")
    return response.choices[0].message.content


def generate_recommendations(interests, search_data):
    print("Generating personalized recommendations...")
    response = client.chat.completions.create(
        model='Meta-Llama-3.1-8B-Instruct',
        messages=[
            {"role": "system", "content": """You are a recommendation specialist. Based on the user's interests 
            and search data, provide personalized recommendations in these categories:
            1. Games they might enjoy
            2. Content they should explore
            3. Communities they might want to join
            4. Learning resources for their interests
            5. Related topics they might like
            Format recommendations clearly with explanations why each would appeal to them."""},
            {"role": "user", "content": f"User Interests: {interests}\nSearch Data: {search_data}"}
        ],
        temperature=0.7,
        top_p=0.1
    )
    print("Recommendations generated")
    return response.choices[0].message.content


def process_user_data(data):
    try:
        print("\n=== Starting Multi-Agent Analysis ===")

        # Initial interest analysis
        interests = analyze_interests(data)

        # Agent 1: Data Collection
        search_data = data_collection_agent(interests)
        print("Data collection complete")

        # Agent 2: Categorization
        categories = categorization_agent(interests, search_data)
        print("Interest categorization complete")

        # Agent 3: Trend Analysis
        trends = trend_analysis_agent(search_data)
        print("Trend analysis complete")

        # Agent 4: Final Recommendations
        recommendations = recommendation_agent(interests, categories, trends)

        final_output = {
            "user_interests": interests,
            "categories": categories,
            "trends": trends,
            "recommendations": recommendations
        }

        return json.dumps(final_output, indent=2)

    except Exception as e:
        print(f"Error in processing: {str(e)}")
        return f"Error processing user data: {str(e)}"


# Keep existing generate_query function
def generate_query(data):
    print("Generating search query for additional context...")
    response = client.chat.completions.create(
        model='Meta-Llama-3.1-8B-Instruct',
        messages=[
            {"role": "system",
             "content": "Generate a search query to find additional information related to these user interests. Focus on finding new but relevant content."},
            {"role": "user", "content": data}
        ],
        temperature=0.1,
        top_p=0.1
    )
    query = response.choices[0].message.content
    query = ''.join([c for c in query if c.isalnum() or c.isspace()])
    return {"q": query}


# Process the test data
if __name__ == "__main__":
    from db import query_vector_store
    from datetime import datetime
    from db import get_data

    # Get data from the database
    results = get_data()

    # Fallback if no data is found
    if not results:
        results = """
        I enjoy playing strategy games like Civilization and Age of Empires.
        I frequently watch tech reviews and programming tutorials.
        Recently started learning Python and machine learning.
        """

    print("\n=== Starting Recommendation System ===")
    result = process_user_data(results)
    print("\nFinal Recommendations:")
    print(result)