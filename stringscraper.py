from bs4 import BeautifulSoup         # Imports the BeautifulSoup Module        
import urllib2 					              # Imports the urllib module, spec. urllib2

url = "http://www.anysite.com/"       # Sets the 'url' variable to the site to be scraped 
page = urllib2.urlopen(url)           # Uses urrllib2 to open the url variable and sets result to 'page' variable
soup = BeautifulSoup(page.read())     # Uses Soup to read the 'page' variable

for string in soup.strings:           # Finds strings in soup	
	print(repr(string))			            # Prints all strings in soup doc
	
