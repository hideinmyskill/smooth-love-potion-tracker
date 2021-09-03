import requests
from bs4 import BeautifulSoup
import json
import argparse

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
    print("Username: " + str(dic.get("ign")))
    print("Total SLP farmed: " + str(dic.get("total_slp")))
    print("Player's current rank: " + str(dic.get("rank")))
    print("Player's current MMR:  " + str(dic.get("mmr")))
    print("Last SLP claimed: " + str(dic.get("last_claim_amount")))


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


#initialized parser
parser = argparse.ArgumentParser(description='SLP scholar tracker bot')

#parameters
parser.add_argument('-a','--addr', metavar='', help='Enter the Ronin address')
parser.add_argument('-n', '--name', metavar='', help='Set a name for the the ronin address')
parser.add_argument('-f', '--file', metavar='', help='Enter file path of the dictionary')

#parse arguments
args = parser.parse_args()
if args.addr or args.name:
    tracker(args.addr, args.name)

elif args.file:
    while True:
        try:
            #Open a text file that contains the name and ronin address in dictionary.
            js = open(args.file, "r")
            data = json.load(js)
            js.close()
            break

        except:
            print("File not found")
            exit()

    for index, (key, value) in enumerate(data.items()):
        res = tracker(value, key)
        banner()
