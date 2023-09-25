#!/usr/bin/env python
import csv
import sys
from datetime import datetime

states_count = {'New York': 0, 'Texas': 0, 'California': 0, 'Florida': 0}
states_tweet_dict = {
    'New York': {'Biden': 0, 'Trump': 0, 'Both': 0}
    , 'Texas': {'Biden': 0, 'Trump': 0, 'Both': 0}
    , 'California': {'Biden': 0, 'Trump': 0, 'Both': 0}
    , 'Florida': {'Biden': 0, 'Trump': 0, 'Both': 0}
}

for line in sys.stdin:

    line = line.strip()
    name, state, count_state = line.split('\t')

    if name == 'Both':
        states_tweet_dict[state][name] += 1
    elif name == 'Biden':
        states_tweet_dict[state][name] += 1
    elif name == 'Trump':
        states_tweet_dict[state][name] += 1

    states_count[state] += 1

# Emit the final results
current_word = 'Biden'
print('%s\t%s\t%s\t%s\t%s' % (
    'New York', states_tweet_dict['New York']['Both'] / states_count['New York'],
    states_tweet_dict['New York']['Biden'] / states_count['New York'],
    states_tweet_dict['New York']['Trump'] / states_count['New York'],
    states_count['New York'],
))

print('%s\t%s\t%s\t%s\t%s' % (
    'Texas', states_tweet_dict['Texas']['Both'] / states_count['Texas'],
    states_tweet_dict['Texas']['Biden'] / states_count['Texas'],
    states_tweet_dict['Texas']['Trump'] / states_count['Texas'],
    states_count['Texas'],
))

print('%s\t%s\t%s\t%s\t%s' % (
    'California', states_tweet_dict['California']['Both'] / states_count['California'],
    states_tweet_dict['California']['Biden'] / states_count['California'],
    states_tweet_dict['California']['Trump'] / states_count['California'],
    states_count['California'],
))

print('%s\t%s\t%s\t%s\t%s' % (
    'Florida', states_tweet_dict['Florida']['Both'] / states_count['Florida'],
    states_tweet_dict['Florida']['Biden'] / states_count['Florida'],
    states_tweet_dict['Florida']['Trump'] / states_count['Florida'],
    states_count['Florida'],
))
