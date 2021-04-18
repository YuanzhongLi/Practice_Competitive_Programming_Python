from heapq import *
class User:
    def __init__(self, id):
        self.id = id
        self.follower_ids = set([]) # follower id
        self.tweets = [] # (timestamp, tweet id)

    def tweet(self, tweetId, timestamp):
        self.tweets.append((timestamp, tweetId))

    def follow(self, followeeId):
        self.follower_ids.add(followeeId)

    def unfollow(self, followeeId):
        if followeeId in self.follower_ids:
            self.follower_ids.remove(followeeId)


class Twitter:
    def __init__(self):
        self.users = {} # key: userId, value: User
        self.timestamp = 0

    def getUser(self, userId):
        users = self.users
        if not userId in users:
            new_user = User(userId)
            users[userId] = new_user
            return new_user
        else:
            return users[userId]

    def postTweet(self, userId: int, tweetId: int) -> None:
        user = self.getUser(userId)
        user.tweet(tweetId, self.timestamp)
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        user = self.getUser(userId)
        followers = [self.getUser(follower_id) for follower_id in list(user.follower_ids)]
        recent_ten_tweets = []
        for tweet in user.tweets[-10:]:
            heappush(recent_ten_tweets, tweet)

        for follower in followers:
            for tweet in follower.tweets[-10:]:
                heappush(recent_ten_tweets, tweet)
                if len(recent_ten_tweets) > 10:
                    heappop(recent_ten_tweets)

        recent_ten_tweets = list(recent_ten_tweets)
        recent_ten_tweets.sort(reverse=True)
        ret = [tweetId  for _, tweetId in recent_ten_tweets]
        return ret

    def follow(self, followerId: int, followeeId: int) -> None:
        follower = self.getUser(followerId); followee = self.getUser(followeeId)
        follower.follow(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        follower = self.getUser(followerId); followee = self.getUser(followeeId)
        follower.unfollow(followeeId)
