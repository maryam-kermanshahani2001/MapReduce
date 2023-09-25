#!/usr/bin/env python3
import sys

likes_count = {'Biden': 0, 'Trump': 0, 'Both': 0}
retweet_count = {'Biden': 0, 'Trump': 0, 'Both': 0}
source_count = {'Twitter Web App': 0, 'Twitter for iPhone': 0, 'Twitter for Android': 0}

# Read input from STDIN
for line in sys.stdin:
    line = line.strip()
    name, likes, retweets, source, src_num = line.split('\t')
    if name == 'Both':
        likes_count['Both'] += float(likes)
        retweet_count['Both'] += float(retweets)
    elif name == 'Biden':
        likes_count['Biden'] += float(likes)
        retweet_count['Biden'] += float(retweets)
    elif name == 'Trump':
        likes_count['Trump'] += float(likes)
        retweet_count['Trump'] += float(retweets)
    if source in source_count.keys():
        source_count[source] += 1

current_word = 'Both'
print('%s\t%s\t%s\t%s\t%s\t%s' % (
    current_word, likes_count['Both'], retweet_count['Both'], source_count['Twitter Web App'],
    source_count['Twitter for iPhone'],
    source_count['Twitter for Android']))

current_word = 'Biden'
print('%s\t%s\t%s\t%s\t%s\t%s' % (
    current_word, likes_count['Biden'], retweet_count['Biden'], source_count['Twitter Web App'],
    source_count['Twitter for iPhone'],
    source_count['Twitter for Android'],
))

current_word = 'Trump'
print('%s\t%s\t%s\t%s\t%s\t%s' % (
    current_word, likes_count['Trump'], retweet_count['Trump'], source_count['Twitter Web App'],
    source_count['Twitter for iPhone'],
    source_count['Twitter for Android'],
))
