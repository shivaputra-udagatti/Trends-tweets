
import requests
from requests_oauthlib import OAuth1
from urllib.parse import parse_qs
import sqlite3
import json
import datetime

REQUEST_TOKEN_URL = "https://api.twitter.com/oauth/request_token"
AUTHORIZE_URL = "https://api.twitter.com/oauth/authorize?oauth_token="
ACCESS_TOKEN_URL = "https://api.twitter.com/oauth/access_token"

CONSUMER_KEY = "IvmEmZt0RrYLZgKNUwiCtIWwP"
CONSUMER_SECRET = "B9TnxIAGEcf0K7DLr3626SopSSiTJRBIxBgcnWuVoa1CQdQJd8"

OAUTH_TOKEN = "2280454746-gslxOtCVYp6EIVdKVwaprfLZhl9jDB5TgTEVPAP"
OAUTH_TOKEN_SECRET = "b54ftEhnLQH7Z6w8Nbwbq2KVNFAqQMHkPUET9BcLGvYyj"


def setup_oauth():
    # Request token
    oauth = OAuth1(CONSUMER_KEY, client_secret=CONSUMER_SECRET)
    r = requests.post(url=REQUEST_TOKEN_URL, auth=oauth)
    credentials = parse_qs(r.content)

    resource_owner_key = credentials.get('oauth_token')[0]
    resource_owner_secret = credentials.get('oauth_token_secret')[0]

    authorize_url = AUTHORIZE_URL + resource_owner_key
    print ('Please go here and authorize: ' + authorize_url)

    verifier = raw_input('Please input the verifier: ')
    oauth = OAuth1(CONSUMER_KEY,
                   client_secret=CONSUMER_SECRET,
                   resource_owner_key=resource_owner_key,
                   resource_owner_secret=resource_owner_secret,
                   verifier=verifier)

    # Finally, Obtain the Access Token
    r = requests.post(url=ACCESS_TOKEN_URL, auth=oauth)
    credentials = parse_qs(r.content)
    token = credentials.get('oauth_token')[0]
    secret = credentials.get('oauth_token_secret')[0]

    return token, secret


def get_oauth():
    oauth = OAuth1(CONSUMER_KEY,
                client_secret=CONSUMER_SECRET,
                resource_owner_key=OAUTH_TOKEN,
                resource_owner_secret=OAUTH_TOKEN_SECRET)
    return oauth

oauth = get_oauth()
r = requests.get(url="https://api.twitter.com/1.1/trends/place.json?id=23424848", auth=oauth)
conn = sqlite3.connect('tweets')
now = datetime.datetime.now()
tdate=str(now.year)+"-"+str('%02d' % now.month)+"-"+str('%02d' % now.day)
tweet_json = (r.content).decode('utf8')
tweet_json = json.loads(tweet_json)
for i in range(len(tweet_json[0]['trends'])):
    name=tweet_json[0]['trends'][i]['name']
    name=name.replace("'", '')
    turl=tweet_json[0]['trends'][i]['url']
    q=tweet_json[0]['trends'][i]['query']
    conn.execute("INSERT INTO tweets_table (q,name,url,created) VALUES ('"+q+"','"+name+"','"+turl+"','"+tdate+"')")

#conn.execute('''CREATE TABLE tweets_table( id INTEGER PRIMARY KEY AUTOINCREMENT,url TEXT NOTvNULL ,name TEXT NOT NULL,created TEXT,q TEXT);''')
#conn.execute("DROP TABLE tweets_table")
conn.commit()

print(tweet_json)
#print(tweet_json)







