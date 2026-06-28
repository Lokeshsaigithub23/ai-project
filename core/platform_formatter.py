from formatters.linkedin_formatter import format_linkedin
from formatters.facebook_formatter import format_facebook
from formatters.instagram_formatter import format_instagram
from formatters.twitter_formatter import format_twitter
from formatters.reddit_formatter import format_reddit
from formatters.bluesky_formatter import format_bluesky
from formatters.threads_formatter import format_threads
from formatters.telegram_formatter import format_telegram


def build_platform_content(article, caption, hashtags):
    return {
        "linkedin": format_linkedin(article, caption, hashtags),
        "facebook": format_facebook(article, caption, hashtags),
        "instagram": format_instagram(caption, hashtags),
        "twitter": format_twitter(caption, hashtags),
        "reddit": format_reddit(article, caption, hashtags),
        "bluesky": format_bluesky(caption, hashtags),
        "threads": format_threads(caption, hashtags),
        "telegram": format_telegram(article, caption, hashtags)
    }