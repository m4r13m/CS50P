import requests
import sys
try:
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    n = float(sys.argv[1])
    response = requests.get("//rest.coincap.io/v3/assets/bitcoin?apiKey=YourApiKey")


    o = response.json()
    data = o["data"]
    price = data["priceUsd"]
    amount = float(price) * n
    print(f"${amount:,.4f}")

except (ValueError,requests.RequestException):
    sys.exit("Command-line argument is not a number")
