import os
import sys

import pandas as pd


def main():
    # Determine project root (one level up from this file's directory)
    this_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.dirname(this_dir)

    # Make backend importable
    backend_path = os.path.join(root_dir, "backend")
    if backend_path not in sys.path:
        sys.path.append(backend_path)

    from retriever import retrieve  # noqa: E402

    # Load test data
    test_path = os.path.join(this_dir, "test.csv")
    test_df = pd.read_csv(test_path)

    rows = []
    for q in test_df["job_description"]:
        results = retrieve(q, k=10)
        for r in results:
            rows.append({
                "Query": q,
                "Assessment_url": r["url"],
            })

    out_path = os.path.join(root_dir, "Anshika_Anand.csv")
    out_df = pd.DataFrame(rows, columns=["Query", "Assessment_url"])
    out_df.to_csv(out_path, index=False)


if __name__ == "__main__":
    main()
