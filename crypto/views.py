from django.shortcuts import render
import requests
import json


api_key = '2864eda73aa52539b39242f69af0ffceb4c83faa4ade9af093ea718ea1930eb9'


def index(request):

    # Grab Crypto Price Data
    crpyto_names = 'BTC,ETH,XRP,BCH,EOS,LTC,XLM,ADA,USDT,MIOATA,TRX'
    price_request = requests.get(f'https://min-api.cryptocompare.com/data/pricemultifull?fsyms={crpyto_names}&tsyms=USD&api_key={api_key}')
    price = json.loads(price_request.content)

    # Grab Crypto news
    news_request = requests.get(f'https://min-api.cryptocompare.com/data/v2/news/?lang=EN&api_key={api_key}')
    news = json.loads(news_request.content)

    context = {
        'price': price,
        'news': news,
    }

    return render(request, 'index.html', context)


def prices(request):

    if request.method == 'POST':
        quote = request.POST['quote'].upper()
        crpyto_request = requests.get(
            f'https://min-api.cryptocompare.com/data/pricemultifull?fsyms={quote}&tsyms=USD&api_key={api_key}')
        crypto = json.loads(crpyto_request.content)
        context = {
            'quote': quote,
            'crypto': crypto
        }
        return render(request, 'prices.html', context)
    else:
        notfound = 'Enter a crypto currency symbol into to search'
        return render(request, 'prices.html', {'notfound': notfound})


def all_prices(request):
    crpyto_names = 'BTC,ETH,XRP,BCH,EOS,LTC,XLM,ADA,USDT,MIOATA,TRX'
    all_crypto = requests.get(f'https://min-api.cryptocompare.com/data/pricemultifull?fsyms={crpyto_names}&tsyms=USD&api_key={api_key}')
    price = json.loads(all_crypto.content)

    context = {
        'price': price,
    }
    return render(request, 'all_prices.html', context)
