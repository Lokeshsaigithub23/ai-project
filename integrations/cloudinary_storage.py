import cloudinary
import cloudinary.uploader

cloudinary.config(
    cloud_name="de8svb12g",
    api_key="748953524598481",
    api_secret="qzxqajVnKRkBkZQBjVAxa8RITFg",
    secure=True
)


def upload_image_to_cloudinary(image_path):
    """
    Upload image to Cloudinary.
    Returns public HTTPS URL.
    """

    result = cloudinary.uploader.upload(
        image_path,
        resource_type="image"
    )

    print("=" * 80)
    print("IMAGE UPLOADED TO CLOUDINARY")
    print(result["secure_url"])
    print("=" * 80)

    return result["secure_url"]


def upload_video_to_cloudinary(video_path):
    """
    Upload video to Cloudinary.
    Returns public HTTPS URL.
    """

    result = cloudinary.uploader.upload(
        video_path,
        resource_type="video"
    )

    print("=" * 80)
    print("VIDEO UPLOADED TO CLOUDINARY")
    print(result["secure_url"])
    print("=" * 80)

    return result["secure_url"]