from validators.twitter_validator import validate_twitter
from validators.linkedin_validator import validate_linkedin
from validators.facebook_validator import validate_facebook
from validators.instagram_validator import validate_instagram
from validators.reddit_validator import validate_reddit
from validators.bluesky_validator import validate_bluesky
from validators.threads_validator import validate_threads
from validators.telegram_validator import validate_telegram


def validate_content(content):

    return {

        "twitter": validate_twitter(content["twitter"]),

        "linkedin": validate_linkedin(content["linkedin"]),

        "facebook": validate_facebook(content["facebook"]),

        "instagram": validate_instagram(content["instagram"]),

        "reddit": validate_reddit(content["reddit"]),

        "bluesky": validate_bluesky(content["bluesky"]),

        "threads": validate_threads(content["threads"]),

        "telegram": validate_telegram(content["telegram"])

    }