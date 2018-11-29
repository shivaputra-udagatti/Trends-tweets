import schedule
import time
import os


def job(t):
    os.system('python twitter.py')
    os.system('python twitter_search.py')
    return

schedule.every().day.at("11:30").do(job,'Data stored')
while True:
    schedule.run_pending()
    time.sleep(60) 
