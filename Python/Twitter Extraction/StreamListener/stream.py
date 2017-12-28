import tweepy
from tweepy import OAuthHandler

class Listener(tweepy.StreamListener):

	def on_status(self, status):
		try:
			global file
			# print(status.text)
			file.write(str(status.text)+'\n')
		except ValueError:
			with open('data.txt', 'a') as file:
				print('https://twitter.com/'+str(status.screen_name)+'/'+str(status.id))
				file.write(str(status.text)+'\n')
				file.close()


	def on_error(self, status_code):
		if status_code == 420:
			#returning False in on_data disconnects the stream
			return False

consumer_key = 'JsfKHldzYEbkDFW2Wd0KXpLaF'
consumer_secret = '9gErHjaEDAENUKRar1kUpN5TJ6QCYwAUVKGX3nuotNKBQqESM6'
access_token = '727631948907163650-2nEVrIEbShXNIRqa8qvkuACF2HHhvOj'
access_token_secret = 'ScdE82k2xhSk8D69PmqHpK1FAt91tlDvUdrKpNmIZixZi'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

myStream = Listener()
myS = tweepy.Stream(auth = auth, listener= Listener())
with open('data.txt', 'a') as file:
	try:
		myS.filter(track=['morte'], async=True)
	except KeyboardInterrupt:
		file.close()