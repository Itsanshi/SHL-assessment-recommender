# FAISS-based retrieval system
import faiss
import pickle
import numpy as np

class AssessmentRetriever:
    def __init__(self, index_path, metadata_path):
        self.index = faiss.read_index(index_path)
        with open(metadata_path, 'rb') as f:
            self.metadata = pickle.load(f)
    
    def search(self, query_embedding, k=5):
        """Search for top-k similar assessments"""
        distances, indices = self.index.search(query_embedding, k)
        return indices, distances
