def validate_linkedin(content):

    issues = []

    if len(content) > 3000:
        issues.append("LinkedIn post exceeds 3000 characters.")

    return issues