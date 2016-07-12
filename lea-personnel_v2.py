import sys, urllib2, csv, unicodedata
from bs4 import BeautifulSoup

def scrape_stats():
	#urls run from 0 to 605
	url_count = 0
	src_url = 'http://crimereporting.ncsbi.gov/public/2014/LEPersonnel/LEPerPopRatAgyTrd/leperpopratagytrd/'
	src_url_end = '.htm'

	fieldnames = ['agency_id','Agency Name','Year','Reporting Status','Fulltime Male Sworn','Fulltime Female Sworn','Fulltime Male Civilian','Fulltime Female Civilian','Total Employees','Population Coverage','Sworn Rate per 1,000 Population']
	writer = csv.DictWriter(open('lea_personnel.csv', 'wb'),fieldnames=fieldnames)
	lea_row = {'agency_id':'','Agency Name':'','Year':'','Reporting Status':'','Fulltime Male Sworn':0,'Fulltime Female Sworn':0,'Fulltime Male Civilian':0,'Fulltime Female Civilian':0,'Total Employees':0,'Population Coverage':0,'Sworn Rate per 1,000 Population':0}
	writer.writeheader()
	print 'ALERT: New log created...'

	while url_count < 605:
		expect_year = 2005
		print src_url + str(url_count) + src_url_end
		html_file = urllib2.urlopen(src_url + str(url_count) + src_url_end).read()
		soup = BeautifulSoup(html_file, 'html.parser')

		for lea_detail in soup.findChildren('table')[11].findChildren('td'):
			lea_name = lea_detail.string

		data_table = soup.findChildren('table')[12]

		rows = data_table.findChildren('tr')
		header = 1
		header_row = []
		for row in rows:
			cell_count = 0
			cells = row.findChildren('td')
			if header == 1:
				for cell in cells:
					header_row.append(cell.string)
				header = 0
			else:
				while int(cells[1].string) != expect_year:
					lea_row = {'agency_id':url_count,'Agency Name':cells[0].string,'Year':expect_year,'Reporting Status':'','Fulltime Male Sworn':'','Fulltime Female Sworn':'','Fulltime Male Civilian':'','Fulltime Female Civilian':'','Total Employees':'','Population Coverage':'','Sworn Rate per 1,000 Population':''}
					writer.writerow(lea_row)
					expect_year += 1
				lea_row = {'agency_id':url_count,'Agency Name':cells[0].string,'Year':'','Reporting Status':'','Fulltime Male Sworn':0,'Fulltime Female Sworn':0,'Fulltime Male Civilian':0,'Fulltime Female Civilian':0,'Total Employees':0,'Population Coverage':0,'Sworn Rate per 1,000 Population':0}
				for cell in cells:
					try:
						value = int(cell.string.replace(',',''))
						lea_row[header_row[cell_count].lstrip()] = value
					except ValueError:
						if cell.string == 'Does Not Participate' or cell.string == 'Reporting':
							lea_row[header_row[cell_count].lstrip()] = cell.string
					cell_count += 1
				writer.writerow(lea_row)
				expect_year += 1
		url_count += 1

if __name__ == '__main__':
	scrape_stats()