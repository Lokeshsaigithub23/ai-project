import os
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv
from pymongo import MongoClient
import gridfs

# Load .env from the project root
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

MONGODB_URI = os.getenv("MONGODB_URI")

print("=" * 60)
print("Mongo URI Loaded:")
print(MONGODB_URI)
print("=" * 60)

if not MONGODB_URI:
    raise Exception("MONGODB_URI not found in .env")

client = MongoClient(    MONGODB_URI,
                           serverSelectionTimeoutMS=5000
)

db = client["social_media"]

fs = gridfs.GridFS(db)


def get_database():
    return db


def get_gridfs():
    return fs


def test_connection():
    try:
        client.admin.command("ping")
        print("=" * 60)
        print("✅ MongoDB Connected Successfully")
        print("=" * 60)
        return True

    except Exception as e:
        print("=" * 60)
        print("❌ MongoDB Connection Failed")
        print(e)
        print("=" * 60)
        return False
    

    from datetime import datetime

# ------------------------------
# USER EXPERIENCE FEEDBACK
# ------------------------------
def save_user_feedback(rating, feedback):

    collection = db["user_feedback"]

    document = {
        "rating": int(rating),
        "feedback": feedback,
        "created_at": datetime.utcnow()
    }

    result = collection.insert_one(document)

    return result.inserted_id