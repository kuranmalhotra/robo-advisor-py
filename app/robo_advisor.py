
# Robo Advisor and Portfolio Manager
### Created 2/25/2019 by Kuran P. Malhotra
### Starter Repo from https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/projects/robo-advisor.md

from dotenv import load_dotenv
import json
import os
import requests
import pandas as pd

load_dotenv() # loads environment variables set in a ".env" file, including the value of the ALPHAVANTAGE_API_KEY variable

# see: https://www.alphavantage.co/support/#api-key
api_key = os.environ.get("ALPHAVANTAGE_API_KEY")
print("API KEY: " + api_key)

symbol = ""

def getsymbol(): # function to include validation into the system.
	global symbol
	symbol = input("Please specify a stock symbol: ") 

	if len(symbol) < 1:
		print("Oops, we didn't get your symbol. Mind trying again?")
		getsymbol() 
	elif len(symbol) > 6: # Per a quick Google, 6 seems to be the max length of a ticker: https://www.quora.com/Whats-the-shortest-and-the-longest-that-a-companys-ticker-can-be-on-a-stock-market-exchange
			print("Hmm...that symbol seems a bit long...mind trying again?")
			getsymbol()
	else: print("Thanks! Let's see what we can do...")

	symbol = symbol.upper()

getsymbol()

# see: https://www.alphavantage.co/documentation/#daily (or a different endpoint, as desired)
# Assemble URL

request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}"
print(request_url)

# TODO: use the "requests" package to issue a "GET" request to the specified url, and store the JSON response in a variable...

response = requests.get(request_url)

# Validate a valid response given improper response codes:

if "Error" in response.text:
	print("Hmm. Something went wrong there...try again later!")
	exit()

# print("RESPONSE STATUS: " + str(response.status_code))
# print("RESPONSE TEXT: " + response.text)

parsed_response = response.json()


# TODO: further parse the JSON response...

# TODO: traverse the nested response data structure to find the latest closing price and other values of interest...
latest_price_usd = "$100,000.00"

#
# INFO OUTPUTS
#

# TODO: write response data to a CSV file

# TODO: further revise the example outputs below to reflect real information
print("-----------------")
print(f"STOCK SYMBOL: {symbol}")
print("RUN AT: 11:52pm on June 5th, 2018")
print("-----------------")
print("LATEST DAY OF AVAILABLE DATA: June 4th, 2018")
print(f"LATEST DAILY CLOSING PRICE: {latest_price_usd}")
print("RECENT HIGH: $101,000.00")
print("RECENT LOW: $99,000.00")
print("-----------------")
print("RECOMMENDATION: Buy!")
print("RECOMMENDATION REASON: Because the latest closing price is within threshold XYZ etc., etc. and this fits within your risk tolerance etc., etc.")
print("-----------------")
