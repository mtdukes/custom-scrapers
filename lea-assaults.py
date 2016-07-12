import sys, urllib2, csv, unicodedata
from bs4 import BeautifulSoup

def scrape_stats():
	#urls run from 0 to 402
	url_count = 0
	#src_url = 'http://crimereporting.ncdoj.gov/public/2013/LEPersonnel/LEPerPopRatAgyTrd/leperpopratagytrd/'
	src_url = 'http://crimereporting.ncsbi.gov/public/2014/LEOKillAsslt/LEOAssltWeaAgyTrd/leoassltweaagytrd/'
	src_url_end = '.htm'

	fieldnames = ['agency_id','agency_name','Year', 'Firearm', 'Knife or Other Cutting Instrument','Other Dangerous Weapon','Hands, Fists, Feet, etc.',' Total Officer Assaults']
	writer = csv.DictWriter(open('lea_assaults.csv', 'wb'),fieldnames=fieldnames)
	lea_row = {'agency_id':'','agency_name':'','Year':'', 'Firearm':0, 'Knife or Other Cutting Instrument':0,'Other Dangerous Weapon':0,'Hands, Fists, Feet, etc.':0,' Total Officer Assaults':0}
	writer.writeheader()
	print 'ALERT: New log created...'

	while url_count < 402:
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
			lea_row = {'agency_id':url_count,'agency_name':lea_name,'Year':'', 'Firearm':0, 'Knife or Other Cutting Instrument':0,'Other Dangerous Weapon':0,'Hands, Fists, Feet, etc.':0,' Total Officer Assaults':0}
			cells = row.findChildren('td')
			current_year = cells[0].string
			if header == 1:
				for cell in cells:
					header_row.append(cell.string)
				header = 0
			else:
				while int(current_year) != expect_year:
					lea_row = {'agency_id':url_count,'agency_name':lea_name,'Year':expect_year, 'Firearm':0, 'Knife or Other Cutting Instrument':0,'Other Dangerous Weapon':0,'Hands, Fists, Feet, etc.':0,' Total Officer Assaults':0}
					writer.writerow(lea_row)
					expect_year += 1
				for cell in cells:
					try:
						value = int(cell.string)
						lea_row[header_row[cell_count]] = value
					except ValueError:
						pass
					cell_count += 1
				writer.writerow(lea_row)
				expect_year += 1
		while int(expect_year) <= 2014:
			lea_row = {'agency_id':url_count,'agency_name':lea_name,'Year':expect_year, 'Firearm':0, 'Knife or Other Cutting Instrument':0,'Other Dangerous Weapon':0,'Hands, Fists, Feet, etc.':0,' Total Officer Assaults':0}
			writer.writerow(lea_row)
			expect_year += 1
		url_count += 1

if __name__ == '__main__':
	scrape_stats()