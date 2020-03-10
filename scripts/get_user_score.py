# coding: utf-8
import pyhmeter
import got
import matplotlib.pyplot as plt
import sys
import matplotlib
import pandas as pd
import os
import re

sample_scores=pyhmeter.load_scores("Data_Set_S1.txt")
scores=[]
dates=[]
tweets=[]
url_rem=[]
neutral_rem=[]
normal=[]
url_score=[]
neutral_score=[]
# tweetCriteria=got.manager.TweetCriteria().setUsername("barackobama").setQuerySearch("ClimateChange").setSince('2019-03-01').setUntil('2019-12-30').setMaxTweets(10000)
tweetCriteria = got.manager.TweetCriteria().setUsername("KremlinRussia_E").setQuerySearch("Climate").setSince("2009-12-30").setUntil("2019-12-30").setMaxTweets(100000)
print(got.manager.TweetManager.getTweets(tweetCriteria))
for i in got.manager.TweetManager.getTweets(tweetCriteria):
    text=re.sub(r'[^\x00-\x7F]+',' ', i.text)
    tweets.append(text)
    h=pyhmeter.HMeter(list(i.text.split()),sample_scores)
    normal.append(h.happiness_score())
    h.deltah=1.0
    neutral_score.append(h.happiness_score())
    neutral_rem.append(h.matchlist)
    dates.append(i.date)

data=pd.DataFrame(list(zip(tweets,neutral_rem,normal,neutral_score)),columns=['normal','cleaned_tweets','no_clean','cleaned_score'])
data.to_csv(os.getcwd()+"/putin(2009-2020)cleaned(deltah=1.0).csv",sep="|")
datetimes=matplotlib.dates.date2num(dates)
plt.plot_date(datetimes,neutral_score,marker=None,linestyle="-")
plt.xticks(rotation=70)
plt.xlabel("time")
plt.ylabel("hedonometer score")
plt.savefig("/home/saksham/Twitter_Project/GetOldTweets-python-master/putin(2009-2020)cleaned(delta=1.0).png")
plt.show()
