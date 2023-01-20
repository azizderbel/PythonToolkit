import threading
import requests
from lxml import html

class Stock(threading.Thread):

    def __init__(self, symbol: str) -> None:
        super().__init__()
        self.symbol = symbol
        self.url = f'https://finance.yahoo.com/quote/{symbol}'
        self.price = None

    # override the run method
    def run(self):
        try:
            response = requests.get(self.url)
        except:
            print('Could not get to the Api')
        else:
            if response.status_code == 200:
                # parse html
                tree = html.fromstring(response.text)
                # get the price in text
                price_text = tree.xpath(
                '//*[@id="quote-header-info"]/div[3]/div[1]/div[1]/fin-streamer[1]/text()')
                if price_text:
                    try:
                        self.price = float(price_text[0].replace(',', ''))
                    except ValueError:
                        self.price = None
    
    def __str__(self):
        return f'{self.symbol}\t{self.price}'



