# twitter_sentiment_anaysis
This is a twitter sentiment analysis module which provide you a graph of sentiments of tweets which you have streamed

To train the classifiers you will need this folder in the same directory https://drive.google.com/open?id=1Fx3NbPYxPgb9zylAdCMz5grTvUejRgcU by running the script training.py

pickle each one of classifiers by running the script pickle.py

Sentiment_mod.py returns the sentiment value and its confidence level which is then imported by twitter_stream.py to output the sentiment of streamed tweets to the tweet-out.txt file.

Graph is shown by the no. of positive and negative tweets in the tweet-out.txt by running the script graphing_data.py

