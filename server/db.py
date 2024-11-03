import os
from datetime import datetime

import iris
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
tableDefinition = "(id IDENTITY, platform VARCHAR(50), timestamp TIMESTAMP PRIMARY KEY, content TEXT, embedding VECTOR(DOUBLE, 384))"
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
    results = cursor.fetchall()
    return results


add_documents_to_vector_store(process_data())

# Close connection when done
cursor.close()
conn.close()