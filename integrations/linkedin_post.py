def validate_telegram(content):

    issues = []

    if len(content) > 4096:
        issues.append("Telegram message exceeds 4096 characters.")

    return issues