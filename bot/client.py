from binance.client import Client
from dotenv import load_dotenv
import os

load_dotenv()

class BinanceFuturesClient:

    def __init__(self):

        self.client = Client(
            os.getenv("BINANCE_API_KEY"),
            os.getenv("BINANCE_SECRET_KEY"),
            testnet=True
        )

        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    def market_order(self, symbol, side, quantity):

        return self.client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )

    def limit_order(self, symbol, side, quantity, price):

        return self.client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )