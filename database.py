import yfinance as yf
from bitcoin_tracker.models import BitcoinPrice

# Fetch Bitcoin data using yfinance
bitcoin_data = yf.download("BTC-USD", start="2017-06-12", end="2021-06-12")

# Store Bitcoin closing prices in the database
for index, row in bitcoin_data.iterrows():
    date = index.date()
    price = row['Close']
    BitcoinPrice.objects.create(date=date, price=price)
