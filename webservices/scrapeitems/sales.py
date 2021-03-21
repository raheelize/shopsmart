from bs4 import BeautifulSoup,SoupStrainer
import requests 
import sys
from  account.models import Sale

link = "https://whatsonsale.com.pk/categories/fashion-accessories"
def get_sales():
    #print(link)
    try:
        req = requests.get(link)
        soup = BeautifulSoup(req.text,'lxml')
        
        catalog = soup.find_all('h2',{'class': 'title'})
        description = soup.find_all('div',{'class':'description'})
        links = soup.find_all('div',{'class':'field-item'})
        #print(links)
        for i in range(0,len(catalog)):
            CATALOG = catalog[i].text
            if Sale.objects.filter(catalog=CATALOG):
                continue
            DESC = description[i].text
            SALE_LINK = "https://whatsonsale.com.pk/" + links[i].find('a').get('href')
            IMG = links[i].find('img').get('src')
            print(CATALOG)
            # print(DESC)
            # print(SALE_LINK)
            # print(IMG)
            Sale(catalog=CATALOG, description= DESC, img_url= IMG, sale_url=SALE_LINK).save()
	     
    except(ConnectionError, Exception):
            return False
#get_sales()