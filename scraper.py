#!/usr/bin/env python

import scraperwiki
import requests
import lxml.html
import re

lots = '''kerry_hill205
stirchleywines
puredestination
galateadesigns
carlwalters
honeymoon_dreams
dawnqueen5
dayllen44
purpledecember84'''

lotslist = lots.split('\n')
print lotslist
# # Read in a page
#url = 'http://worldc.am/id/4b058831f964a5200eb822e3'
#url = 'https://www.instagram.com/p/-0ICf6gPdN/'
baseurl = 'https://www.instagram.com/'
url = 'https://www.instagram.com/bhameastside/'

# # Find something on the page using css selectors
def grabfollows(username):
    userurl = baseurl+username
    html = scraperwiki.scrape(userurl)
    root = lxml.html.fromstring(html)
    print root
    #profiles = root.cssselect('script')
    headers = root.cssselect('script')
    print headers[6].text
    profiledata = headers[6].text
    follows = profiledata.split('follows":{"count":')[1].split('}')[0]
    followers = profiledata.split('"followed_by":{"count":')[1].split('}')[0]
    print "FOLLOWS:", follows
    print "FOLLOWERS:", followers
    record['follows'] = follows
    record['followers'] = followers 
    record['username'] = username 
    scraperwiki.sqlite.save(['username'], record)


record = {}
for username in lotslist:
    grabfollows(username)

#html = requests.get(url)
#print html.content

# Saving data:



