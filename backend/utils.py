def normalize_yes_no(value):
    """
    Ensures values are always 'Yes' or 'No'
    """
    if isinstance(value, str):
        return "Yes" if value.lower() in ["yes", "y", "true"] else "No"
    return "No"


def format_assessment(row):
    """
    Converts raw metadata into API-ready format
    """
    return {
        "url": row["url"],
        "name": row["name"],
        "adaptive_support": normalize_yes_no(row["adaptive_support"]),
        "description": row["description"],
        "duration": int(row["duration"]),
        "remote_support": normalize_yes_no(row["remote_support"]),
        "test_type": row["test_type"] if isinstance(row["test_type"], list)
                     else [row["test_type"]],
    }
