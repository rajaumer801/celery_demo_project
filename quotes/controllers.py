import requests

from quotes.models import Quote
from quotes.serializers import QuoteSerializer


def get_random_quotes():
    url = "https://api.forismatic.com/api/1.0/?method=getQuote&lang=en&format=json&json=?"
    r = requests.get(url=url)
    # extracting data in json format
    data = r.json()
    print(data)
    quote_data = {'author': data.get('quoteAuthor'),
                  'quote': data.get('quoteText')}
    serializer = QuoteSerializer(data=quote_data)
    serializer.is_valid()
    serializer.save()


def remove_oldest_quote():
    Quote.objects.earliest('added_at').delete()
