import pandas as pd

df = pd.read_csv("shl_raw.csv")

df = df[~df["name"].str.contains("Job Solution", case=False)]
df["test_type"] = "Knowledge & Skills"  # improve later
df["duration"] = 60
df["adaptive_support"] = "No"
df["remote_support"] = "Yes"

df.to_csv("../backend/data/shl_catalog.csv", index=False)
