import os
from typing import Dict
import pandas as pd
from sqlalchemy import create_engine
import requests

engine = create_engine('postgresql://postgres:xxxx@db:5432/')
query = 'select * from tweets'
df_tweet = pd.read_sql(query, engine)
print(df_tweet)

webhook_url = "https://hooks.slack.com/services/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"
tweet_shot = df_tweet.sample(n=1)

data = {'text': tweet_shot['text'].item()}
print(data)
requests.post(url=webhook_url, json=data)