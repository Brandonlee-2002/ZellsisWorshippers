import os
import dotenv

dotenv.load_dotenv()
GRID_API_KEY = os.getenv("GRID_API_KEY")
if not GRID_API_KEY:
    raise ValueError("GRID_API_KEY not set in .env file")

LOL_TITLE_ID = 3