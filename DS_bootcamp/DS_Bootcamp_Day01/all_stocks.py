import sys

def get_info(query):
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
    
    TICKER_TO_COMPANY = {v:k for k , v in COMPANIES.items()}
    
    if query.upper() in TICKER_TO_COMPANY:
        return f"{query.upper()} is a ticker symbol for {TICKER_TO_COMPANY[query.upper()]}"

    normalized_name = query.capitalize()
    if normalized_name in COMPANIES:
        ticker = COMPANIES[normalized_name]
        price = STOCKS[ticker]
        return f"{normalized_name} stock price is {price}"
    
    return f"{query} is an unknown company or an unknown ticker symbol"

def main():
    if len(sys.argv) != 2:  # Проверяем количество аргументов
        return
    
    input_str = sys.argv[1]
    if (",,") in input_str:
        return
    
    queries = [query.strip() for query in input_str.split(',') if query.strip()]
    
    for query in queries:
        result = get_info(query)
        print(result)

if __name__ == '__main__':
    main()
    