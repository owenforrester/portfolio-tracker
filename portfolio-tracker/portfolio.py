import yfinance as yf
import pandas as pd
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_stock_info(stock_symbol):
    ticker = yf.Ticker(stock_symbol)
    price = ticker.info['currentPrice']
    shares = float(input(f"How many shares of {stock_symbol} do you own? "))
    return price, shares

def return_portfolio(portfolio):
    print("PORTFOLIO:\n")
    for stock in portfolio:
        print(f"{stock['Ticker']}: {stock['Shares']} shares at ${stock['Price']:.2f} each, total value: ${stock['Total Value']:.2f}\n")

def choice_reset(choice):
    return input("Press 1 to view portfolio analytics, or 2 to add another stock to your portfolio, or 3 to view your portfolio, 4 to see your diversification, or 5 to exit.\n")

def get_portfolio_diversification(portfolio, total_total_value):
    for stock in portfolio:
        stock['Diversification'] = stock['Total Value'] / total_total_value * 100
    return portfolio

clear()
portfolio = []


choice = input("Press 1 to view portfolio analytics, or 2 to add another stock to your portfolio, or 3 to view your portfolio, 4 to see your diversification, or 5 to exit.\n")


while True:
    
    if choice not in ['1', '2', '3', '4', '5']:
        clear()
        print("Invalid choice. Please try again.\n")
        choice = choice_reset(choice)

    elif choice == '1':
        clear()
        print("Portfolio analytics coming soon!\n")
        choice = choice_reset(choice)

    elif choice == '2':
        clear()
        stock_symbol = input("What is the Ticker symbol? \n")
        try:
            price, shares = get_stock_info(stock_symbol)
            total_value = price * shares
            portfolio.append({
                "Ticker": stock_symbol,
                "Shares": shares,
                "Price": price,
                "Total Value": total_value
            })
            total_total_value = sum(stock['Total Value'] for stock in portfolio)
            clear()
            print(f"Stock information retrieved successfully!\nYou own {shares:.2f} shares of {stock_symbol} worth ${total_value:.2f}.\n\n")
            choice = choice_reset(choice)
        except:
            clear()
            print(f"\"{stock_symbol}\" is an invalid ticker symbol. Please try again.\n\n")
            choice = choice_reset(choice)

    elif choice == '3':
        clear()
        if len(portfolio) == 0:
            print("Your portfolio is currently empty.\n")
        else:
            return_portfolio(portfolio)
            print(f"Total portfolio value: ${total_total_value:.2f}\n")
        choice = choice_reset(choice)

    elif choice == '4':
        clear()
        if len(portfolio) == 0:
            print("Your portfolio is currently empty.\n")
        else:
            print("Diverisification:\n")
            get_portfolio_diversification(portfolio, total_total_value)
            for stock in portfolio:
                print(f"{stock['Ticker']}: {stock['Diversification']:.2f}%\n")
        choice = choice_reset(choice)

    elif choice == '5':
        clear()
        print("Exiting program...\n\nSuccess!")
        break

