import requests
import sys


def main():
    btc = get_btc()
    search_btc(btc)



def get_btc():
    try:
        btc = float(sys.argv[1])
        return btc
    except Exception as e:
        sys.exit("Error. Try bitcoin.py [amount of bitcoin you would like to buy]")


def search_btc(btc):
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

    if response.status_code != 200:
            sys.exit("Error fetching data from Coindesk API")

    data = response.json()


    rate = data["bpi"]["USD"]["rate_float"]

    value = btc * rate
    print(f"${value:,.4f}")

if __name__ == "__main__":
    main()
