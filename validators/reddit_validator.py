def validate_reddit(content):

    issues = []

    if len(content) > 40000:
        issues.append("Reddit post is too long.")

    return issues