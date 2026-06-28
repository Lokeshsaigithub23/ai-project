def format_twitter(caption, hashtags):

    text = f"{caption}\n\n{hashtags}"

    if len(text) > 280:
        text = text[:277] + "..."

    return text