from binance.client import Client
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("BINANCE_API_KEY")
secret_key = os.getenv("BINANCE_SECRET_KEY")

client = Client(
    api_key,
    secret_key,
    testnet=True
)

client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

try:
    account = client.futures_account()

    print("Connection successful!")
    print("Wallet Balance:", account["totalWalletBalance"])

except Exception as e:
    print("Error:", e)