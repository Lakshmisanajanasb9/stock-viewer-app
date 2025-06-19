from flask import Flask, jsonify
import yfinance as yf 

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the Stock Viewer app!"

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