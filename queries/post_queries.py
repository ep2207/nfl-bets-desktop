from tkinter import messagebox
import requests
import json
from functions import sanitizeInput


def getMatches():

    data={"unit-code":"khlnjmkn-jbnkz-miff-898f"}
    url = "https://nflbets-51ac322b191f.herokuapp.com/matches-d"

    headers = {"Content-Type": "application/json"}
    response = requests.post(url, data=json.dumps(data), headers=headers, verify=True)

    
    print (response.status_code)
    if response.status_code == 200:
        
        return response.json()
    else:
        print(f"Failed to post data. Status code: {response.status_code}")
        return None
    

def postCommentary(match_id, commentary):

    clean_comment = sanitizeInput(commentary)

    data={"unit-code":"khlnjmkn-jbnkz-miff-898f","match-id": match_id, "commentary":clean_comment}
    url = "https://nflbets-51ac322b191f.herokuapp.com/commentary-d"

    headers = {"Content-Type": "application/json"}
    response = requests.post(url, data=json.dumps(data), headers=headers, verify=True)

    
    print (response.status_code)
    if response.status_code == 200:
        messagebox.showwarning("Success", "Commentary posted! swap matches to see your comment appear.")

        return response.json() 
    else:
        print(f"Failed to post data. Status code: {response.status_code}")
        return None
    

def closeMatch(matchAndBetsData):

    data={"unit-code":"khlnjmkn-jbnkz-miff-898f"}
    data.update(matchAndBetsData) #append data 
    url = "https://nflbets-51ac322b191f.herokuapp.com/close-match-d"

    headers = {"Content-Type": "application/json"}
    response = requests.post(url, data=json.dumps(data), headers=headers, verify=True)

    
    print (response.status_code)
    if response.status_code == 200:
        
        return response.json() 
    else:
        print(f"Failed to post data. Status code: {response.status_code}")
        return None
    
