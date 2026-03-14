import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from job_data_loader import load_jobs

model = SentenceTransformer("all-MiniLM-L6-v2")

# Load job dataset
jobs_df = load_jobs()

job_titles = jobs_df["title"].tolist()
job_descriptions = jobs_df["description"].tolist()

# Convert job descriptions to embeddings
job_embeddings = model.encode(job_descriptions)

job_embeddings = np.array(job_embeddings).astype("float32")

# Create FAISS index
index = faiss.IndexFlatL2(job_embeddings.shape[1])
index.add(job_embeddings)


def recommend_jobs_vector(resume_text, top_k=5):

    resume_embedding = model.encode([resume_text]).astype("float32")

    distances, indices = index.search(resume_embedding, top_k)

    results = []

    for idx in indices[0]:

        results.append(job_titles[idx])

    return results