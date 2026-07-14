stock_price={
    "AAPL":180,
    "TSLA":250,
    "GOOGL":140,
    "MSFT":330
    }
total_investment=0
while True:
    stock_name=input("Enter stock name:(or type 'DONE' to exit)").upper()

    if stock_name == "DONE":
        break

    quantity=int(input("Enter number of shares:"))
    
    if stock_name in stock_price:
        price=stock_price[stock_name]
        investment=price*quantity
        total_investment=total_investment +investment

        print("price per share:",price)
        print("Total investment:",investment)

    else:
        print("Stock not available")

print("total portfolio investment:", total_investment)


