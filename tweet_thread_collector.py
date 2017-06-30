#!/usr/bin/python
import twitter
import configparser
from datetime import datetime,timedelta

class tweet_auth(object):
    def __init__(self):
        self._config = None

    def get_consumer_key(self):
        return self._get_option('CONSUMER_KEY')

    def get_consumer_secret(self):
        return self._get_option('CONSUMER_SECRET')

    def get_access_key(self):
        return self._get_option('ACCESS_KEY_TOKEN')

    def get_access_secret(self):
        return self._get_option('ACCESS_TOKEN_SECRET')

    def _get_option(self, option):   
        try:
            return self._get_config().get('Tweet', option)
        except:
            return None

    def _get_config(self):
        if not self._config:
            self._config = configparser.ConfigParser()
            self._config.read(u'.auth_tweet')
        return self._config

def authenticate():
    auth = tweet_auth()
    api = twitter.Api(consumer_key=auth.get_consumer_key(),consumer_secret=auth.get_consumer_secret(),access_token_key=auth.get_access_key(),access_token_secret=auth.get_access_secret())
    return api

def get_root_thread_info(api, date, user_handle):
    results = api.GetSearch(raw_query="q=Today%27s%20thread%20from%3A"+user_handle+"%20since%3A"+date)
    list_ids = []
    for s in results:
        list_ids.append(s.id)
    return list_ids

#def extract_replies(api, date, list_ids)

def generate_date():
    yesterday = datetime.now() - timedelta(days=1)
    return yesterday.strftime("%Y-%m-%d")

def main():
    api = authenticate()
    date = generate_date()
    list_ids = get_root_thread_info(api, date, 'OnlyNakedTruth')
    print list_ids

if __name__ == '__main__':
    main()

