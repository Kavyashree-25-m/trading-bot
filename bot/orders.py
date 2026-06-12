from bot.logging_config import logger

def place_order(client, symbol, side, order_type, quantity, price=None):

    logger.info(
        f"Request: {symbol} {side} {order_type}"
    )

    if order_type == "MARKET":

        response = client.market_order(
            symbol,
            side,
            quantity
        )

    else:

        response = client.limit_order(
            symbol,
            side,
            quantity,
            price
        )

    logger.info(f"Response: {response}")

    return response