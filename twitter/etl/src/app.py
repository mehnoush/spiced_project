
import pymongo
from sqlalchemy import create_engine
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer



print('ETL job started')

print('EXTRACT')

client = pymongo.MongoClient(host="mongodb", port=27017)

print(f'this is our mongodb connection: {client}')

db = client.twitter
print(db.tweets.count_documents(filter={}))

#result = db.tweets.find()

#print(f"we have EXTRACTED {result} from mongodb")


#print(db.tweets.count())
#db.tweets.find_one({'username':'guardian'})
# tweets_highfol = db.tweets.find()
# print(db.tweets_highfol.count_documents(filter={}))
# #tweets_highfol=[] 
#print("TRANSFORM")
# df_tweet=pd.DataFrame(result)
# dic_tweet=df_tweet.to_dict()
# print(dic_tweet)

s  = SentimentIntensityAnalyzer()
tweets_900 = db.tweets.find(filter={'followers_count': {"$gt": 900}}) 
tweet_bd = []
for tweet in tweets_900:
    tweet_bd.append(tweet)

#
provax =[]
antivax=[]
for tweet in  tweet_bd:
    sentiment = s.polarity_scores(tweet['text'])
    #print(sentiment)
    tweet['sentiment'] = sentiment['compound']
    if tweet['sentiment']>0:
        provax.append(tweet)
        tweet['opinion']='provax'
    else:
        antivax.append(tweet) 
        tweet['opinion']='antivax'
print('nomber of provax and antivax accounts')


# print(provax.head(3))
# print(antivax.head(3))



tweet_df = pd.DataFrame(tweet_bd)
print(tweet_df.columns)

tweet_df.drop('_id', axis = 1 , inplace=True)
print(tweet_df.columns)

df_provax = tweet_df.loc[tweet_df['opinion']== 'provax']
print(df_provax.head())
df_antivax = tweet_df.loc[tweet_df['opinion']== 'provax']
print(df_provax.head())

if len(tweet_df)==0:
    print('no data in dataframe to push to postgres')

print('LOAD')

engine = create_engine('postgresql://postgres:xxxx@db:5432/')

print(f'connection to postgres defined: {engine}')

tweet_df.to_sql('tweets', engine, if_exists='replace', index=False)


print("ETL finsihed!")


