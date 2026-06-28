from core.llm_engine import (
    ask_llm,
    ask_llm_image,
    ask_llm_image_with_text
)


def generate_article(topic=None, image_path=None):

    # ----------------------------
    # TEXT + IMAGE
    # ----------------------------

    if topic and image_path:

        prompt = """
Write a professional article.

Requirements:
- Use BOTH the uploaded image and the user's topic.
- Do not ignore either one.
- Maximum 5 lines.
- Around 80-120 words.
- Professional tone.
- Short introduction.
- Short conclusion.
"""

        return ask_llm_image_with_text(
            topic,
            prompt,
            image_path
        )

    # ----------------------------
    # IMAGE ONLY
    # ----------------------------

    if image_path:

        prompt = """
Analyze the uploaded image.

Write a short professional article based ONLY on the image.

Requirements:
- Maximum 5 lines.
- Around 80-120 words.
- Professional tone.
"""

        return ask_llm_image(
            prompt,
            image_path
        )

    # ----------------------------
    # TEXT ONLY
    # ----------------------------

    prompt = f"""
Write a professional article about:

{topic}

Requirements:
- Maximum 5 lines.
- Around 80-120 words.
- Professional tone.
- Easy to read.
- No bullet points.
"""

    return ask_llm(prompt)