import os
from dotenv import load_dotenv

load_dotenv()

ZERNIO_API_KEY = os.getenv("ZERNIO_API_KEY")
ZERNIO_BASE_URL = os.getenv("ZERNIO_BASE_URL")