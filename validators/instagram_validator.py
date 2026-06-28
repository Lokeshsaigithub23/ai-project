def validate_instagram(content):

    issues = []

    if len(content) > 2200:
        issues.append("Instagram caption exceeds 2200 characters.")

    hashtag_count = content.count("#")

    if hashtag_count > 30:
        issues.append("Instagram allows a maximum of 30 hashtags.")

    return issues