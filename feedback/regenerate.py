from core.llm_engine import ask_llm

def regenerate_content(topic, feedback):

    prompt = f"""
Topic:
{topic}

User Feedback:
{feedback}

Regenerate:

1. Professional Article
2. Social Media Caption
3. Relevant Hashtags

Follow the feedback exactly.
"""

    response = ask_llm(prompt)

    return {
        "article": response,
        "caption": "",
        "hashtags": ""
    }