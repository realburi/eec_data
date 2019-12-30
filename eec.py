from bs4 import BeautifulSoup as soup
import requests 

def crawler(url):
	data = requests.get(url, params=None)
	data.encoding = "utf-8"
	crawler = soup(data.text, "html.parser")
	table = crawler.find("table")
	tr = table.findAll('tr')

	table_content = []
	count = 0
	for item in tr:
		table_content.append(item)

	output_rows = []

	for table_row in table_content:
 	    columns = table_row.findAll('td')
 	    output_row = []
 	    for column in columns:
 	        output_row.append(column.text)
 	    output_rows.append(output_row)

	return output_rows
