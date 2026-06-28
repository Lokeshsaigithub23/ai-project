def build_payload(
    article,
    caption,
    hashtags,
    image,
    video,
    selected_platforms
):
    """
    Build the raw payload for publishing.

    Platform-specific formatting will be handled later
    in zernio_client.py using the formatter module.
    """

    return {
        "article": article,
        "caption": caption,
        "hashtags": hashtags,
        "image": image,
        "video": video,
        "platforms": selected_platforms
    }