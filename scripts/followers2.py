import time
import tweepy
import pandas as pd
import requests


consumer_key = '0ugpcU0KFmk7QU3aGlK8T30LK'
consumer_secret = 'lSmsjzkg619539BRniunhq71cWQHO5BRrCvuN2hgctghtO3wzY'
access_token = '1209190206726799360-iINQ2oyAHyhiEzTnaJDGKpXYRvcnar'
access_token_secret = 'DyqIAsMaOIJXjhdiLAC9IIlbJcnFTrXSvPa4PFPjeGH8W'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)


f=open("/home/saksham/Twitter_Project/GetOldTweets-python-master/followers.txt","r")
cnt=0
followers=[]
their_followers=[]
for i in f:
    cnt+=1
    print(cnt)
    followers.append(i)
    try:
        r=api.followers_ids(i)
        print(len(r))
        their_followers.append(len(r))
    except tweepy.error.TweepError as t:
        their_followers.append(None)

data=pd.DataFrame(list(zip(followers, their_followers)),columns=["Name","NofFollowers"])
data.to_csv("followers_with_values.csv")
f.close()
