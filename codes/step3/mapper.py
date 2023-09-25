#!/usr/bin/env python
import csv
import sys
from datetime import datetime

states_count = {'New York': 0, 'California': 0}
states_tweet_dict = {
    'New York': {'Biden': 0, 'Trump': 0, 'Both': 0}
    , 'California': {'Biden': 0, 'Trump': 0, 'Both': 0}

}
c = 0
for line in sys.stdin:
    # c += 1
    # print(c)
    reader = csv.reader([line])
    fields = next(reader)

    if line.startswith("created_at"):
        continue

    created_at = fields[0]
    hour_string = fields[0].split()[1]
    if fields[13] == "" or fields[3] == " " or fields[14] == "" or fields[14] == " ":
        continue
    lat = float(fields[13])
    long = float(fields[14])
    tweet = fields[2]

    hour = datetime.strptime(hour_string, "%H:%M:%S").hour

    if -79.7624 < long < -71.7517 and 40.4772 < lat < 45.0153:
        state = 'New York'
    elif -124.6509 < long < -114.1315 and 32.5121 < lat < 42.0126:
        state = 'California'
    else:
        continue

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
