import tweepy
import os

API_KEY = "..."
API_SECRET = "..."

# OAuth2: app context only
# OAuth 2 - APP only - read-only access to public information.
auth = tweepy.OAuthHandler(
    consumer_key = API_KEY, 
    consumer_secret = API_SECRET
)

try:
    # get the request token (verification code) from twitter
    redirect_url = auth.get_authorization_url()
    print(f'Please visit: {redirect_url}')
    verifier = input('Please input verifier: ')

    # get the access token key and secret
    access_token = auth.get_access_token(verifier)

    # update the authentification
    auth.set_access_token(*access_token)

   # test it
    api = tweepy.API(auth)
    for status in api.home_timeline():
        print(status.text)

    # print to output
    for token, label in zip(access_token, ['ACCESS_TOKEN', 'ACCESS_TOKEN_SECRET']):
        print(f'{label}={token}')

except tweepy.TweepError:
    print('Error! User authentification failed.')



