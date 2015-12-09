# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

import scraperwiki
import lxml.html
#
# # Read in a page
url = 'http://worldc.am/id/4b058831f964a5200eb822e3'
html = scraperwiki.scrape(url)
#
# # Find something on the page using css selectors
root = lxml.html.fromstring(html)
profiles = root.cssselect("p[class='profileuser profileline']")
for profile in profiles:
  print profile

#
# # Write out to the sqlite database using scraperwiki library
scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
