from utils.consts import GRID_API_KEY
import requests

def fetch_all_tournaments():
    hasNext = True

    tournament_query = """



    """

    while hasNext:
        data = fetch_from_grid()



def fetch_from_grid(
        query:str,
        variables: str = None,
        url:str = "https://api-op.grid.gg/central-data/graphql/",
        api_key:str = GRID_API_KEY,
) -> requests.Response:
    headers = {
        "x-api-key": api_key
    }

    req_json = {
        "query": query
    }

    if variables:
        req_json["variables"] = variables

    res = requests.post(
        url,
        headers=headers,
        json=req_json
    )

    return res.json()
