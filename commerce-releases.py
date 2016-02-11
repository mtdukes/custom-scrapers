'''
A scraper to gather the NC Department of Commerce's press releases

using the BeautifulSoup library
accepts a CSV file name (for now) and a url to scrape
'''

#import libraries
import sys, urllib2, csv, json, re
from bs4 import BeautifulSoup
from time import sleep

#main scraper function
def scrape_function(csv_file, url):

	last_page = 0
	current_page = 1
	id_no = 0

	#open a new csv using the entered file name
	with open(csv_file,'wb') as f:
		writer = csv.writer(f)
		writer.writerow(['id','title','release_date','text','link'])
		print 'New file created...'

		#Navigate to root page (http://www.nccommerce.com/news/press-releases)
		html_file = urllib2.urlopen(url).read()
		soup = BeautifulSoup(html_file,'html.parser')

		#Get last page number
		button_links = soup.find_all("a",class_="CommandButton")
		last_page = button_links[len(button_links)-1]['href'].rsplit('=', 1)[-1]

		while current_page <= int(last_page):
			html_file = urllib2.urlopen(url+'?udt_4733_param_page='+str(current_page)).read()
			print 'Page',current_page,'loaded ...'
			soup = BeautifulSoup(html_file,'html.parser')

			#Get all links on page
			release_listing = soup.find_all("a",href=re.compile("udt_4733_param_detail"))
			for link in release_listing:
				page_link = url+link['href']
				release_page = urllib2.urlopen(page_link).read()
				rel_soup = BeautifulSoup(release_page,'html.parser')
				title = rel_soup.find("div",id="dnn_ctr4733_ModuleContent").find("h3").text.strip()
				release_date = rel_soup.find("table",attrs={"width":"100%"}).find("p").text.rsplit('Date:', 1)[-1].strip()
				text = rel_soup.find("table",attrs={"width":"95%"}).find("td").text.strip()
				if text == '* press release includes an attachment *':
					text = rel_soup.find_all("table",attrs={"width":"95%"})[1].find("td").text.strip()
				writer.writerow([id_no,title.encode("utf-8"),release_date,text.encode("utf-8"),page_link])
				id_no += 1
			print 'Page',current_page,'data saved ...'

			current_page += 1

			sleep(2)

if __name__ == '__main__':
	scrape_function('commerce-releases.csv', 'http://www.nccommerce.com/news/press-releases')
	
	print '...done'