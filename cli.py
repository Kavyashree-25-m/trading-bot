import argparse

from bot.client import BinanceFuturesClient
from bot.orders import place_order
from bot.validators import validate_order


def main():
    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )

    parser.add_argument(
        "--symbol",
        required=True
    )

    parser.add_argument(
        "--side",
        required=True
    )

    parser.add_argument(
        "--type",
        required=True
    )

    parser.add_argument(
        "--quantity",
        required=True,
        type=float
    )

    parser.add_argument(
        "--price",
        type=float
    )

    args = parser.parse_args()

    try:
        validate_order(
            args.symbol.upper(),
            args.side.upper(),
            args.type.upper(),
            args.quantity,
            args.price
        )

        client = BinanceFuturesClient()

        response = place_order(
            client,
            args.symbol.upper(),
            args.side.upper(),
            args.type.upper(),
            args.quantity,
            args.price
        )

        print("\n===== ORDER SUMMARY =====")
        print(f"Symbol       : {args.symbol.upper()}")
        print(f"Side         : {args.side.upper()}")
        print(f"Type         : {args.type.upper()}")
        print(f"Quantity     : {args.quantity}")

        if args.price:
            print(f"Price        : {args.price}")

        print("\n===== ORDER RESPONSE =====")

        print(
            f"Order ID     : {response.get('orderId', 'N/A')}"
        )

        print(
            f"Status       : {response.get('status', 'N/A')}"
        )

        print(
            f"Executed Qty : {response.get('executedQty', 'N/A')}"
        )

        print(
            f"Average Price: {response.get('avgPrice', 'N/A')}"
        )

        print("\nSUCCESS")

    except Exception as e:
        print(f"\nFAILED: {e}")


if __name__ == "__main__":
    main()