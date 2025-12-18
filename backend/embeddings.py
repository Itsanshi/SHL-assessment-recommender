import pandas as pd
import faiss
import pickle
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

df = pd.read_csv("data/shl_catalog.csv")
texts = (df["name"] + " " + df["description"]).tolist()

embeddings = model.encode(texts, show_progress_bar=True)

index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

faiss.write_index(index, "data/faiss.index")
pickle.dump(df.to_dict(), open("data/metadata.pkl", "wb"))
