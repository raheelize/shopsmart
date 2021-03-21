from bs4 import BeautifulSoup
import requests

# search for JunaidJamshed
def search(query):
    items_list = []
    try:
        link = "https://www.junaidjamshed.com/catalogsearch/result/?q="+query
        print(link)
        req = requests.get(link)
        soup = BeautifulSoup(req.text, 'html.parser')
        titles = soup.find_all('a',{'class':'product-item-link'})
        prices = soup.find_all('span',{'class':'price'})
        img_url = soup.find_all('img', {'class':'product-image-photo lazy'})
        X = (len(titles))
        
        #item_link = [i['href'] for i in soup.find_all('a',{'class':'product photo product-item-photo'}, href=True) if i['href'] != "#"]
        #i = range(0,len(titles))
        #print(prices)
        for i in range(0,X):
            #print("in loop")
            #print(titles[i].text)
            #print(prices[i].text)
            #print(img_url[i].get('src'))
            TITLE = titles[i].text
            TITLE = TITLE.replace("\t","")
            TITLE = TITLE.replace("\n","")
            #print(TITLE)
            PRICE = prices[i].text
            IMAGE = img_url[i].get('data-original')
            #IMAGE = IMAGE.replace("?quality=80&bg-color=255,255,255&fit=bounds&height=755&width=589&canvas=589:755","")
            LINK = titles[i].get('href')
            BRAND = "JunaidJamshed"
            print(titles[i].text)
            item = {
                'title': TITLE,
                'price': PRICE,
                'img': IMAGE,
                'brand': BRAND,
                'link': LINK
            }
            #print(item)
            items_list.append(item)
        
    except(ConnectionError, Exception):
        return False
    
    
    return items_list