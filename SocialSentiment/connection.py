import requests
import time

from apikeys import finnhubKey
from SQLSchema import SocialSentimentSchema

# Fill DB for one stock at a time due to data limits
def fillDB(ticker):

    # Create schema instance to connect to db
    ss = SocialSentimentSchema()

    daysInMonth = {
        '01' : 31,
        '02' : 28,
        '03' : 31,
        '04' : 30,
        '05' : 31,
        '06' : 30,
        '07' : 31,  
        '08' : 31,
        '09' : 30,
        '10' : 31,
        '11' : 30,
        '12' : 31
    }

    # There can only be 100 hours of data at a time, so will loop over 4 days at a time (96 hrs)
    for x, y in daysInMonth.items():
        start = 1
        end = 4

        while end <= y:
            queryAPI(ticker, start, end, x, ss)
            if end >= y: break
            start += 4
            if end + 4 > y:
                end = y
            else: end +=4
            time.sleep(0.1)

        time.sleep(1)

def queryAPI(ticker, start, end, month, ss):
    print(month, start)
    response = requests.get(f'https://finnhub.io/api/v1/stock/social-sentiment?symbol={ticker}&from=2022-{month}-{start}T00:00:00&to=2022-{month}-{end}T23:00:00&token={finnhubKey}')
    res = response.json()
    
    if 'error' in res:
        print('API limit reached (60 calls/min) Waiting to try again...')
        time.sleep(60)
        response = requests.get(f'https://finnhub.io/api/v1/stock/social-sentiment?symbol={ticker}&from=2022-{month}-{start}T00:00:00&to=2022-{month}-{end}T23:00:00&token={finnhubKey}')
        res = response.json()

    for i in reversed(res['reddit']):
        dbInsert(i, ticker, ss, 'reddit')

    for i in reversed(res['twitter']):
        dbInsert(i, ticker, ss, 'twitter')

def dbInsert(res, ticker, ss, source):
    date = res['atTime']
    source = source
    symbol = ticker
    mention = res['mention']
    positive_score = res['positiveScore']
    negative_score = res['negativeScore']
    positive_mention = res['positiveMention']
    negative_mention = res['negativeMention']
    score = round(res['score'],4)

    print(f"VALUES ('{date}', '{source}', '{symbol}', '{mention}', '{positive_score}', '{negative_score}', '{positive_mention}', '{negative_mention}', '{score}');")

    ss.cursor.execute("INSERT INTO finnhub (date, source, symbol, mention, positive_score, negative_score, positive_mention, negative_mention, score)"
                      f"VALUES ('{date}', '{source}', '{symbol}', '{mention}', '{positive_score}', '{negative_score}', '{positive_mention}', '{negative_mention}', '{score}');")

fillDB('NVDA')