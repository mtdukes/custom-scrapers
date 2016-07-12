#Custom scrapers
Here are some scrapers I made. Mostly in Python.

##Scraper template
A template to quickly build scrapers and store information. Accepts a csv filename and a url to scrape. More improvement TK. Will eventually output some json. Copy it and build your own scraper.

**Usage (for testing):**

`cp scraper-template.py your-new-scraper.py`

`python your-new-scraper.py test_csv.csv http://google.com`

##Law enforcement personnel (v2)
A scraper to collect data on law enforcement personnel from the N.C. State Bureau of Investigation's [Uniform Crime Reporting Program](http://crimereporting.ncsbi.gov/), [located here](http://crimereporting.ncsbi.gov/public/2014/LEPersonnel/LEPerPopRatAgyTrd/leperpopratagytrd/leperpopratagytrd.htm).

**Usage:**

`python lea-personnel_v2.py`

##Law enforcement assaults
A scraper to collect data on assaults on law enforcement from the N.C. State Bureau of Investigation's [Uniform Crime Reporting Program](http://crimereporting.ncsbi.gov/), [located here](http://crimereporting.ncsbi.gov/public/2014/LEOKillAsslt/LEOAssltWeaAgyTrd/leoassltweaagytrd/leoassltweaagytrd.htm).

**Usage:**

`python lea-assaults.py`

##Mental health beds
A scraper to collect data on available mental health beds from the N.C. Division of Mental Health, Developmental Disabilities and Substance Abuse Services' [Bed availablility inventory](http://www.ncdmh.net/bedavailability/bedavailability.aspx).

**Usage:**

`python track_beds.py`

##Commerce press releases
A scraper to collect data from [N.C. Department of Commerce press releases](http://www.nccommerce.com/news/press-releases).

**Usage:**

`python commerce-releases.py`