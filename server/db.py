import os
from datetime import datetime

import iris
import numpy as np
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
from ai import process_data

# Load environment variables (e.g., for database credentials)
load_dotenv()

# Initialize embedding model (Sentence-BERT in this case)
model = SentenceTransformer('all-MiniLM-L6-v2')

# Configure IRIS connection
username = os.getenv("IRIS_USERNAME", "demo")
password = os.getenv("IRIS_PASSWORD", "demo")
hostname = os.getenv('IRIS_HOSTNAME', 'localhost')
port = '1972'
namespace = 'USER'
CONNECTION_STRING = f"{hostname}:{port}/{namespace}"

# Connect to InterSystems IRIS
conn = iris.connect(CONNECTION_STRING, username, password)
cursor = conn.cursor()

# Create table for storing document embeddings
tableName = "DocumentSchema.DocumentEmbeddings"
tableDefinition = "(id IDENTITY PRIMARY KEY, platform VARCHAR(50), timestamp TIMESTAMP, content TEXT, embedding VECTOR(DOUBLE, 384))"
cursor.execute(f"CREATE TABLE IF NOT EXISTS {tableName} {tableDefinition}")

# Function to add documents to the vector store (IRIS database)
def add_documents_to_vector_store(documents):
    sql = f"""
    INSERT INTO {tableName}
    (platform, timestamp, content, embedding)
    VALUES (?, ?, ?, TO_VECTOR(?, DOUBLE, 384))
    """

    # Prepare the list of tuples (parameters for each row)
    data = [
        (
            doc['platform'],
            datetime.strptime(doc['time'], "%Y-%m-%dT%H:%M:%SZ"),
            doc['text'],
            ','.join(map(str, model.encode(doc['text']).tolist()))
        )
        for doc in documents
    ]

    cursor.executemany(sql, data)
    conn.commit()

# Function to get all data between the specified time frame
def get_data():
    sql = f"""
        SELECT content
        FROM {tableName}
        """

    cursor.execute(sql)
    results = cursor.fetchall()
    return results

# Function to perform similarity search using vector search in IRIS SQL
def query_vector_store(query_text):
    query_embedding = model.encode(query_text).tolist()
    query_embedding_str = ','.join(map(str, query_embedding))

    sql = f"""
            SELECT TOP 5 platform, timestamp, content
    FROM {tableName}
    ORDER BY VECTOR_COSINE(embedding, TO_VECTOR(?, DOUBLE, 384)) DESC
        """
    cursor.execute(sql, [query_embedding_str])
    data = cursor.fetchall()

    # Calculate similarity between query and each document and return a weigjted percentage
    return data

# def calculate_similarity_percentage(query_embedding, document_embedding):
#     query_vector = np.array(query_embedding)
#     document_vector = np.array(document_embedding)
#     cosine_similarity = np.dot(query_vector, document_vector) / (np.linalg.norm(query_vector) * np.linalg.norm(document_vector))
#     similarity_percentage = cosine_similarity * 100
#     return similarity_percentage

# Function to get the weighted average similarity percentage of the top 5 similar documents
# def get_weighted_similarity_percentage(query_text):
#     results, query_embedding = query_vector_store(query_text)
#     total_similarity = 0
#
#     for result in results:
#         document_embedding = list(map(float, result[3].split(',')))
#         similarity_percentage = calculate_similarity_percentage(query_embedding, document_embedding)
#         total_similarity += similarity_percentage
#
#     weighted_similarity_percentage = total_similarity / len(results) if results else 0
#     return weighted_similarity_percentage

data = query_vector_store("Among Us Secret Roles and Game Modes")