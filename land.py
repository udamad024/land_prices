from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import os

def land_checks(web,num):
  my_url = 'https://ikman.lk/en/shops/{inp}?page={n}'.format(inp=web,n=num)

  uClient = uReq(my_url) #opens connection to URL, grabbing the page
  page_html = uClient.read() #Gets the HTML file from opened URL
  uClient.close() #Closes Connection

  #HTML parsing
  page_soup = soup(page_html, "html.parser")

  containers =  page_soup.findAll("div",{"class":"ui-item"})

  if os.path.exists("products{}.csv".format(num)):
    os.remove("products{}.csv".format(num))
  else:
    print("The file does not exist")

  filename = "products{}.csv".format(num)
  f = open(filename, "w")

  headers = "Land_Name, Land_price\n"  # header in csv file (excel)
  f.write(headers)  # #first line is header

  for container in containers:
    title_container = container.findAll("a",{"class":"item-title h4"})
    product_name = title_container[0].text

    price = container.findAll("p",{"class":"item-info"})
    product_price = price[0].text

    print("Title: " + product_name)
    print("Price: " + product_price)

    f.write(product_name + "," + product_price.replace(",", " ") + "\n")

  f.close()

ints = input("Enter Ikman Shop name: ")
num = int(input("Please Enter Requried number: "))

land_checks(ints,num)