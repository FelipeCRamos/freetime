
consumer_key = 'JsfKHldzYEbkDFW2Wd0KXpLaF'
consumer_secret = '9gErHjaEDAENUKRar1kUpN5TJ6QCYwAUVKGX3nuotNKBQqESM6'
access_token = '727631948907163650-2nEVrIEbShXNIRqa8qvkuACF2HHhvOj'
access_token_secret = 'ScdE82k2xhSk8D69PmqHpK1FAt91tlDvUdrKpNmIZixZi'

#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
    	print(data)
    	return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['feliz', 'animado', 'alegre', 'animada'])
