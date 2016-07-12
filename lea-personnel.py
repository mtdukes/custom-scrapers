import sys, urllib2, csv
from bs4 import BeautifulSoup

def scrape_stats():
	#urls run from 0 to 604
	url_count = 0
	src_url = 'http://crimereporting.ncsbi.gov/public/2014/LEPersonnel/LEPerPopRatAgyTrd/leperpopratagytrd/'
	src_url_end = '.htm'

	writer = csv.writer(open('lea_personnel.csv', 'wb'))
	writer.writerow(['agency_id','agency_name','year','reporting_status','male_sworn','female_sworn','male_civilian','female_civilian','total','population_coverage','sworn_rate'])
	print 'ALERT: New log created...'

	while url_count <= 10:
		try:
			print src_url + str(url_count) + src_url_end
			html_file = urllib2.urlopen(src_url + str(url_count) + src_url_end).read()
			soup = BeautifulSoup(html_file)

			data_table = soup.findChildren('table')[12]

			rows = data_table.findChildren('tr')
			for row in rows:
				row_values = []
				row_values.append(url_count)
				cells = row.findChildren('td')
				for cell in cells:
					row_values.append(cell.string)
				writer.writerow(row_values)
		except:
			print 'ERROR: ' + str(url_count)
		url_count += 1

if __name__ == '__main__':
	scrape_stats()
	print '...done'