"""
Bitcoin Telegram Bot Script

This script monitors the current price of Bitcoin and sends updates to a specified Telegram chat
when the price falls below a defined limit. It utilizes the CoinMarketCap API to fetch the latest
cryptocurrency prices and the Telegram Bot API to send messages.

Requirements:
- Python 3.x
- requests library
- A valid CoinMarketCap API key
- A valid Telegram Bot token and chat ID

For more information on obtaining API keys, visit:
- CoinMarketCap: https://pro.coinmarketcap.com/account
- Telegram Bot: https://core.telegram.org/bots#botfather
"""
import time
from decimal import Decimal

import requests

from constants import (
    LIMIT,
    TIME_INTERVAL,
    TELEGRAM_CHAT_ID,
    TELEGRAM_BOT_TOKEN,
    API_KEY
)


def get_price():
    """Fetches the current price of Bitcoin in USD.

    This function sends a request to the CoinMarketCap API to retrieve the latest cryptocurrency listings.
    It extracts the price of Bitcoin (BTC) from the response and returns it.

    Returns:
        float: The current price of Bitcoin in USD.

    Raises:
        requests.exceptions.RequestException: If the API request fails.
        KeyError: If the expected data structure is not found in the response.
    """
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
        'start': '1',
        'limit': '10',
        'convert': 'USD'
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': API_KEY,
    }

    try:
        response = requests.get(url, headers=headers, params=parameters)
        response.raise_for_status()  # Raise an error for bad responses
        btc_price = response.json()['data'][0]['quote']['USD']['price']
        return btc_price
    except requests.exceptions.RequestException as e:
        print(f"Error fetching price: {e}")
        return None
    except KeyError:
        print("Error: Unexpected response structure.")
        return None

def send_updates(msg):
    """Sends a message to a specified Telegram chat.

    This function constructs a URL for the Telegram Bot API to send a message
    to a chat identified by the chat ID. It uses the bot token for authentication
    and sends the provided message as text.

    Args:
        msg (str): The message to be sent to the Telegram chat.

    Raises:
        requests.exceptions.RequestException: If the API request fails.
    """
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage?chat_id=" \
          f"{TELEGRAM_CHAT_ID}&text={msg}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
    except requests.exceptions.RequestException as e:
        print(f"Error sending message: {e}")

if __name__ == '__main__':
    """Main execution block for monitoring Bitcoin price and sending updates.

    This script continuously checks the current price of Bitcoin at regular intervals.
    If the price falls below a specified limit, it sends a notification message to a
    designated Telegram chat. The checking interval is defined by the TIME_INTERVAL constant.

    The script runs indefinitely until manually terminated.

    Raises:
        KeyboardInterrupt: If the user interrupts the execution (e.g., Ctrl+C).
        Exception: Any other exceptions that may occur during price retrieval or message sending.
    """
    while True:
        price = get_price()
        if price is not None and price < Decimal(LIMIT):
            send_updates(msg=f"Bitcoin price now is {price}")

        time.sleep(TIME_INTERVAL)
