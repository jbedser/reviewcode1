import argparse
import os.path
import re
from Tweet import Tweet,TweetUser



Users={}
Tweets=[]

parser = argparse.ArgumentParser(description='Process tweets.')
parser.add_argument('--users', type=str,help='File name for Users list')
parser.add_argument('--tweets', type=str,help='File name for Tweets')

args = parser.parse_args()
#print(args)
if(args.users==None or args.tweets==None):
	print("Please supply names for both User and Tweets files.")
	exit()
if(os.path.exists(args.users)==False):
	print("Please make sure that the file for Users exists.")
	exit()
if(os.path.exists(args.tweets)==False):
	print("Please make sure that the file for Tweets exists.")
	exit()

with open(args.users) as f:
	for line in f:
		user_follows = re.search('(\\w+) follows (.+)', line, re.IGNORECASE)
		if user_follows:
			User_check = user_follows.group(1)
			FollowList_check = user_follows.group(2).replace(" ", "").split(",")
			#print("User_check:{}".format(User_check))
			#print("FollowList_check:{}".format(FollowList_check))
			if User_check not in Users:
				Users[User_check]=TweetUser(User_check)
				
			for follower in FollowList_check:
				if follower not in Users:
					Users[follower]=TweetUser(follower)
				Users[User_check].addFollower(Users[follower])

with open(args.tweets) as f:
	for line in f:
		tweet_regex = re.search('(\\w+)> (.+)', line, re.IGNORECASE)
		if tweet_regex:
			user = tweet_regex.group(1)
			message = tweet_regex.group(2)
			tweet=Tweet(user,message)		
			Tweets.append(tweet)

f.closed
for user in sorted(Users):
	print("{}".format(user))
	#print("showFollowing:{}".format(Users[user].showFollowing()))
	for tweet in Tweets:
		if Users[user].isFollowing(tweet.tweetuser)==True or tweet.tweetuser==user:
			print("@{}:{}".format(tweet.tweetuser,tweet.message))
