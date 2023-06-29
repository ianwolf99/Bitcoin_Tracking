import yfinance as yf
from django.core.management.base import BaseCommand
from bitcoin_tracker.models import BitcoinPrice
class Command(BaseCommand):
    help = 'Fetches and stores Bitcoin closing prices from yfinance'

    def handle(self, *args, **options):
        # Fetch Bitcoin data using yfinance
        bitcoin_data = yf.download("BTC-USD", start="2017-06-12", end="2021-06-12")

        # Store Bitcoin closing prices in the database
        for index, row in bitcoin_data.iterrows():
            date = index.date()
            price = row['Close']
            BitcoinPrice.objects.create(date=date, price=price)

        self.stdout.write(self.style.SUCCESS('Bitcoin data fetched and stored successfully.'))
