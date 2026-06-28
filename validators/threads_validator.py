def validate_threads(content):

    issues = []

    if len(content) > 500:
        issues.append("Threads post is too long.")

    return issues