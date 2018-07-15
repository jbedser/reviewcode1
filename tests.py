import unittest
from Tweet import Tweet,TweetUser
class TestStringMethods(unittest.TestCase):

    def test_create_user(self):
        user=TweetUser("TestUser")
        self.assertEqual(user.Name, 'TestUser')

    def test_add_follower(self):
        user1=TweetUser("TestUser1")
        user2=TweetUser("TestUser2")
        user1.addFollower(user2)
        self.assertEqual(user1.showFollowing(), 'TestUser2 ')

    def test_create_tweet(self):
    	tweet=Tweet("TestUser1","Test Message")
    	self.assertEqual(tweet.tweetuser, "TestUser1")
    	self.assertEqual(tweet.message, "Test Message")


if __name__ == '__main__':
    unittest.main()