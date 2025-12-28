from utils.consts import GRID_API_KEY, LOL_TITLE_ID
import requests

def fetch_tournament_ids(cursor="", count=None):

    MAX_COUNT = 50
    hasNext = True

    res = []

    variables = {
        "gameId": LOL_TITLE_ID,
        "cursor": cursor,
        "count": MAX_COUNT
    }

    while hasNext and count > 0 :

        tournament_query = """
            query GetTournaments ($gameId: ID, $cursor: CURSOR, $count: SCALAR) {
                tournaments (
                    filter: {
                        titleId: $gameId,
                        hasParent: FALSE,
                    }
                    after: $cursor,
                    first: $count
                ) {
                    pageInfo {
                        hasNextPage
                        endCursor
                    }
                    edges {
                        cursor
                        node {
                            name
                            id
                            teams {
                                name
                                id
                            }
                        }
                    }
                }
            }
        """
        data = fetch_from_grid()

        res.append(data)

        hasNext = data['data']['pageInfo']['hasNextPage']
        count -= MAX_COUNT

    return res


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
