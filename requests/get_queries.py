import requests
import json


def getMatches():

    data={"unit-code":"khlnjmkn-jbnkz-miff-898f"}
    url = "https://nflbets-51ac322b191f.herokuapp.com/matches-d"

    headers = {"Content-Type": "application/json"}
    response = requests.post(url, data=json.dumps(data), headers=headers, verify=False)

    
    print (response.status_code)
    if response.status_code == 200:
        
        print(response.json())
        return response.json()  # assuming the server responds with JSON data
    else:
        print(f"Failed to post data. Status code: {response.status_code}")
        return None
    
