#A template for quickly building basic scrapers
#using the BeautifulSoup library
#accepts a CSV file name (for now) and a url to scrape

#import libraries
import sys, urllib2, csv, json
from bs4 import BeautifulSoup
import argparse

#main scraper function
def scrape_function(csv_file, url):

	#open a new csv using the entered file name
	writer = csv.writer(open(csv_file, 'wb'))
	writer.writerow(['column_1','column_2','column_3','column_4'])
	print 'New file created...'

	try:
		html_file = urllib2.urlopen(url).read()
		print 'Page loaded ...'
		soup = BeautifulSoup(html_file)

		#This template just grabs the page title
		writer.writerow([soup.title])
		print 'Row written ...'

	except:
		print 'ERROR!'


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Download the files from a station RSS feed')
	parser.add_argument('file',help='Enter the destination file name')
	parser.add_argument('path',help='Enter the url to scrape')
	args = parser.parse_args()
	
	scrape_function(args.file, args.path)
	
	print '...done'