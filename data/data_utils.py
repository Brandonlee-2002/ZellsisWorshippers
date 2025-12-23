from utils.consts import GRID_API_KEY
import requests

def fetch_from_grid(
        query:str,
        fragment:str = None,
        url:str = "https://api-op.grid.gg/central-data/graphql/",
        api_key:str = GRID_API_KEY,
) -> requests.Response:
    headers = {
        "x-api-key": api_key
    }

    req_json = {
        "query": query
    }

    if fragment:
        req_json["fragment"] = fragment

    res = requests.post(
        url,
        headers=headers,
        json = req_json
    )

    return res.json()
