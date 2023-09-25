#!/usr/bin/env python3
import csv
import sys

likes_count = {'Biden': 0, 'Trump': 0, 'Both': 0}
retweet_count = {'Biden': 0, 'Trump': 0, 'Both': 0}
source_count = {'Twitter Web App': 0, 'Twitter for iPhone': 0, 'Twitter for Android': 0}

for line in sys.stdin:

    reader = csv.reader([line])
    fields = next(reader)

    if line.startswith("created_at"):
        continue

    tweet = fields[2]
    likes = float(fields[3])
    retweets = float(fields[4])
    source = fields[5]

    if ('#JoeBiden' in tweet or '#Biden' in tweet) and ('#DonaldTrump' in tweet or '#Trump' in tweet):
        print('%s\t%s\t%s\t%s\t%s' % ('Both', likes, retweets, source, 1))

    elif '#JoeBiden' in tweet or '#Biden' in tweet:
        print('%s\t%s\t%s\t%s\t%s' % ('Biden', likes, retweets, source, 1))

    elif '#DonaldTrump' in tweet or '#Trump' in tweet:
        print('%s\t%s\t%s\t%s\t%s' % ('Trump', likes, retweets, source, 1))


