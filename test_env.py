from dotenv import load_dotenv
import os

loaded = load_dotenv()

print("Loaded:", loaded)

key = os.getenv("OPENAI_API_KEY")

if key:
    print("SUCCESS")
    print(key[:20] + "...")
else:
    print("FAILED")