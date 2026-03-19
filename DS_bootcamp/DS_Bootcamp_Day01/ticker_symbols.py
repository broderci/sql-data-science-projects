import sys

def get_company_info(ticker):
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
    
    normalized_ticker = ticker.upper()
    if normalized_ticker in TICKER_TO_COMPANY:
        company = TICKER_TO_COMPANY[normalized_ticker]
        price = STOCKS[normalized_ticker]
        return f" {company} {price}"
    return None

def main():
    if len(sys.argv) != 2:  # Проверяем количество аргументов
        return
    
    ticker = sys.argv[1]
    company_info = get_company_info(ticker)
    
    if company_info is not None:
        print(company_info)
    else:
        print("Unknown company")

if __name__ == '__main__':
    main()
    
    