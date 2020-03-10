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



    # data=pd.read_csv(os.getcwd()+"/followers.csv")
    # # print(data)
    # l=[]
    # print(data["screen_name"][0][35:(len(data["screen_name"][0])-(len(data["screen_name"][0])-36)/2)-4])
    # # print(data["screen_name"][1])
    # f=open(os.getcwd()+"/followers.txt","a")
    # for i in range(len(data["screen_name"])):
    #     f.write(data["screen_name"][i][35:(len(data["screen_name"][i])-(len(data["screen_name"][i])-36)/2)-4]+"\n")
    #     l.append(data["screen_name"][i][35:(len(data["screen_name"][i])-(len(data["screen_name"][i])-36)/2)-4])
    # # print(l)

    data=pd.read_csv(os.getcwd()+"/followers.txt",header=None)
    # print(data[0])
    sample_scores=pyhmeter.load_scores("Data_Set_S1.txt")
    scores=[]
    dates=[]
    days=["%.2d" % i for i in range(1,30)]
    cnt=0
    for month in ["%.2d" % i for i in range(1,13)]:
        for day in range(len(days)-1):
            date="2019-"+str(month)+"-"+str(days[day])
            next_date="2019-"+str(month)+"-"+str(days[day+1])
            day_score=0
            for user in data[0][:100]:
                print("querying...")
                cnt+=1
                print(cnt)
                tweetCriteria=got.manager.TweetCriteria().setUsername(user).setQuerySearch("ClimateChange").setSince(date).setUntil(next_date).setMaxTweets(1)
                
                sum=0
                for i in got.manager.TweetManager.getTweets(tweetCriteria):
                    # printTweet("### Example 1 - Get tweets by username [barackobama]", i)
                    h=pyhmeter.HMeter(list((i.text).split()),sample_scores)
                    sum+=h.happiness_score()
                    # dates.append(i.date)
                    # print(i.date)
                    # l.append(h.happiness_score())
                    # print(h.happiness_score())

                    # cnt+=1
                    # print(cnt)
                sum/=i
                day_score+=sum 
            day_score/=100
            dates.append(date)
            scores.append(day_score)
    datetimes=matplotlib.dates.date2num(dates)
    plt.plot_date(datetimes,scores,marker=None,linestyle="-")
    plt.xticks(rotation=70)
    plt.xlabel("time")
    plt.ylabel("hedonometer score")
    plt.savefig("/home/saksham/Twitter_Project/GetOldTweets-python-master/test3.png")
    plt.show()


if __name__ == '__main__':
    main()
