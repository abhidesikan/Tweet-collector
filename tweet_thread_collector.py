#!/usr/bin/python
import twitter

def authenticate():
    api = twitter.Api(consumer_key=CONSUMER_KEY,consumer_secret=CONSUMER_SECRET,access_token_key=ACCESS_KEY_TOKEN,access_token_secret=ACCESS_TOKEN_SECRET)
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

