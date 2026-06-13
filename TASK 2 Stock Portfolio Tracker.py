"""
TASK 2: Stock Portfolio Tracker

Lets the user enter stock names & quantities, calculates total investment
using a hardcoded price dictionary, and saves results to a CSV file.
"""

import csv
import os
from datetime import datetime

# Hardcoded stock prices (USD)
STOCK_PRICES = {
    "AAPL":  180.00,   # Apple
    "TSLA":  250.00,   # Tesla
    "GOOGL": 140.00,   # Alphabet (Google)
    "AMZN":  185.00,   # Amazon
    "MSFT":  415.00,   # Microsoft
    "META":  520.00,   # Meta
    "NFLX":  650.00,   # Netflix
    "NVDA":  900.00,   # NVIDIA
}

OUTPUT_FILE = "portfolio_report.csv"


def show_available_stocks():
    print("\n  📈 Available Stocks:")
    print(f"  {'Symbol':<8} {'Price (USD)':>12}")
    print("  " + "-" * 22)
    for symbol, price in STOCK_PRICES.items():
        print(f"  {symbol:<8} ${price:>11.2f}")
    print()


def get_portfolio():
    portfolio = []
    print("\n  Enter your stock holdings (type 'done' when finished).")

    while True:
        symbol = input("\n  Stock symbol (e.g. AAPL): ").strip().upper()

        if symbol.lower() == "done":
            break

        if symbol not in STOCK_PRICES:
            print(f"    '{symbol}' is not in our list. Please choose from the table above.")
            continue

        # Get quantity
        try:
            qty_str = input(f"  Quantity of {symbol}: ").strip()
            quantity = int(qty_str)
            if quantity <= 0:
                raise ValueError
        except ValueError:
            print("   Please enter a positive whole number for quantity.")
            continue

        # Check if this stock was already added; if so, update quantity
        existing = next((item for item in portfolio if item["symbol"] == symbol), None)
        if existing:
            existing["quantity"] += quantity
            print(f"   Updated {symbol}: total {existing['quantity']} shares.")
        else:
            portfolio.append({"symbol": symbol, "quantity": quantity})
            print(f"   Added {quantity} share(s) of {symbol}.")

    return portfolio


def calculate_portfolio(portfolio):
    grand_total = 0.0
    for item in portfolio:
        price = STOCK_PRICES[item["symbol"]]
        value = price * item["quantity"]
        item["price"] = price
        item["value"] = value
        grand_total += value
    return grand_total


def display_report(portfolio, grand_total):
    print("\n" + "=" * 55)
    print("             PORTFOLIO SUMMARY REPORT")
    print("=" * 55)
    print(f"  {'Symbol':<8} {'Qty':>6} {'Price (USD)':>12} {'Value (USD)':>12}")
    print("  " + "-" * 42)

    for item in portfolio:
        print(
            f"  {item['symbol']:<8} {item['quantity']:>6} "
            f"${item['price']:>11.2f} ${item['value']:>11.2f}"
        )

    print("  " + "-" * 42)
    print(f"  {'TOTAL':>27} ${grand_total:>11.2f}")
    print("=" * 55 + "\n")


def save_to_csv(portfolio, grand_total, filename=OUTPUT_FILE):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Portfolio Report", f"Generated: {timestamp}"])
        writer.writerow([])
        writer.writerow(["Symbol", "Quantity", "Price (USD)", "Value (USD)"])
        for item in portfolio:
            writer.writerow([
                item["symbol"],
                item["quantity"],
                f"{item['price']:.2f}",
                f"{item['value']:.2f}",
            ])
        writer.writerow([])
        writer.writerow(["", "", "GRAND TOTAL", f"{grand_total:.2f}"])

    print(f"  💾 Report saved to '{os.path.abspath(filename)}'")


def main():
    print("\n" + "=" * 55)
    print("          STOCK PORTFOLIO TRACKER")
    print("=" * 55)

    show_available_stocks()
    portfolio = get_portfolio()

    if not portfolio:
        print("\n  ℹ  No stocks entered. Exiting.\n")
        return

    grand_total = calculate_portfolio(portfolio)
    display_report(portfolio, grand_total)

    save = input("  Save report to CSV? (yes/no): ").strip().lower()
    if save in ("yes", "y"):
        save_to_csv(portfolio, grand_total)

    print("\n  Thank you for using the Stock Portfolio Tracker! 👋\n")


if __name__ == "__main__":
    main()