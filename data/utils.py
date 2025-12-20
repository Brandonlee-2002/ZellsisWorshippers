import dotenv
import requests
import os

dotenv.load_dotenv()
GRID_API_KEY = os.getenv("GRID_API_KEY")

def fetch_team():
    pass

def fetch_tournament():
    pass

def fetch_from_grid(
        body:str,
        url:str = "https://api-op.grid.gg/central-data/graphql/",
        api_key:str = GRID_API_KEY,
) -> requests.Response:
    headers = {
        "x-api-key": api_key
    }

    res = requests.post(
        url,
        headers=headers,
        json = {'query': body}
    )

    return res.json()
