def validate_twitter(content):

    issues = []

    if len(content) > 280:
        issues.append("Twitter character limit exceeded.")

    hashtag_count = content.count("#")

    if hashtag_count > 5:
        issues.append("Too many hashtags for Twitter.")

    return issues