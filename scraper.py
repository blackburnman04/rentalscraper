import requests
import time
import csv
import sys
from bs4 import BeautifulSoup

housesforrent = []
housestobuy = []



def saverent():
    filename = input("Please input name of file to be saved")        
    with open (filename + '.csv','w') as file:
       writer=csv.writer(file)
       writer.writerow(['Address','Town', 'Price', 'Period'])
       for row in housesforrent:
          writer.writerow(row)
    print("File Saved Successfully")

def savebuy():
    filename = input("Please input name of file to be saved")        
    with open (filename + '.csv','w') as file:
       writer=csv.writer(file)
       writer.writerow(['Address','Town', 'Price', 'Period'])
       for row in housestobuy:
          writer.writerow(row)
    print("File Saved Successfully")


def rent():
    
    search = input("Please enter town")

    url = "https://www.propertypal.com/property-to-rent/" + search
    page=requests.get(url)
    soup=BeautifulSoup(page.text,"lxml")
    g_data = soup.findAll("div", {"class": "propbox-details"})
    for item in g_data:
        try:
            title = item.find_all("span", {"class": "propbox-addr"})[0].text
        except:
            pass
        try:
            town = item.find_all("span", {"class": "propbox-town"})[0].text
        except:
            pass
        try:
            price = item.find_all("span", {"class": "price-value"})[0].text
        except:
            pass
        try:
            period = item.find_all("span", {"class": "price-period"})[0].text
        except:
            pass
        scrape=[title,town,price,period]
        housesforrent.append(scrape)


    button_next = soup.find("a", {"class": "btn paging-next"}, href=True)
    while button_next:
        time.sleep(2)#delay time requests are sent so we don't get kicked by server
        url = "https://www.propertypal.com{0}".format(button_next["href"])
        page=requests.get(url)
        print(url + "  scraped successfully")
        soup=BeautifulSoup(page.text,"lxml")
        g_data = soup.findAll("div", {"class": "propbox-details"})
        for item in g_data:
            try:
                title = item.find_all("span", {"class": "propbox-addr"})[0].text
            except:
                pass
            try:
                town = item.find_all("span", {"class": "propbox-town"})[0].text
            except:
                pass
            try:
                price = item.find_all("span", {"class": "price-value"})[0].text
            except:
                pass
            try:
                period = item.find_all("span", {"class": "price-period"})[0].text
            except:
                pass
            button_next = soup.find("a", {"class" : "btn paging-next"}, href=True)

            scrape=[title,town,price,period]
            housesforrent.append(scrape)



def buy():
    
    search = input("Please enter town")

    url = "https://www.propertypal.com/property-for-sale/" + search
    page=requests.get(url)
    soup=BeautifulSoup(page.text,"lxml")
    g_data = soup.findAll("div", {"class": "propbox-details"})
    for item in g_data:
        try:
            title = item.find_all("span", {"class": "propbox-addr"})[0].text
        except:
            pass
        try:
            town = item.find_all("span", {"class": "propbox-town"})[0].text
        except:
            pass
        try:
            price = item.find_all("span", {"class": "price-value"})[0].text
        except:
            pass
        try:
            period = item.find_all("span", {"class": "price-period"})[0].text
        except:
            pass
        scrape2=[title,town,price,period]
        housestobuy.append(scrape2)


    button_next = soup.find("a", {"class": "btn paging-next"}, href=True)
    while button_next:
        time.sleep(2)#delay time requests are sent so we don't get kicked by server
        url = "https://www.propertypal.com{0}".format(button_next["href"])
        page=requests.get(url)
        print(url + "  scraped successfully")
        soup=BeautifulSoup(page.text,"lxml")
        g_data = soup.findAll("div", {"class": "propbox-details"})
        for item in g_data:
            try:
                title = item.find_all("span", {"class": "propbox-addr"})[0].text
            except:
                pass
            try:
                town = item.find_all("span", {"class": "propbox-town"})[0].text
            except:
                pass
            try:
                price = item.find_all("span", {"class": "price-value"})[0].text
            except:
                pass
            try:
                period = item.find_all("span", {"class": "price-period"})[0].text
            except:
                pass
            button_next = soup.find("a", {"class" : "btn paging-next"}, href=True)

            scrape2=[title,town,price,period]
            housestobuy.append(scrape2)


def menu():
        strs = ('Enter 1 to search Rental Properties\n'
                'Enter 2 to search for Properties to Buy\n'
                'Enter 3 to Exit\n' )
        choice = input(strs)
        return int(choice) 

while True:          #use while True
    choice = menu()
    if choice == 1:
        rent()
        saverent()
    elif choice == 2:
        buy()
        savebuy()
    elif choice == 3:
        break
    
