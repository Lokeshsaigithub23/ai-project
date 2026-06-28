def validate_facebook(content):

    issues = []

    if len(content) > 5000:
        issues.append("Facebook post is too long.")

    return issues