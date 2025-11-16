import json
import os


def bucketParser(meta):
    headline = meta.get("headline")
    print(headline)

    backlog_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "backlog.json")

    # Ensure file exists
    if not os.path.exists(backlog_path):
        with open(backlog_path, "w") as f:
            f.write("{}")

    # Load existing JSON safely
    with open(backlog_path, "r", encoding="utf-8") as log:
        content = log.read().strip()
        if not content:
            data = {}
        else:
            try:
                data = json.loads(content)
            except json.JSONDecodeError:
                # If file is corrupted, reset to empty dict rather than crashing
                data = {}

    # If headline already exists, do not add again
    if headline in data:
        return False

    # Add new entry and write file back
    data[headline] = meta
    with open(backlog_path, "w", encoding="utf-8") as log:
        json.dump(data, log, indent=4)

    return True