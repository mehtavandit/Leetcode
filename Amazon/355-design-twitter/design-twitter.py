class Twitter:

    def __init__(self):
        self.tweets = {}
        self.following = {}
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []
        self.tweets[userId].append((tweetId, self.timestamp))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets_feed = []

        if userId in self.following:
            for followee in self.following[userId]:
                if followee in self.tweets:
                    tweets_feed.extend(self.tweets[followee])

        if userId in self.tweets:
            tweets_feed.extend(self.tweets[userId])

        tweets_feed.sort(key = lambda x: x[1], reverse = True)

        print(tweets_feed)
        
        return [tweet[0] for tweet in tweets_feed[:10]]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = []
        if followeeId not  in self.following[followerId]:
            self.following[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following and followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)