#Custom scrapers
Here are some scrapers I made. Mostly in Python.

##Scraper template
A template to quickly build scrapers and store information. Accepts a csv filename and a url to scrape. More improvement TK. Will eventually output some json. Copy it and build your own scraper.

**Usage (for testing):**

`cp scraper-template.py your-new-scraper.py'

`python your-new-scraper.py test_csv.csv http://google.com`

##Law enforcement personnel
A scraper to collect data on law enforcement personnel from the N.C. Department of Justice's [Uniform Crime Reporting Program](http://crimereporting.ncdoj.gov/Reports.aspx), [located here](http://crimereporting.ncdoj.gov/public/2013/LEPersonnel/LEPerPopRatAgyTrd.htm).

**Usage:**

`python lea-personnel.py`