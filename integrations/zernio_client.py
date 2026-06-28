from core.validators import validate_platform
import requests

API_KEY = "sk_6cc4d5d9c646918666abdbfcb672664596c0f105a481e393648382b249a25c3b"

BASE_URL = "https://zernio.com/api/v1"

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}


def get_connected_accounts():

    response = requests.get(
        f"{BASE_URL}/accounts",
        headers=HEADERS
    )

    print("=" * 80)
    print("GET ACCOUNTS STATUS :", response.status_code)
    print(response.text)
    print("=" * 80)

    if response.status_code != 200:
        return {}

    data = response.json()

    accounts = {}

    if "accounts" in data:

        for account in data["accounts"]:

            platform = account["platform"].lower()
            account_id = account["_id"]

            accounts[platform] = account_id

    print("=" * 80)
    print("CONNECTED ACCOUNTS")
    print(accounts)
    print("=" * 80)

    return accounts


def publish_to_zernio(payload):

    connected_accounts = get_connected_accounts()

    results = {}

    for platform in payload["platforms"]:

        # -------------------------------
        # Platform Validation
        # -------------------------------

        is_valid, message = validate_platform(
            platform,
            payload.get("image"),
            payload.get("video")
        )

        if not is_valid:

            results[platform] = {
                "status": "failed",
                "message": message
            }

            continue

        platform = platform.lower()

        # -------------------------------
        # Connected Account Check
        # -------------------------------

        if platform not in connected_accounts:

            results[platform] = {
                "status": "failed",
                "message": "Account Not Connected"
            }

            continue

        # -------------------------------
        # Content
        # -------------------------------

        content = payload["caption"]

        if payload.get("article"):
            content = f"{payload['article']}\n\n{payload['hashtags']}"

        # -------------------------------
        # Request Body
        # -------------------------------

        body = {

            "content": content,

            "publishNow": True,

            "platforms": [
                {
                    "platform": platform,
                    "accountId": connected_accounts[platform]
                }
            ]
        }

        # -------------------------------
        # IMAGE (Disabled for now)
        # -------------------------------

        if payload.get("image"):
            body["mediaItems"] = [
                {
                    "type": "image",
                    "url": payload["image"]
                }
            ]
        print("=" * 80)
        print("PLATFORM :", platform)
        print("IMAGE URL :", payload.get("image"))
        print("IMAGE TYPE :", type(payload.get("image")))
        print("VIDEO URL :", payload.get("video"))
        print("CONTENT LENGTH :", len(content))
        print("REQUEST BODY :")
        print(body)
        print("=" * 80)

        # -------------------------------
        # VIDEO
        # -------------------------------

        if payload.get("video"):

            body["mediaItems"] = [
                {
                    "type": "video",
                    "url": payload["video"]
                }
            ]

        print("=" * 80)
        print("POST BODY")
        print(body)
        print("=" * 80)

        try:
            # -------------------------------
    # CHECK IMAGE URL BEFORE POSTING
    # -------------------------------
            image_url = payload.get("image")
            if image_url:
                try:
                    check = requests.get(image_url, timeout=30)
                    print("=" * 80)
                    print("IMAGE STATUS :", check.status_code)
                    print("CONTENT-TYPE :", check.headers.get("Content-Type"))
                    print("FINAL IMAGE URL :", check.url)
                    print("=" * 80)
                except Exception as e:
                    print("=" * 80)
                    print("IMAGE CHECK FAILED :", e)
                    print("=" * 80)

    # -------------------------------
    # SEND TO ZERNIO
    # -------------------------------    
                   
            print("=" * 80)
            print("STARTING REQUEST TO ZERNIO")
            print("Platform :", platform)
            print("Media Type :", "Video" if payload.get("video") else "Image")
            print("Image URL :", payload.get("image"))
            print("Video URL :", payload.get("video"))
            print("REQUEST BODY :")
            print(body)
            print("=" * 80)


            response = requests.post(
                f"{BASE_URL}/posts",
                headers=HEADERS,
                json=body,
                timeout=320
            )

            print("=" * 80)
            print("REQUEST FINISHED")
            print("POST STATUS :", response.status_code)
            print("POST RESPONSE :")
            print(response.text)
            print("RESPONSE HEADERS :")
            print(response.headers)
            print("REQUEST BODY :")
            print(body)
            print("=" * 80)
        except requests.exceptions.ReadTimeout:
            print("=" * 80)
            print("❌ Zernio request timed out after 120 seconds.")
            print("=" * 80)
            results[platform] = {
                "status": "failed",
                "message": "Zernio request timed out."
            }
            continue
        except requests.exceptions.RequestException as e:
            print("=" * 80)
            print("❌ Request Exception")
            print(e)
            print("=" * 80)
            results[platform] = {
                "status": "failed","message": str(e)
            }
            continue
            


        if response.status_code in [200, 201]:

            results[platform] = {
                "status": "success",
                "message": response.text
            }

        else:

            results[platform] = {
                "status": "failed",
                "message": response.text
            }

    return results