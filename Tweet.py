class Tweet(object):
	tweetmessage=""
	tweetuser=""
	def __init__(self,user,message):
		self.tweetuser=user
		self.message=message

class TweetUser(object):

	Name=""
	Following=[]
	Followers=[]
	Tweets=[]
	def __init__(self,name):
		self.Name=name
		self.Following=[]

	def _str_(self):
		print("TweetUser:{} FollowList:{}\nTweets:{}".format(self.Name,self.FollowList,self.Tweets))

	def addFollower(self,followUser):
		if self.isFollowing(followUser.Name)==False:
			#print("{} following {}".format(self.Name,followUser.Name))
			self.Following.append(followUser)

	def isFollowing(self,User):
		for user in self.Following:
			if user.Name==User:
				return True
		return False

	def showFollowing(self):
		result=""
		for user in self.Following:
			result=result+user.Name+" "
		return result