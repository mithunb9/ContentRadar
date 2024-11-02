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

print(process_data("""
             Google is currently fighting a lawsuit filed by the US labor department claiming gender discrimination. Officials of Google said it was too financially burdensome and logistically challenging to hand over salary records that the government requested in order to investigate.[53] A judge has however ordered Google to hand over salary records to the government in this ongoing investigation by the US Department of Labor.[54]

James Damore et al. v. Google, LLC
In a lawsuit filed January 8, 2018, multiple employees and job applicants alleged Google discriminated against a class defined by their “conservative political views[,] male gender[,] and/or […] Caucasian or Asian race”.[55]

Arne Wilberg v. Google, Inc.
On January 29, 2018, YouTube technical recruiter Arne Wilberg filed a suit accusing Google “of systematically discriminating in favor of job applicants who are Hispanic, African American, or female, and against Caucasian and Asian men.”[56]

Kelly Ellis et al VS. Google, Inc.
On August 14, 2017, three former employees of Google have filed a class action lawsuit against the internet company, alleging a pattern of discrimination against women workers, including systemically lower pay than their male counterparts. [57]

Microtransactions
In-app purchases class action
In 2014 a parent filed a class action lawsuit against Google for "in-app" purchases, which are microtransactions that can be made within applications.[58] This lawsuit followed a class action lawsuit and investigation by the Federal Trade Commission against Apple Inc. over similar complaints. (See Apple Inc. litigation -- In-app purchases class action). The parent contended that there is a 30-minute window during which authorizations can be made for credit card purchases that are designed to entice children to make such purchases in "free apps", and that Google should have been aware of the issue because of the Apple litigation.[58]

Epic Games v. Google
Main article: Epic Games v. Google
On August 13, 2020, Epic Games filed an antitrust lawsuit against Google following the removal of the Epic-developed game Fortnite from Google Play, after an update release allowed Epic to directly sell microtransactions, bypassing the 30 percent revenue share with Google. Epic alleges that Google is using the 30 percent revenue share imposed on developers to enforce a monopoly on development for Android.[59] Simultaneously, Epic filed a similar lawsuit against Apple Inc, which had also removed Fortnite from the App Store (iOS) for similar reasons.[60]

In October 2021, Google launched a counter-suit against Epic Games, asserting that Epic was in violation of its Play Store contract terms when it added a new Fortnite version without its payment system.[61]

Match Group v. Google
On May 9, 2022, Match Group sued Google over its strategic manipulation of markets and abuse of power where mandating Match Group to use Google's billing system to remain in the Google Play Store. The lawsuit, filed in the Northern District of California, accuses the company of deploying “anticompetitive tactics” to maintain a monopoly on the Android mobile ecosystem.[62]
             """))


