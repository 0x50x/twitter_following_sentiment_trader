import twitter
from time import sleep
import datetime
import time
from time import mktime
from nltk.sentiment.vader import SentimentIntensityAnalyzer

new_words = {
    'long': 1,
    'short': -1,
    'buy': 1,
    'sell': -1,
    'pump': 1,
    'dump': -1}

analyser = SentimentIntensityAnalyzer()

analyser.lexicon.update(new_words)

def sentiment_analyzer_scores(sentence):
    score = analyser.polarity_scores(sentence)
    return(score)
import requests
coins = requests.get('https://api.binance.com/api/v3/ticker/24hr')
coins = coins.json()
cs = []
for c in coins:
    if 'BTC' in c['symbol']:
        cs.append(c['symbol'][:-3])

api = twitter.Api(consumer_key='',
                      consumer_secret='',
                      access_token_key='',
                      access_token_secret='')
#print(api.VerifyCredentials())
users = api.GetFriends()
for u in users:
    print (u.screen_name)
for u in users:
    #print(u.screen_name)
    sleep(2)
    try:

        t = api.GetUserTimeline(screen_name=u.screen_name, count=100)#u.screen_name, count=10)
        tweets = [i.AsDict() for i in t]
        for t in tweets:
            ts =  time.strptime(t['created_at'],'%a %b %d %H:%M:%S +0000 %Y')
            dt = datetime.datetime.fromtimestamp(mktime(ts))

            if dt > datetime.datetime.now()-datetime.timedelta(days=7):
                split=(t['text']).replace('\n', ' ').split(' ')
                for s in split:
                    if s.isupper() or ('$' in s and (s).upper().replace('$','') in cs):
                        if s in cs or (s).upper().replace('$','') in cs:
                            print('coin:')
                            print(s)
                            print('sentiment score:')
                            print(sentiment_analyzer_scores(t['text'])['compound'])
    except Exception as e:
        print(e)