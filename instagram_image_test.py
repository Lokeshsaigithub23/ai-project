import requests

API_KEY = "sk_6cc4d5d9c646918666abdbfcb672664596c0f105a481e393648382b249a25c3b"

ACCOUNT_ID = "6a3e95af9d9472faaef44d1c"

BASE_URL = "https://zernio.com/api/v1"

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

payload = {
    "content": "Instagram image test from standalone script",
    "publishNow": True,
    "platforms": [
        {
            "platform": "instagram",
            "accountId": ACCOUNT_ID
        }
    ],
    "mediaItems": [
        {
            "type": "image",
            "url": "https://upload.wikimedia.org/wikipedia/commons/3/3f/JPEG_example_flower.jpg"
        }
    ]
}

print("=" * 80)
print("REQUEST PAYLOAD")
print(payload)
print("=" * 80)

response = requests.post(
    f"{BASE_URL}/posts",
    headers=HEADERS,
    json=payload,
    timeout=120
)

print("=" * 80)
print("STATUS :", response.status_code)
print("RESPONSE :")
print(response.text)
print("=" * 80)