'''
A scraper to track the number of beds and related information on 
http://www.ncdmh.net/bedavailability/bedavailability.aspx

Other resources here:
https://github.com/openelections/openelections-data-nv/blob/master/precinct_utils.py
https://github.com/jeremyjbowers/slmpd/blob/master/scraper.py

NOTE: This list is missing Northhampton County
'''

#import libraries
import csv, json
from bs4 import BeautifulSoup
import requests
from time import sleep

base_url = 'http://www.ncdmh.net/bedavailability/bedavailability.aspx'
data = {}

#utility function for getting keys
def _set_keys(page_content):
	soup = BeautifulSoup(page_content, "html.parser")
	keys = soup.select('input[type="hidden"]')

	for key in keys:
		data[key['name']] = key['value']

	#is our data there?
	#for d in data:
	#	print d + ": " + data[d]

def main():
	#open a new csv using the entered file name
	writer = csv.writer(open('record.csv', 'wb'))
	writer.writerow(['variable','county','facility_no'])
	print 'State file created...'

	table_data=[]
	select_list=[]
	try:
		r = requests.get(base_url)
		#this is for later
		if int(r.status_code) == 200:
			_set_keys(r.content)
		#restart your bs4 variable
		soup = BeautifulSoup(r.content, "html.parser")
		#build a table with all the appropriate ids
		table = soup.find('table', attrs={'id':'ctl00_ContentPlaceHolder1_gvNumFacilitiesByCounty'})
		#split those into rows
		rows = table.findChildren('tr')
		#for each row, grab the table data 
		for row in rows:
			table_row = []
			cols = row.find_all('td')
			for col in cols:
				if cols.index(col) > 0:
					table_row.append(col.text.strip())
				#if it's the first column, get the select value
				else:
					select = col.find('input')['onclick'].split("NumFacilitiesByCounty','")[1].split("'")[0]
					table_row.append(select)
					select_list.append(select)
					#if you need it, get the first input variable with col.find('input')['onclick'].split("javascript:__doPostBack('")[1].split("',")[0]
			if not table_row:
				pass
			else:
				table_data.append(table_row)
				writer.writerow(table_row)
	except:
		print "ERROR! But I'm not smart enough to tell you where!"

	#open a new csv using the entered file name
	county_writer = csv.writer(open('county-record.csv', 'wb'))
	county_writer.writerow(['variable','type','pop_served','city','name','address','zip','phone','vouchers','in_use','rate'])
	print 'County file created...'

	for select in select_list:
		scrape_county(select,county_writer)
		sleep(1)

def scrape_county(select_value, county_writer):

	#add these values to data for testing
	data['__EVENTTARGET'] = 'ctl00$ContentPlaceHolder1$gvNumFacilitiesByCounty'
	data['__EVENTARGUMENT'] = select_value
	r = requests.post(base_url, data=data)
	soup = BeautifulSoup(r.content, "html.parser")
	table = soup.find('table', attrs={'id':'ctl00_ContentPlaceHolder1_gvNumPerCounty'})
	rows = table.findChildren('tr')
	table_data=[]
	for row in rows:
		table_row = []
		cols = row.find_all('td')
		for col in cols:
			if cols.index(col) > 0:
				table_row.append(col.text.strip())
			else:
				table_row.append(
					col.find('input')['onclick'].split("NumPerCounty','")[1].split("'")[0]
					)
		if not table_row:
			pass
		else:
			table_data.append(table_row)
			county_writer.writerow(table_row)

if __name__ == '__main__':
	
	main()