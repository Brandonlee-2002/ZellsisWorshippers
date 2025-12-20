import requests
import pprint

def post_to_api(url, body):
    response = requests.post(
    url,
    headers={"x-api-key": "t79SFuwUHNIVNndQ5qUZsdszfpgXqST5MLRIa3G5"},
    json = {"query": body}
    )

    if response.status_code == 200:
        print("Successful POST request.")
        try:
            pprint.pprint(response.json())
        except requests.exceptions.JSONDecodeError as e:
            print(f"Error deconding response: {e}")
    else:
        bad_response = response.status_code
        print(f"Request failed with status code: {bad_response}")

url = "https://api-op.grid.gg/central-data/graphql/"

body = """
    {
      tournaments {
        pageInfo {
          hasPreviousPage
          hasNextPage
          startCursor
          endCursor
        }
        totalCount
        edges {
          cursor
          node {
            ...tournamentFields
          }
        }
      }
    }
    fragment tournamentFields on Tournament {
      id
      name
      nameShortened
    }"""

post_to_api("https://api-op.grid.gg/central-data/graphql/", body)
