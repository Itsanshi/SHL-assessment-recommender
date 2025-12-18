import pandas as pd
from backend.retriever import retrieve

test = pd.read_csv("test.csv")
rows = []

for q in test["Query"]:
    results = retrieve(q, k=10)
    for r in results:
        rows.append([q, r["url"]])

out = pd.DataFrame(rows, columns=["Query", "Assessment_url"])
out.to_csv("submission.csv", index=False)
