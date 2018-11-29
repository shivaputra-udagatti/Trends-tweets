
import requests
from requests_oauthlib import OAuth1
from urllib.parse import parse_qs
import sqlite3
import re
import time
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
conn = sqlite3.connect('tweets')
a=conn.execute("SELECT uname FROM tweetsearch_table ")
#conn.execute('''CREATE TABLE tweetrepla_table( id INTEGER PRIMARY KEY AUTOINCREMENT,data TEXT  NULL ,tid TEXT  NULL,retweet TEXT NULL,favorite_count TEXT NULL,uname TEXT NULL,profimg TEXT NULL,sname TEXT NOT NULL,url TEXT NULL);''')
#conn.execute("DROP TABLE tweetreplay_table")

aa=list(a.fetchall())
for k in range(0,len(aa)):
    aaa=str(aa[k])
    query=re.sub('[,\'()]+', '', aaa)
    print(query)
    r = requests.get(url="https://api.twitter.com/1.1/search/tweets.json?q="+query+"&count=50000", auth=oauth)
    time.sleep(2)
    tweet_json = (r.content).decode('utf8')
    tweet_json = json.loads(tweet_json)
        #tweet_json = json.dumps(tweet_json)
    try:
        for i in range(len(tweet_json['statuses'])):
            if tweet_json['statuses'][i]['in_reply_to_status_id_str'] is not None:
                ttext=tweet_json['statuses'][i]['text'].strip()
                ttext=ttext.replace("'",'')
                ttext=ttext.replace('\n',' ')
                tid=tweet_json['statuses'][i]['id_str']
                retweet=str(tweet_json['statuses'][i]['retweet_count'])
                favorite_count=str(tweet_json['statuses'][i]['favorite_count'])
                uname=tweet_json['statuses'][i]['user']['screen_name']
                sname=tweet_json['statuses'][i]['user']['name']
                profimg=tweet_json['statuses'][i]['user']['profile_image_url']
                conn.execute("INSERT INTO tweetreplay_table (sname,data,tid,retweet,favorite_count,uname,profimg) VALUES ('"+ sname +"','"+ ttext +"','"+ tid +"','"+retweet+"','"+favorite_count+"','"+uname+"','"+profimg+"','"+profimg+"')");
                print(ttext)
                print(tid)
    except Exception as e:
        print("error===",e)

conn.commit()

#print(tweet_json)
#print(tweet_json)







