import pyhmeter
import got
import matplotlib.pyplot as plt
import sys
import matplotlib
import pandas as pd
import os


def main():

    def printTweet(descr, t):
        print(descr)
        print("Username: %s" % t.username)
        print("Retweets: %d" % t.retweets)
        print("Text: %s" % t.text)
        print("Mentions: %s" % t.mentions)
        print("Hashtags: %s\n" % t.hashtags)


    data=pd.read_csv(os.getcwd()+"/followers.txt",header=None)
    # print(data[0])
    sample_scores=pyhmeter.load_scores("Data_Set_S1.txt")
    scores=[]
    dates=[]    
    cnt=0
    average_score=0
    for month in ["%.2d" % i for i in range(1,13)]:
        monthly_score=0
        user_cnt=0
        cnt=0
        for user in data[0].sample(n=2000):
            tweetCriteria=got.manager.TweetCriteria().setUsername(user).setQuerySearch("ClimateChange").setSince("2019-"+month+"-01").setUntil("2019-"+month+"-30").setMaxTweets(10)
            # sum=0
            # cnt=0
            for i in got.manager.TweetManager.getTweets(tweetCriteria):
                # printTweet("### Example 1 - Get tweets by username [barackobama]", i)
                user_cnt+=1
                h=pyhmeter.HMeter(list((i.text).split()),sample_scores)
                if h.happiness_score() is not None:
                    monthly_score+=h.happiness_score()
                    print(cnt)
                    cnt+=1
                print(user)
                print(h.happiness_score())
                # dates.append(i.date)
                # print(i.date)
                # l.append(h.happiness_score())
                # print(h.happiness_score())
        if cnt!=0:
            # monthly_score+=sum
            monthly_score/=cnt
        print(monthly_score)
        scores.append(monthly_score)
        average_score+=monthly_score
        dates.append(month)
    # datetimes=matplotlib.dates.date2num(dates)
    # plt.plot_date(datetimes,scores,marker=None,linestyle="-")
    average_score/=len(scores)
    print(scores,dates)
    plt.plot(dates,scores,label="actual data",color="red")
    plt.axhline(y=average_score,label="average score")
    # plt.plot(average_score)
    plt.xticks(rotation=70)
    plt.xlabel("time(month)")
    plt.ylabel("hedonometer score")
    plt.legend()
    # plt.title("")
    plt.savefig("/home/saksham/Twitter_Project/GetOldTweets-python-master/test3.png")
    plt.show()
        
        







if __name__ == '__main__':
    main()