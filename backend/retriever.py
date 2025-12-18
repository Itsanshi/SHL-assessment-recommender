import faiss, pickle
from sentence_transformers import SentenceTransformer
from utils import format_assessment

model = SentenceTransformer("all-MiniLM-L6-v2")
index = faiss.read_index("data/faiss.index")
meta = pickle.load(open("data/metadata.pkl", "rb"))


def retrieve(query, k=10):
    q_emb = model.encode([query])
    _, ids = index.search(q_emb, k)

    results = []
    for i in ids[0]:
        row = {
            "name": meta["name"][i],
            "url": meta["url"][i],
            "description": meta["description"][i],
            "test_type": meta["test_type"][i],
            "duration": meta["duration"][i],
            "adaptive_support": meta["adaptive_support"][i],
            "remote_support": meta["remote_support"][i],
        }
        results.append(format_assessment(row))

    return results
