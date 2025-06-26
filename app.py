from flask import Flask, jsonify
import yfinance as yf 
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return jsonify({"Hello": "Welcome to the Stock Price API!"})

@app.route('/stock/<ticker>')
def stock_view(ticker):
    stock = yf.Ticker(ticker=ticker)
    data = stock.history(period="1d")
    if data.empty:
        return jsonify({"error": "Invalid ticker"}), 404
    price = data['Close'].iloc[-1]
    return jsonify({"price": price, "ticker": ticker})

if __name__ == '__main__':
    app.run()
    