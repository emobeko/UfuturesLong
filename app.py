from flask import Flask, request
import json
from binance.um_futures import UMFutures

app = Flask(__name__)


@app.route("/webhook", methods=['POST'])
def webhook():

    try:
        data = json.loads(request.data)
        ticker = data['ticker']
        exchange = data['exchange']
        price = data['price']
        side = data['side']
        quantity = data['quantity']
        key = data['binanceApiKey']
        secret = data['binanceSecretKey']

        params = {
            "symbol": ticker,
            "side": side,
            "positionSide": "LONG",
            "type": "MARKET",
            "quantity": quantity,
        }
        um_futures_client = UMFutures()

        print(um_futures_client.time())

        um_futures_client = UMFutures(key=key, secret=secret)

        print(um_futures_client.account())

        response = um_futures_client.new_order(**params)
        print(response)

    except Exception as e:
        print(f"Error: {str(e)}")
        raise

    return {
        "code": "success",
    }








