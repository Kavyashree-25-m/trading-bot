# Binance Futures Testnet Trading Bot

## Overview

This project is a Python-based trading bot that places orders on the Binance Futures Testnet (USDT-M).

The bot supports:

* Market Orders
* Limit Orders
* BUY and SELL sides
* Command-line interface (CLI)
* Input validation
* Logging of requests, responses, and errors
* Exception handling

---

## Project Structure

```text
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── logs/
│   └── trading.log
│
├── cli.py
├── requirements.txt
├── README.md
└── .env
```

---

## Requirements

* Python 3.x
* Binance Futures Testnet Account
* API Key and Secret Key

---

## Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Configuration

Create a `.env` file in the project root:

```env
BINANCE_API_KEY=your_api_key
BINANCE_SECRET_KEY=your_secret_key
```

---

## Usage

### Place a Market Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### Place a Limit Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 200000
```

---

## Logging

All requests, responses, and errors are stored in:

```text
logs/trading.log
```

---

## Assumptions

* Uses Binance Futures Testnet only.
* Supports MARKET and LIMIT order types.
* LIMIT orders use GTC (Good Till Cancelled).
* API credentials are stored securely using environment variables.

---

## Error Handling

The application handles:

* Invalid symbols
* Invalid order sides
* Invalid order types
* Missing price for LIMIT orders
* API exceptions
* Network failures
* Invalid quantities

```
```
