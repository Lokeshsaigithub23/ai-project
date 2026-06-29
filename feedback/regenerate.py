from core.llm_engine import ask_llm


def regenerate_content(
    topic,
    article,
    caption,
    hashtags,
    feedback
):

    prompt = f"""
You are improving AI-generated social media content.

Topic:
{topic}

Current Article:
{article}

Current Caption:
{caption}

Current Hashtags:
{hashtags}

User Feedback:
{feedback}

Regenerate ALL the content according to the feedback.

Return ONLY in this exact format:

ARTICLE:
<new article>

CAPTION:
<new caption>

HASHTAGS:
<new hashtags>
"""

    response = ask_llm(prompt)

    article = ""
    caption = ""
    hashtags = ""

    current = None

    for line in response.splitlines():

        text = line.strip()

        if text.upper() == "ARTICLE:":
            current = "article"
            continue

        elif text.upper() == "CAPTION:":
            current = "caption"
            continue

        elif text.upper() == "HASHTAGS:":
            current = "hashtags"
            continue

        if current == "article":
            article += text + "\n"

        elif current == "caption":
            caption += text + "\n"

        elif current == "hashtags":
            hashtags += text + "\n"

    return {
        "article": article.strip(),
        "caption": caption.strip(),
        "hashtags": hashtags.strip(),
    }