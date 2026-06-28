from core.llm_engine import (
    ask_llm,
    ask_llm_image,
    ask_llm_image_with_text
)


def generate_hashtags(topic=None, image_path=None):

    # TEXT + IMAGE

    if topic and image_path:

        prompt = """
Generate 10 hashtags.

Use BOTH the uploaded image and the user's topic.

Return ONLY hashtags.
"""

        return ask_llm_image_with_text(
            topic,
            prompt,
            image_path
        )

    # IMAGE ONLY

    if image_path:

        prompt = """
Generate 10 hashtags from this image.

Return ONLY hashtags.
"""

        return ask_llm_image(
            prompt,
            image_path
        )

    # TEXT ONLY

    prompt = f"""
Generate 10 hashtags for:

{topic}

Return ONLY hashtags.
"""

    return ask_llm(prompt)