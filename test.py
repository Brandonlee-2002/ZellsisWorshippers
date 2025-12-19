import json

import requests

headers = {
    "x-api-key": "t79SFuwUHNIVNndQ5qUZsdszfpgXqST5MLRIa3G5"
}

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


body2 = """
{
  tournament(id: 757087) {
    id
    name
    titles {
      id
      name
      }
    }
}"""

body3 = """
{
    
}
"""
response = requests.post(
    "https://api-op.grid.gg/central-data/graphql/",
    headers=headers,
    json = {"query":body}
)

kekw = requests.post(
    "https://api-op.grid.gg/central-data/graphql/",
    headers=headers,
    json = {"query":body2}
)

data = response.json()

wthelly = kekw.json()

print(kekw)

with open("tournaments_output.json", "w") as f:
    json.dump(data, f, indent=4)

with open("brandon is a dumb bitch.json", "w") as f:
    json.dump(wthelly, f, indent=4)

