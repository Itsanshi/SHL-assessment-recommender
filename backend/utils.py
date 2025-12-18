# Utility functions
import pandas as pd
import numpy as np

def load_catalog(path):
    """Load SHL catalog from CSV"""
    return pd.read_csv(path)

def preprocess_text(text):
    """Preprocess text for embedding"""
    return text.lower().strip()

def calculate_similarity(embedding1, embedding2):
    """Calculate cosine similarity between embeddings"""
    return np.dot(embedding1, embedding2) / (np.linalg.norm(embedding1) * np.linalg.norm(embedding2))
