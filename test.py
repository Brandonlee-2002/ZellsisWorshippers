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

# this snippet gives all series of a tournament, given the tournament's matching id
body3 = """
{ 
  tournament(id: 758074) {
    id
    name
    teams {
      id name
    }
  }

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

sixseven = requests.post(
    "https://api-op.grid.gg/central-data/graphql/",
    headers=headers,
    json = {"query":body3}
)

data = response.json()

wthelly = kekw.json()

why = sixseven.json()

print(why)

with open("tournaments_output.json", "w") as f:
    json.dump(data, f, indent=4)

with open("game_id_tournament.json", "w") as f:
    json.dump(wthelly, f, indent=4)

with open("teams_list_tournament.json", "w") as f:
    json.dump(why, f, indent=4)