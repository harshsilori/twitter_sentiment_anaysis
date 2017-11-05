from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

import json

import sentiment_mod as s

#consumer key, consumer secret, access token, access secret.
ckey="MROK32neWVKqIlC0pRIx5qbXp"
csecret="jEe66g5EtigmmDCT84fv5hBSjsbbMiVTSbtzrVu6fQLuRjCksl"
atoken="782522413-s8VnYEv4Wcnh7e0ZiI7PsKHavn0yjS5uaHgeHBWe"
asecret="DqfsK9D4Redi0rvNkdnc8oDX70npNiOAXdog1eFFY0eHz"

class listener(StreamListener):

    def on_data(self, data):
        try:
            
            all_data = json.loads(data)
            tweets = all_data["text"]
            sentiment,confidence = s.sentiment(tweets)
            print(tweets, sentiment, confidence)
            with open("twitter-out.txt",mode="a", encoding="utf-8") as myfile:
                
                myfile.write(sentiment)
                myfile.write("\n")
                
            
            return(True)
        except:
            return True
        
    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["Trump"])
