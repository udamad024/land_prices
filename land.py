from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://ikman.lk/en/shops/my-colombo-properties'

uClient = uReq(my_url) #opens connection to URL, grabbing the page
page_html = uClient.read() #Gets the HTML file from opened URL
uClient.close() #Closes Connection

#HTML parsing
page_soup = soup(page_html, "html.parser")

containers =  page_soup.findAll("div",{"class":"ui-item"})
print()