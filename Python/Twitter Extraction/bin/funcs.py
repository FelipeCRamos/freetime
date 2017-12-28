def printPage(page):
	global count
	for tweet in page:
		print('\n')
		print("[{}] @".format(tweet.created_at)+str(tweet.user.screen_name)+" said:")
		print(tweet.text)
		count += 1

def savePage(page):
	global savefile
	for tweet in page:
		savefile.write('\n')
		savefile.write("[{}] @".format(tweet.created_at)+str(tweet.user.screen_name)+" said:")
		savefile.write(tweet.text)
