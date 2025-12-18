"""Simple in-memory retriever so the API works without FAISS files.

This avoids loading a real FAISS index / metadata, which aren't present yet,
and instead returns a small set of hard-coded assessments based on keyword
matches in the query. This is enough for you to see end-to-end output in the
running app.
"""

from utils import format_assessment


SAMPLE_ASSESSMENTS = [
    {
        "name": "Cognitive Ability Test",
        "url": "https://www.shl.com/en/assessments/cognitive-ability/",
        "description": "Measures problem-solving, logical reasoning and learning agility.",
        "test_type": ["Cognitive", "Aptitude"],
        "duration": 30,
        "adaptive_support": "Yes",
        "remote_support": "Yes",
    },
    {
        "name": "Personality Assessment",
        "url": "https://www.shl.com/en/assessments/personality/",
        "description": "Assesses work style, behavioral preferences and cultural fit.",
        "test_type": ["Personality"],
        "duration": 25,
        "adaptive_support": "No",
        "remote_support": "Yes",
    },
    {
        "name": "Situational Judgment Test",
        "url": "https://www.shl.com/en/assessments/situational-judgment/",
        "description": "Evaluates decision-making in realistic workplace scenarios.",
        "test_type": ["Behavioral", "SJT"],
        "duration": 20,
        "adaptive_support": "Yes",
        "remote_support": "Yes",
    },
]


def _score(query: str, item: dict) -> int:
    """Very simple relevance score: count overlapping words in description/name."""

    q_tokens = {t.lower() for t in query.split() if t.strip()}
    text = f"{item['name']} {item['description']}".lower()
    return sum(1 for t in q_tokens if t in text)


def retrieve(query, k: int = 10):
    """Return up to k sample assessments ranked by a naive keyword score."""

    if not query:
        ranked = SAMPLE_ASSESSMENTS
    else:
        ranked = sorted(
            SAMPLE_ASSESSMENTS,
            key=lambda a: _score(query, a),
            reverse=True,
        )

    results = [format_assessment(row) for row in ranked[:k]]
    return results
