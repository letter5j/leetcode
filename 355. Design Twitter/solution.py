from __future__ import annotations
from queue import PriorityQueue
from typing import Dict, List, Set


class Tweet:
    def __init__(self, tweet_id: int, timestamp: int, next: Tweet = None):
        self.tweet_id = tweet_id
        self.timestamp = timestamp
        self.next = next

    def __gt__(self, other):
        return self.timestamp < other.timestamp


class Twitter:
    userid_news: Dict[int, Tweet]
    followee_map: Dict[int, Dict[int, bool]]

    def __init__(self):
        self.userid_news = dict()
        self.followee_map = dict()
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count = self.count + 1
        tweet_next = self.userid_news[userId] if userId in self.userid_news else None

        self.userid_news[userId] = Tweet(tweetId, self.count,
                                         tweet_next)

    def getNewsFeed(self, userId: int) -> List[int]:
        result = list()
        priority_queue: PriorityQueue = PriorityQueue(len(self.followee_map) + 1)

        if userId in self.userid_news:
            priority_queue.put(self.userid_news[userId])
        if userId in self.followee_map:
            for follower in self.followee_map[userId].keys():
                if follower in self.userid_news:
                    priority_queue.put(self.userid_news[follower])

        while priority_queue.qsize() != 0:
            if len(result) == 10:
                break
            tweet: Tweet = priority_queue.get()
            result.append(tweet.tweet_id)
            if tweet.next is not None:
                priority_queue.put(tweet.next)

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followee_map.setdefault(followerId, dict())
        followers: Dict[int, bool] = self.followee_map[followerId]
        followers[followeeId] = True

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followee_map:
            followers: Dict[int, bool] = self.followee_map[followerId]
            followers.pop(followeeId, None)
