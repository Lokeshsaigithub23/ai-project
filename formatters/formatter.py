from .linkedin_formatter import format_linkedin
from .instagram_formatter import format_instagram
from .facebook_formatter import format_facebook
from .twitter_formatter import format_twitter


def get_platform_content(platform, article, caption, hashtags):

    platform = platform.lower()

    if platform == "linkedin":
        return format_linkedin(article, caption, hashtags)

    elif platform == "instagram":
        return format_instagram(article, caption, hashtags)

    elif platform == "facebook":
        return format_facebook(article, caption, hashtags)

    elif platform == "twitter":
        return format_twitter(article, caption, hashtags)

    return caption