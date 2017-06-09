#!/usr/bin/python
import twitter
import configparser

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
            self._config.read('.auth_tweet')
        return self._config

def authenticate():
    auth = tweet_auth()
    api = twitter.Api(consumer_key=auth.get_consumer_key(),consumer_secret=auth.get_consumer_secret(),access_token_key=auth.get_access_key(),access_token_secret=auth.get_access_secret())
    return api

def get_public_status(user_id, api):
    statuses = api.GetUserTimeline(user_id)
    print([s.text for s in statuses])
    replies = api.GetReplies()
    print replies

def main():
    api = authenticate()
    get_public_status('2943003606', api)

if __name__ == '__main__':
    main()

