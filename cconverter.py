import requests
import json

currency = input().lower()
res_request = requests.get(f'http://www.floatrates.com/daily/{currency}.json')
request_dict = json.loads(res_request.text)
currency_dict = {}
if currency == 'usd':
    currency_dict.update(eur=request_dict['eur']['inverseRate'])
elif currency == 'eur':
    currency_dict.update(usd=request_dict['usd']['inverseRate'])
else:
    currency_dict.update(usd=request_dict['usd']['inverseRate'], eur=request_dict['eur']['inverseRate'])
while True:
    exchange_currency = input().lower()
    if exchange_currency == '':
        break
    amount = float(input())
    print('Checking the cache...')
    if exchange_currency in currency_dict:
        print('Oh! It is in the cache!')
        result = amount / currency_dict[exchange_currency]
    else:
        print('Sorry, but it is not in the cache!')
        currency_dict[exchange_currency] = request_dict[exchange_currency]['inverseRate']
        result = amount / currency_dict[exchange_currency]
    print(f'You received {round(result, 2)} {exchange_currency.upper()}.')
