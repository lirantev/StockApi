import requests
import json

userInput = input("Please enter stock symbol:\n")
splitInput = userInput.split(",")
for x in splitInput:
	stockName = requests.get("https://api.iextrading.com/1.0/stock/"+ x +"/quote", verify = False)
	stockPrice = requests.get("https://api.iextrading.com/1.0/stock/"+ x +"/price",verify = False)
	stockPriceData = stockPrice.json()
	stockNameData = stockName.json()
	print(f"Stock name is: {stockNameData['companyName']}")
	print(f"Stock symbol is: {stockNameData['symbol']}")
	print(f"Stock price is: {stockPriceData}")
	print(f"Stock change is: {stockNameData['change']}")
	if (stockNameData['change'] < 0):
		print("The stock has moved down")
	else:
		print("The stock has moved up")