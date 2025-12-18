import pandas as pd
from backend.retriever import retrieve

df = pd.read_csv("train.csv")
recalls = []

for q in df["Query"].unique():
    gt = df[df["Query"] == q]["Assessment_url"].tolist()
    preds = retrieve(q, k=10)
    pred_urls = [p["url"] for p in preds]

    recall = len(set(gt) & set(pred_urls)) / len(gt)
    recalls.append(recall)

print("Mean Recall@10:", sum(recalls)/len(recalls))
