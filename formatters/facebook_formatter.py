def format_facebook(article, caption, hashtags):

    return f"""
{caption}

{article[:1500]}

{hashtags}
"""