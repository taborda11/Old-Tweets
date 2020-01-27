import GetOldTweets3 as got
import pandas as pd
from datetime import datetime, timedelta

initial_date = datetime.strptime("2019-01-01", "%Y-%m-%d")
end_date = datetime.strptime("2019-12-31", "%Y-%m-%d")
OUTPUT_FILE = '2019_AMZN_TWEETS_dollar.csv'
QUERY = '$AMZN'

first = True
while initial_date <= end_date:
    print (initial_date.strftime("%Y-%m-%d"))
    next_date = initial_date + timedelta(days=1)  
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch(QUERY)\
                                            .setSince(initial_date.strftime("%Y-%m-%d"))\
                                            .setUntil(next_date.strftime("%Y-%m-%d"))\
                                                .setEmoji("unicode")\
                                                .setLang("en")
                                                
    initial_date = next_date
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    print (len(tweets))

    id = []
    permalink = []
    username = []
    text = []
    date = []
    retweets = []
    mentions = []
    hashtags = []
    geo = []


    for tweet in tweets:
        id.append(tweet.id)
        permalink.append(tweet.permalink)
        username.append(tweet.username)
        text.append(tweet.text)
        date.append(tweet.date)
        retweets.append(tweet.retweets)
        mentions.append(tweet.mentions)
        hashtags.append(tweet.hashtags)
        geo.append(tweet.geo)

    tweets = list(zip(id, permalink, username, text, date, retweets, mentions, hashtags, geo))

    df = pd.DataFrame(tweets, columns=['id', 'permalink', 'username', 'text', 'date', 'retweets', 'mentions', 'hashtags', 'geo'])
    df = df.set_index('id')

    if (first):
        df.to_csv(OUTPUT_FILE, mode='w')
        first = False
    else:
        df.to_csv(OUTPUT_FILE, mode='a', header='false')