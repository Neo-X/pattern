import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from pattern.web import Twitter, hashtags
from pattern.db  import Datasheet, pprint, pd
import json

# This example retrieves tweets containing given keywords from Twitter.

try: 
    # We'll store tweets in a Datasheet.
    # A Datasheet is a table of rows and columns that can be exported as a CSV-file.
    # In the first column, we'll store a unique id for each tweet.
    # We only want to add the latest tweets, i.e., those we haven't seen yet.
    # With an index on the first column we can quickly check if an id already exists.
    # The pd() function returns the parent directory of this script + any given path.
    table = Datasheet.load(pd("cool.csv"))
    index = set(table.columns[0])
except:
    table = Datasheet()
    index = set()

engine = Twitter(language="en")

# With Twitter.search(cached=False), a "live" request is sent to Twitter:
# we get the most recent results instead of those in the local cache.
# Keeping a local cache can also be useful (e.g., while testing)
# because a query is instant when it is executed the second time.
prev=None
groups = 30
for i in range(groups):
    # 49.253000,-123.111432,25mi
    # results = engine.search("#feelthebern", start=prev, count=100, cached=False, date='2016-02-14', geo=(latitude, longitude, radius))
    results = engine.search("geocode:49.253000,-123.111432,50mi", start=prev, count=100, cached=False)
    # results = engine.search("#SingleLifeIn3Words", start=prev, count=100, cached=False, date='2016-02-14')
    for tweet in results:
        print
        # print str(tweet.text)
        print tweet.author
        print tweet.date
        print hashtags(tweet.text) # Keywords in tweets start with a "#".
        print
        # Only add the tweet to the table if it doesn't already exists.
        if len(table) == 0 or tweet.id not in index:
            # remove new lines
            tweet.text = tweet.text.replace("\n", "")
            # tweet.raw = unicode(tweet.raw).encode('utf8').replace("\n", "")
            tweet.raw = json.dumps(tweet.raw, separators=(',', ': ')).replace("\n", "")
            table.append([tweet.id, tweet.text, tweet.date, tweet.language, tweet.shares, tweet.geo, tweet.geo_lat, tweet.geo_long, tweet.user_id, tweet.location, tweet.statuses_count, tweet.followers_count, tweet.friends_count, tweet.raw])
            index.add(tweet.id)
        # Continue mining older tweets in next iteration.
        prev = tweet.id

# Create a .csv in pattern/examples/01-web/
table.save(pd("cool.csv"))

print "Total results:", len(table)
print

# Print all the rows in the table.
# Since it is stored as a CSV-file it grows comfortably each time the script runs.
# We can also open the table later on: in other scripts, for further analysis, ...

# pprint(table, truncate=100)

# Note: you can also search tweets by author:
# Twitter().search("from:tom_de_smedt")
