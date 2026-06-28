import mimetypes

from integrations.mongodb import get_gridfs


def upload_image(uploaded_file):
    """
    Upload image to MongoDB GridFS.
    Returns GridFS file id.
    """

    fs = get_gridfs()

    content_type = uploaded_file.content_type

    if not content_type:
        content_type = mimetypes.guess_type(uploaded_file.name)[0]

    file_id = fs.put(

        uploaded_file.read(),

        filename=uploaded_file.name,

        content_type=content_type

    )

    print("=" * 60)
    print("IMAGE SAVED TO MONGODB")
    print("FILE ID :", file_id)
    print("=" * 60)

    return str(file_id)

def upload_video(uploaded_file):

    fs = get_gridfs()

    content_type = uploaded_file.content_type

    if not content_type:
        content_type = mimetypes.guess_type(uploaded_file.name)[0]

    file_id = fs.put(
        uploaded_file.read(),
        filename=uploaded_file.name,
        content_type=content_type
    )

    print("=" * 60)
    print("VIDEO SAVED TO MONGODB")
    print("FILE ID :", file_id)
    print("=" * 60)

    return str(file_id)