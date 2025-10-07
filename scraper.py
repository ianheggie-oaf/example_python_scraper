# This is a template for a Python scraper on morph.io (https://morph.io)

import scraperwiki
import lxml.html

# Read in a page
html = scraperwiki.scrape("https://example.com")

# Find something on the page using css selectors
root = lxml.html.fromstring(html)
h1s = root.cssselect("h1")

# Write out to the sqlite database using scraperwiki library
for h1 in h1s:
    value = h1.text_content().strip()
    scraperwiki.sqlite.save(unique_keys=['name'], data={"name": value})

# An arbitrary query against the database
if h1s:
    rows = scraperwiki.sql.select("rowid AS id, name FROM data ORDER BY rowid desc LIMIT 3")
    for row in rows:
        print("{}: {}".format(row['id'], row['name']))

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
