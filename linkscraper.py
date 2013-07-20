from bs4 import BeautifulSoup   # Imports the BeautifulSoup Module        
import urllib2 					        # Imports the urllib2 module

url = "http://www.putyoursitehere.com"    # Sets the 'url' variable to the site to be scraped 
page = urllib2.urlopen(url)   	          # Uses urrllib2 to open the url variable and sets result to 'page' variable
soup = BeautifulSoup(page.read()) 		    # Uses Soup to read the 'page' variable
for link in soup('a'): 				            # Soup finds all 'a' 
   print(link.get('href'))    		        # prints links gotten, targeted by the string 'href'
   

# NOTE: You can target <a> by CSS classes in line 7. Here's an example:

# for link in soup('a', class_= 'sample-class'):
