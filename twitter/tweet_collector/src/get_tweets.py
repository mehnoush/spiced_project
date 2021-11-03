import tweepy
import pymongo

API_KEY = "AO9qiiu6FfwrIGll0hGu0cxeS"
API_SECRET = "q3FnJDzgV5vUiHt6d2hKSaLI2irAEV6juvzpywgixUr99CPQij"
client = pymongo.MongoClient(host='mongodb', port=27017)
db = client.twitter

def get_auth_handler():
    """
    Function for handling Twitter Authentication. See course material for 
    instructions on getting your own Twitter credentials.
    """
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
    return auth


def get_full_text(status):
    """Returns the full text of a (re)tweet"""
    try:
        return status.retweeted_status.full_text
    except AttributeError:  # Not a Retweet
        return status.full_text


if __name__ == '__main__':
    auth = get_auth_handler()
    api = tweepy.API(auth)

    # cursor = tweepy.Cursor(
    #     api.user_timeline,
    #     id='guardian',
    #     tweet_mode='extended'
    #  )
    cursor = tweepy.Cursor(
        api.search, 
        q="covid vaccine", 
        tweet_mode="extended", 
        lang='en',
        result_type='recent'
    )

    for status in cursor.items(50):
        tweet = {
            'text': get_full_text(status),
            'username': status.user.screen_name,
            'followers_count': status.user.followers_count
            }
        #
#################################################################################
#putting the tweets in mongodb
        #doc = tweets
        db.tweets.insert_one(tweet)
        # db.tweets.find_one({'username':'guardian'})
        # tweets_highfol = db.tweets.find_one({'followers_count':{'$gt':900}})
        # print(tweets_highfol({'username'}))
print(db.tweets.count({}))