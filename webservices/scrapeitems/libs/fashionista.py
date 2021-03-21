from bs4 import BeautifulSoup
import requests

def search(query):

    try:
        link = "https://fashionista.shoppingum.com/search?search="+query
        req = requests.get(link)
        soup = BeautifulSoup(req.text, 'html.parser')
        titles = soup.find_all('p',{'class':'mt-1 mb-1 overflow-hidden text-sm l-line-clamp-2 fs-theme-text-purple md:text-lg'})
        
        prices = soup.find_all('span',{'class':'fs-theme-text-pink-01'})
        img_url = soup.find_all('img',{'class':'absolute inset-0 object-contain w-full h-full rounded-lg lozad'})
        item_link = soup.find_all('a',{'class':'px-2 py-1 text-xs font-semibold text-gray-800 bg-white rounded-full md:text-base md:px-4 md:py-2 hover:shadow-xl'}, href=True)
        brand_name = soup.find_all('p',{'class':'text-xs leading-3 md:text-sm'})
        
        for i in range(0,len(titles)):
            TITLE = titles[i].text
            PRICE = prices[i].text
            IMAGE = "https://fashionista.shoppingum.com" + img_url[i].get('data-src')
            BRAND = brand_name[i].text
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