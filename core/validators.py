def validate_platform(platform, image=None, video=None):
    """
    Validate platform-specific publishing rules.
    """

    platform = platform.lower()

    # Instagram requires media
    if platform == "instagram":

        if not image and not video:
            return False, "Instagram requires an image or video."

    # LinkedIn
    elif platform == "linkedin":
        return True, "Valid"

    # Facebook
    elif platform == "facebook":
        return True, "Valid"

    # Twitter/X
    elif platform == "twitter":
        return True, "Valid"

    # Threads
    elif platform == "threads":
        return True, "Valid"

    # Reddit
    elif platform == "reddit":
        return True, "Valid"

    # Telegram
    elif platform == "telegram":
        return True, "Valid"

    # Bluesky
    elif platform == "bluesky":
        return True, "Valid"

    return True, "Valid"