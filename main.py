import requests
from bs4 import BeautifulSoup
import json

def tracker(ronin_add, name):
    ronin = ronin_add.replace("ronin:", "0x")
    url = "https://api.lunaciarover.com/stats/" + str(ronin)

    r = requests.get(url)

    # Getting the soup / source code API response
    soup = BeautifulSoup(r.text, "lxml")
    capture_dict = soup.find("p").text

    #convert the string dictionary to dictionary
    dic = json.loads(capture_dict)

    print("Player name: " + str(name))
    print("Total SLP farmed: " + str(dic.get("total_slp")))
    print("Player's current rank: " + str(dic.get("rank")))
    print("Player's current MMR:  " + str(dic.get("mmr")))
    print("Last SLP claimed: " + str(dic.get("last_claim_timestamp")))
    print(dic)

def banner():
    res = """
            *********************************************************
                **         **   ********  **      **   **********
                ** **      **   **          **   **        **
                **    **   **   ********      **           **
                **      ** **   **          **   **        **
                **        ***   ********   **      **      **
            **********************************************************
            
            """
    return print(res)

while True:
    try:
        # Open a text file that contains the name and ronin address in dictionary.
        js = open("ronin_address.txt", "r")
        data = json.load(js)
        js.close()
        break

    except:
        print("ronin_address.txt not found")
        exit()

for index, (key, value) in enumerate(data.items()):
   res = tracker(value, key)
   banner()
