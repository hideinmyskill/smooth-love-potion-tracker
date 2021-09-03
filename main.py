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

#isko_list = {"mark": "ronin:666382e01b0af19a026f77b33f9ed82863271950",
           #  "Berto Lang": "ronin:2b58d7ddde59063f208462ae9a7cd7cd618172ec",
           # "Nelson": "ronin:23598112e88e82505e836bd65451d80c80acc0a7",
           # "Marj": "ronin:6040c9af3b02317b28c9547b51170c7ee8f8b853",
           #  "Kraaam": "ronin:9fa04682c8222cd3bd13737e1b0a71bfc61ba9c5"}

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
