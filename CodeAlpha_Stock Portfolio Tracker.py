import csv

def stock_portfolio_tracker():
    # Hardcoded stock prices
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "MSFT": 320,
        "GOOGL": 140,
        "AMZN": 135
    }

    portfolio = {}  
    total_investment = 0

    print(" Stock Portfolio Tracker")
    print("Available stocks:", ", ".join(stock_prices.keys()))

    while True:
        stock = input("\nEnter stock symbol (or 'done' to finish): ").upper()
        if stock == "DONE":
            break

        if stock not in stock_prices:
            print(" Stock not found. Please choose from:", ", ".join(stock_prices.keys()))
            continue

        try:
            qty = int(input(f"Enter quantity of {stock}: "))
            if qty < 0:
                print(" Quantity cannot be negative.")
                continue
        except ValueError:
            print(" Please enter a valid number.")
            continue

        # Save stock and calculate investment
        portfolio[stock] = portfolio.get(stock, 0) + qty
        total_investment += stock_prices[stock] * qty

    # Display portfolio summary
    print("\n📑 Portfolio Summary:")
    for stock, qty in portfolio.items():
        print(f"{stock} - {qty} shares @ ${stock_prices[stock]} = ${stock_prices[stock] * qty}")
    print(f"\n💰 Total Investment Value: ${total_investment}")

    # Ask to save results
    save_choice = input("\nDo you want to save results? (txt/csv/no): ").lower()
    
    if save_choice == "txt":
        with open("portfolio.txt", "w") as f:
            f.write("Stock Portfolio Summary\n")
            for stock, qty in portfolio.items():
                f.write(f"{stock} - {qty} shares @ ${stock_prices[stock]} = ${stock_prices[stock] * qty}\n")
            f.write(f"\nTotal Investment Value: ${total_investment}\n")
        print(" Results saved in portfolio.txt")

    elif save_choice == "csv":
        with open("portfolio.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Stock", "Quantity", "Price", "Value"])
            for stock, qty in portfolio.items():
                writer.writerow([stock, qty, stock_prices[stock], stock_prices[stock] * qty])
            writer.writerow(["TOTAL", "", "", total_investment])
        print(" Results saved in portfolio.csv")

    else:
        print(" Results not saved.")

# Run the tracker
if __name__ == "__main__":
    stock_portfolio_tracker()
