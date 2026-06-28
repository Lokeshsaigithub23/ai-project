def validate_bluesky(content):

    issues = []

    if len(content) > 300:
        issues.append("Bluesky character limit exceeded.")

    return issues