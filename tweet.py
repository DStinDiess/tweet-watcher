import tweepy

consumer_key = '__'
consumer_secret = '__'
access_token = '__'
access_token_secret = '__'

accounts = ['DanielStinDiess', 'ImAcrimonious', ]
topics = ['python', ] 


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

class MyStreamListener(tweepy.StreamListener):

	def on_status(self, status):
		if status.user.screen_name in accounts:
			print(status.text)
			# Flash the lights

	def on_error(self, status_code):
		if status_code == 420:
			# Returning False in on_data disconnects the stream
			return False

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener = myStreamListener)


myStream.filter(track = topics, async = True)