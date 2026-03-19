import sys

def get_stock_price(company_name):
    COMPANIES = {
    'Apple': 'AAPL',
    'Microsoft': 'MSFT',
    'Netflix': 'NFLX',
    'Tesla': 'TSLA',
    'Nokia': 'NOK'
    }

    STOCKS = {
    'AAPL': 287.73,
    'MSFT': 173.79,
    'NFLX': 416.90,
    'TSLA': 724.88,
    'NOK': 3.37
    }

    normalized_name = company_name.capitalize()
    if normalized_name in COMPANIES:
        ticker = COMPANIES[normalized_name]
        return STOCKS.get(ticker, None)
    return None

def main():
    if len(sys.argv) != 2:  # Проверяем количество аргументов
        return
    
    company = sys.argv[1]
    price = get_stock_price(company)
    
    if price is not None:
        print(price)
    else:
        print("Unknown company")

if __name__ == '__main__':
    main()
    