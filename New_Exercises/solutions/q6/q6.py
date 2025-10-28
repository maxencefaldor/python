from collections import Counter
import os


def get_error_summary(logfile):
    error_counts = Counter()

    # Resolve logfile relative to this file's directory to ensure tests find fixtures
    base_dir = os.path.dirname(__file__)
    log_path = os.path.join(base_dir, logfile)

    try:
        with open(log_path, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue

                parts = line.split(maxsplit=2)
                if len(parts) == 3 and parts[1] == "[ERROR]":
                    message = parts[2]
                    error_counts[message] += 1
    except FileNotFoundError:
        return {}

    return dict(error_counts)
