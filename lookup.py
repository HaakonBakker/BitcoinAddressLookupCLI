#Usage: python3 lookup.py ADDRESS
import requests
import sys


if (len(sys.argv) != 2):
    print("You need to supply the address.")

def performRequest(url):
    """ Will return the json object (dict) of the URL """
    # Perform get Requests
    resp = requests.get(url)

    if not resp.ok:
        print ("Something went wrong! {}".format(resp.status_code))
        return False

    return resp.json()

BASEURL = "https://blockchain.info/rawaddr/"
addressToLookup = sys.argv[1]
requestURL = BASEURL + addressToLookup

addressInfo = performRequest(requestURL)

# if addressInfo is False, then something went wrong
if addressInfo == False:
    print("The address was not found. Please check that the address is correct.")

def satoshiToBTC(sat):
    # 100000000
    satInOneBTC = 100000000
    btc = sat/satInOneBTC
    return btc

# Will need to print the information of the address
nTx = addressInfo['n_tx']
totalRec = satoshiToBTC(addressInfo['total_received'])
totalSent = satoshiToBTC(addressInfo['total_sent'])
finalBal = satoshiToBTC(addressInfo['final_balance'])

print('{:<20}  {:<20}'.format("Info For:", addressToLookup))
print('{:<20}  {:<20}'.format("Number of txs:", str(nTx) + " txs"))
print('{:<20}  {:<20}'.format("Total Received:", "₿ " + str(totalRec)))
print('{:<20}  {:<20}'.format("Total Sent:", "₿ " + str(totalSent)))
print('{:<20}  {:<20}'.format("Final Balance:", "₿ " + str(finalBal)))
