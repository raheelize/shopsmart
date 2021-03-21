from bs4 import BeautifulSoup
import requests

def search(query):
    items_list = []
    try:
        link = "https://www.gulahmedshop.com/catalogsearch/result/?q="+query
        req = requests.get(link)
        soup = BeautifulSoup(req.text, 'html.parser')
        titles = soup.find_all('a',{'class':'product-item-link'})
        prices = soup.find_all('span',{'class':'price'})
        img_url = soup.find_all('img', {'class':'product-image-photo'})
        #//*[@id="category-products-grid"]/ol/li[1]/div/div[1]/div[1]/a/span[1]/span/span/img
        item_link = [i['href'] for i in soup.find_all('a',{'class':'product-item-link'}, href=True) if i['href'] != "#"]
        for i in range(0,len(titles)):
            TITLE = titles[i].text
            TITLE = TITLE.replace("\t","")
            TITLE = TITLE.replace("\n","")
            PRICE = prices[i].text
            IMAGE = img_url[i].get('src')
            #IMAGE = IMAGE.replace(".pagespeed.ic.py1u_bk3_f.webp","")
            LINK = item_link[i]
            BRAND = "Gul Ahmed"
            item = {
                'title': TITLE,
                'price': PRICE,
                'img': IMAGE,
                'brand': BRAND,
                'link': LINK
            }
            print(item)
            items_list.append(item)
        
    except(ConnectionError, Exception):
        return False

    return items_list