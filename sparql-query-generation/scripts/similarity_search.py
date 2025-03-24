import numpy as np
from sentence_transformers import SentenceTransformer

# Load the model
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# Example sentences
sentences = ["What is the function of the gene BRCA1?", "Find all proteins involved in apoptosis."]

# Compute embeddings
embeddings = model.encode(sentences)

# Save embeddings
np.save('data/processed/embeddings.npy', embeddings)
