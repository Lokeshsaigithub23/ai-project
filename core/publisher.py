from integrations.zernio_client import publish_to_zernio
from core.payload_builder import build_payload


def publish_content(
    article,
    caption,
    hashtags,
    image,
    video,
    selected_platforms
):

    payload = build_payload(
        article,
        caption,
        hashtags,
        image,
        video,
        selected_platforms
    )

    print("=" * 80)
    print("PUBLISH PAYLOAD")
    print(payload)
    print("=" * 80)

    return publish_to_zernio(payload)