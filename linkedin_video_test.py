import requests

API_KEY = "sk_6cc4d5d9c646918666abdbfcb672664596c0f105a481e393648382b249a25c3b"

ACCOUNT_ID = "6a3e93179d9472faaef42dc7"

VIDEO_URL = "https://drive.google.com/uc?export=download&id=11REZznQPs_3tKaxkuuHEgsvdKDiYu0zc"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

payload = {
    "content": "LinkedIn video test from standalone script",
    "publishNow": True,
    "platforms": [
        {
            "platform": "linkedin",
            "accountId": ACCOUNT_ID
        }
    ],
    "mediaItems": [
        {
            "type": "video",
            "url": VIDEO_URL
        }
    ]
}

print("=" * 80)
print("REQUEST PAYLOAD")
print(payload)
print("=" * 80)

try:
    response = requests.post(
        "https://zernio.com/api/v1/posts",
        headers=headers,
        json=payload,
        timeout=300
    )

    print("=" * 80)
    print("STATUS :", response.status_code)
    print("RESPONSE :")
    print(response.text)
    print("=" * 80)

except Exception as e:
    print("ERROR:", e)