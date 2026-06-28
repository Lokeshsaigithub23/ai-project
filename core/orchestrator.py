from generators.article_generator import generate_article
from generators.caption_generator import generate_caption
from generators.hashtag_generator import generate_hashtags

from core.content_assembler import assemble_content
from core.validation_engine import validate_content


def run(topic=None, image_path=None):

    article = generate_article(
        topic=topic,
        image_path=image_path
    )

    caption = generate_caption(
        topic=topic,
        image_path=image_path
    )

    hashtags = generate_hashtags(
        topic=topic,
        image_path=image_path
    )

    platform_content = assemble_content(
        article,
        caption,
        hashtags
    )

    validation_results = validate_content(
        platform_content
    )

    return {
        "article": article,
        "caption": caption,
        "hashtags": hashtags,
        "platform_content": platform_content,
        "validation": validation_results
    }