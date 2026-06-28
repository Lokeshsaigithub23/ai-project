from PIL import Image
import os


def prepare_instagram_image(image_path):
    """
    Convert any image into a valid JPEG for Instagram.
    """

    img = Image.open(image_path)

    # Convert RGBA/P to RGB
    if img.mode != "RGB":
        img = img.convert("RGB")

    new_path = os.path.splitext(image_path)[0] + "_instagram.jpg"

    img.save(
        new_path,
        format="JPEG",
        quality=95
    )

    return new_path