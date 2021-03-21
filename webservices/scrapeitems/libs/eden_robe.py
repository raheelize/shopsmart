from bs4 import BeautifulSoup
import requests

def search(query):
    items_list = []
    try:
        link = "https://edenrobe.com/catalogsearch/result/?q="+query
        req = requests.get(link)
        soup = BeautifulSoup(req.text, 'html.parser')
        #print(soup.text)

        titles = soup.find_all('a',{'class':'product-item-link'})
        prices = soup.find_all('span',{'class':'price'})
        img = [i['href'] for i in soup.find_all('a',{'class':'MagicZoom'}, href=True) if i['href'] != "#"]
        for i in range(0,len(titles)):
            TITLE = titles[i].text.replace('\n', '').replace('\t', '').strip()
            #TITLE = TITLE.replace("\t","")
            #TITLE = TITLE.replace("\n","")
            PRICE = prices[i].text
            IMAGE = img[i]
            BRAND = "Eden Robe"
            LINK = titles[i].get('href')
            item = {
                'title': TITLE,
                'price': PRICE,
                'img': IMAGE,
                'brand': BRAND,
                'link': LINK
            }
            #print(item)
            items_list.append(item)
        #print(titles[i].text)
        #print(prices[i].text)
        #print(img[i])
    except(ConnectionError, Exception):
        return False
    return items_list