
#!/usr/bin/env python
import sys
from twython import Twython
import json
from datetime import datetime
import tweepy
now = datetime.now();
current_time = now.strftime("%H:%M:%S")
print("=",current_time)
tweetStr = raw_input("Type what you want to tweet: ")

#print(test)

#tweetStr =  "ok"
# your twitter consumer and access information goes here
# note: these are garbage strings and won't work
apiKey = 'eDmEXJF5ymgJqt1q33OljC0fo'
apiSecret = 'sj4KlgbElC7yW12R1vVDIfQItXy30FPtCtllMwxGxL70nyAEgc'
accessToken = '1205580133244911616-ROLSWOoFbp2uZ88Shxx4TmfXtqr28i'
accessTokenSecret = 'Jwjtkvlf4REc6pO2j5PUptLVKoh202zBO1ELcc6h7a21A' 
#api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret) i


class StdOutListener(tweepy.StreamListener):

	def on_status(self, status):
		print('------------------------------------------')

		if hasattr(status, 'retweeted_status'):
			try:
				print('Tweet: ' + status.retweeted_status.extended_tweet["full_text"]
			except AttributeError:
				print('Tweet text:' + status.retweeted_status.text
		else:

			try:
				print('Tweeet text: ' + status.full_text);
			except AttributeError:
				print('Tweet text:' + status.text)
#			for hashtag in status.entries['hashtags']:

#				print(hashtag['text'])
		return True


	def on_error(self, status_code):
		print ('Got an error with status code; '+ str(status_code))
		return True

	def on_timeout(self): 
		print('Timout...')
		return True

if __name__ == '__main__':
	listener = StdOutListener()
	tweety = tweepy.OAuthHandler(apiKey, apiSecret)
	tweety.set_access_token(accessToken, accessTokenSecret)
	#api.update_status(status=tweetStr)
	stream = tweepy.Stream(tweety, listener, tweet_mode = 'extended')
	stream.filter(track=['#maga'])
	#api = tweepy.API(tweety)
	#results = api.search(q='from:realDonaldTrump')



#with open("data_file.json", "w") as write_file:
#jsonResults = json.dumps(results)
#data = jsonResults
#print(type(results))
#for x in results["statuses"]:
#	print(x["text"])

#print "Tweeted" +tweetStr       
                        
