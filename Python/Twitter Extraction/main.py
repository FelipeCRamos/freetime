# This is a simple test for vim
import tweepy
import os
import time
# import json

# from .bin import funcs as func
# Searh for IBM BigFive -> AI for Emotions
class User():
	def __init__(self, name):
		self.screen_name = name
		self.file = ''
		self.tweets = []

	def add_tweet(self, text, created_at):
		self.tweets.append([text, created_at])

''' Variables Declaration '''
consumer_key = 'JsfKHldzYEbkDFW2Wd0KXpLaF'
consumer_secret = '9gErHjaEDAENUKRar1kUpN5TJ6QCYwAUVKGX3nuotNKBQqESM6'
access_token = '727631948907163650-2nEVrIEbShXNIRqa8qvkuACF2HHhvOj'
access_token_secret = 'ScdE82k2xhSk8D69PmqHpK1FAt91tlDvUdrKpNmIZixZi'

''' Auth thingd '''
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

''' File i/o funcs '''
def checkUser(user):
	if ((str(user)+'.txt') not in os.listdir("usr/")):
		return False
	else:
		return True

'''Secondary funcs '''
known, api = [], tweepy.API(auth)

def getTree(user):
	global known
	temp_known = []
	print("###\nTrying with @{}\n###".format(user))
	user = api.get_user(user)
	
	try:
		for friend in user.friends():
			if(friend.screen_name not in known):
				known.append(friend.screen_name)
				if friend.screen_name not in temp_known:
					temp_known.append(friend.screen_name)
				print(friend.screen_name)
				users_file = open('users.txt', 'a')
				users_file.write('{}\n'.format(friend.screen_name))
				users_file.close()

			else:
				print("...")
				# print("{} já estava na lista, ignorando".format(friend.screen_name))
		# getTree(friend.screen_name)
		for user in temp_known:
			print(temp_known)
			getTree(temp_known.pop(0))
	except tweepy.error.RateLimitError:
		print("Limite alcançado, aguardando 1 minuto...")
		time.sleep(60*1)
		getTree(user.screen_name)
	except tweepy.error.TweepError:
		getTree(user.friends()[0])

# Current enemy:
# tweepy.error.RateLimitError: [{'message': 'Rate limit exceeded', 'code': 88}]

''' Main func '''
def main():
	print("Username to fetch:")
	user = User(str(input("@")))
	if checkUser(user.screen_name) == False:
		user.file = open(str(user.screen_name)+'.txt', 'w')
		print("Creating new username file (@{})".format(user.screen_name))
		api = tweepy.API(auth)
		print(tweepy.Cursor(api.user_timeline, id=user.screen_name).pages())
		# for page in tweepy.Cursor(api.user_timeline, id=user.screen_name).pages():
			

	else:
		print
		("Resuming data fetch from page x.")
		try:
			api = tweepy.API(auth)
			for page in tweepy.Cursor(api.user_timeline, id=user.screen_name):
				print(page)
		except :
			print("None pages where found on this username.")
# O dia em que lampiao encontrou eike batista, escutar

# main()
getTree(input('User: @'))
# user = "smothermiu"
print(known)
print(len(known))




# users = ["felipencerramos",
# "felpsisapilgrim",
# "smothermiu"]


# def pullTweets(user):
# 	if(checkUser(user) == True):
# 		tweetCount = 0
# 		lastPage = 0



# def printPage(page):
# 	global count
# 	global tweetCount

# 	for tweet in page:
# 		print('\n')
# 		print("[{}] @".format(tweet.created_at)+str(tweet.user.screen_name)+" said:")
# 		print(tweet.text)
# 		count += 1

# def savePage(page):
# 	global savefile
# 	for tweet in page:
# 		savefile.write('\n')
# 		savefile.write("[{}] @".format(tweet.created_at)+str(tweet.user.screen_name)+" said:")
# 		savefile.write(tweet.text)

# savefile = open('usr/'+str(user)+'.txt', 'a')

# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)

# 
# # f.printPage(api.user_timeline(id='felpsisapilgrim'))



# ''' method 2 '''
# count = 0
# for page in tweepy.Cursor(api.user_timeline, id=user).pages():
# 	printPage(page)
# 	savePage(page)

# savefile.write("\n\nTotal de tweets: {}".format(count))
# savefile.close()
print("Done!")
