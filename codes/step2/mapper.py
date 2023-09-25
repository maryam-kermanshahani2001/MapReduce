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

    reader = csv.reader([line])
    fields = next(reader)

    if line.startswith("created_at"):
        continue

    created_at = fields[0]
    hour_string = fields[0].split()[1]
    state = fields[18]
    tweet = fields[2]

    hour = datetime.strptime(hour_string, "%H:%M:%S").hour
    if state in states_count.keys():
        if 9 <= hour <= 17:
            if ('#JoeBiden' in tweet or '#Biden' in tweet) and ('#DonaldTrump' in tweet or '#Trump' in tweet):
                name = 'Both'
                print('%s\t%s\t%s' % (name, state, 1))

            elif '#JoeBiden' in tweet or '#Biden' in tweet:
                name = 'Biden'
                print('%s\t%s\t%s' % (name, state, 1))

            elif '#DonaldTrump' in tweet or '#Trump' in tweet:
                name = 'Trump'
                print('%s\t%s\t%s' % (name, state, 1))
