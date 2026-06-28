from core.llm_engine import (
    ask_llm,
    ask_llm_image,
    ask_llm_image_with_text
)


def generate_caption(topic=None, image_path=None):

    # TEXT + IMAGE

    if topic and image_path:

        prompt = """
Generate a professional social media caption.

Use BOTH the uploaded image and the user's topic.

Keep it under 2 sentences.
"""

        return ask_llm_image_with_text(
            topic,
            prompt,
            image_path
        )

    # IMAGE ONLY

    if image_path:

        prompt = """
Generate a professional caption for this image.

Keep it under 2 sentences.
"""

        return ask_llm_image(
            prompt,
            image_path
        )

    # TEXT ONLY

    prompt = f"""
Generate a caption for:

{topic}

Keep it under 2 sentences.
"""

    return ask_llm(prompt)