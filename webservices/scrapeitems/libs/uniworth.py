import _essentials

#seach from uniworth items
def search(query):
    try:
        link = "https://www.uniworthshop.com/search?keywords="+query
        req = requests.get(link)
        soup = BeautifulSoup(req.text, 'html.parser')
        titles = soup.find_all('div',{'class':'product-name'})
        prices = soup.find_all('span',{'class':'price'})
        img_url = soup.find_all('img', {'class':'primary'})
        item_link = [i['href'] for i in soup.find_all('a',{'class':'product-img'}, href=True) if i['href'] != "#"]
        for i in range(0,len(titles)):
            TITLE = titles[i].text.replace('\n', '').replace('\t', '').strip()
            #TITLE = TITLE.replace("\t","")
            #TITLE = TITLE.replace("\n","")
            PRICE = prices[i].text
            IMAGE = img_url[i].get('data-src')
            LINK = item_link[i]
            BRAND = "Uniworth"
            item = {
                'title': TITLE,
                'price': PRICE,
                'img': IMAGE,
                'brand': BRAND,
                'link': LINK
            }
            items_list.append(item)
        
    except(ConnectionError, Exception):
        return False