#!/usr/bin/python
import twitter

CONSUMER_KEY = 'kjcBfAfP3XNmiigMgEBV9IkoN'
CONSUMER_SECRET = '3ZM7n8DEJIsvf0W7aER6G3nppv2lfqbETElGH40Y9eEfEl5D21'
ACCESS_KEY_TOKEN = '57625285-vCM89XiR8loxHHKY3PT2YKWZ9xDlFyFBjJnYELMlR'
ACCESS_TOKEN_SECRET = '3pieTmsWpvhLPPxxvL0HEYN9M9MHnoVfcIjVqaqsmJb4u'

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

