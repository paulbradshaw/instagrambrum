#!/usr/bin/env python

import scraperwiki
import requests
import lxml.html
import re

#Copy and paste a column from excel within the ''' markers to create a variable
pastedfromexcel = '''kerry_hill205
stirchleywines
puredestination
galateadesigns
carlwalters
honeymoon_dreams
dawnqueen5
dayllen44
purpledecember84'''

#This then splits that variable on each carriage return, to create a list of usernames
usernamelist = pastedfromexcel.split('\n')
baseurl = 'https://www.instagram.com/'
url = 'https://www.instagram.com/bhameastside/'

#Here we define a function which uses the username as an argument
def grabfollows(username):
    #create the full URL by joining the username to the baseurl
    userurl = baseurl+username
    #scrape it into 'html'
    html = scraperwiki.scrape(userurl)
    #convert it to an lxml object
    root = lxml.html.fromstring(html)
    print root
    #grab anything in <script> tags
    headers = root.cssselect('script')
    #the 7th one (index 6) has what we need
    print headers[6].text
    profiledata = headers[6].text
    #split the contents of that tag in two, grab the second part, then split that part again and grab the first part
    follows = profiledata.split('follows":{"count":')[1].split('}')[0]
    followers = profiledata.split('"followed_by":{"count":')[1].split('}')[0]
    print "FOLLOWS:", follows
    print "FOLLOWERS:", followers
    #create the fields in our dictionary, and assign variables to those
    record['follows'] = follows
    record['followers'] = followers 
    record['username'] = username 
    #save the whole thing, with username as the unique key
    #in Morph.io we just need to change sql to sqlite
    scraperwiki.sqlite.save(['username'], record)

#create an empty record (this will be filled when the function runs above)
record = {}
#loop through our username list
for username in usernamelist:
    #run the function defined above on each username
    grabfollows(username)

#html = requests.get(url)
#print html.content

# Saving data:



