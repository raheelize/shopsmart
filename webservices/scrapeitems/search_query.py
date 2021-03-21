
from bs4 import BeautifulSoup,SoupStrainer
from price_parser import Price
import requests 
import sys
from  account.models import QuerySet
#from home.models import Items
items_list = []
def outfitters(query):
	try:
		link = "https://outfitters.com.pk/search?type=product&q="+query
		req = requests.get(link)
		soup = BeautifulSoup(req.text, 'lxml')
		titles = soup.find_all('a',{'class':'product-title'})
		prices = soup.find_all('span',{'class':'money'})
		img_url = soup.find_all('img', {'class':'images-one lazyautosizes lazyloaded'})
		#//*[@id="category-products-grid"]/ol/li[1]/div/div[1]/div[1]/a/span[1]/span/span/img
		item_link = [i['href'] for i in soup.find_all('a',{'class':'product-title'}, href=True) if i['href'] != "#"]
		for i in range(0,len(titles)):
			TITLE = titles[i].text
			TITLE = TITLE.replace("\t","")
			TITLE = TITLE.replace("\n","")
			PRICE = prices[i].text
			IMAGE = img_url[i].get('src')
			IMAGE = IMAGE.replace("?v=1599216010","")
			LINK = item_link[i]
			BRAND = "Outfitters"
			item = {
				'title': TITLE,
				'price': PRICE,
				'img': IMAGE,
				'brand': BRAND,
				'link': LINK
			}
			print(item)
			#items_list.append(item)
			query=	query.replace("+"," ")
			QuerySet(title=item['title'],image_url=item['img'],item_url=item['link'],brand=item['brand'],price=item['price'],category=query).save()
			# item = QuerySet(title=TITLE,image_url=IMAGE,item_url=LINK,brand=BRAND,price=item['price'])
			# item.save()
		
	except(ConnectionError, Exception):
		return False
def eden_robe(query):
	try:
		link = "https://edenrobe.com/catalogsearch/result/?q="+query
		req = requests.get(link)
		soup = BeautifulSoup(req.text, 'lxml')
		#print(soup.text)

		titles = soup.find_all('a',{'class':'product-item-link'})
		prices = soup.find_all('span',{'class':'price'})
		img = [i['href'] for i in soup.find_all('a',{'class':'MagicZoom'}, href=True) if i['href'] != "#"]
		for i in range(0,len(titles)):
			TITLE = titles[i].text
			TITLE = TITLE.replace("\t","")
			TITLE = TITLE.replace("\n","")
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
			#items_list.append(item)
			query=	query.replace("+"," ")
			QuerySet(title=item['title'],image_url=item['img'],item_url=item['link'],brand=item['brand'],price=item['price'],category=query).save()
		#print(titles[i].text)
		#print(prices[i].text)
		#print(img[i])
	except(ConnectionError, Exception):
		return False



def uniworth(query):
	try:
		link = "https://www.uniworthshop.com/search?keywords="+query
		req = requests.get(link)
		soup = BeautifulSoup(req.text, 'lxml')
		titles = soup.find_all('div',{'class':'product-name'})
		prices = soup.find_all('span',{'class':'price'})
		img_url = soup.find_all('img', {'class':'primary'})
		item_link = [i['href'] for i in soup.find_all('a',{'class':'product-img'}, href=True) if i['href'] != "#"]
		for i in range(0,len(titles)):
			TITLE = titles[i].text
			TITLE = TITLE.replace("\t","")
			TITLE = TITLE.replace("\n","")
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
			#items_list.append(item)
			# item = QuerySet(title=TITLE,image_url=IMAGE,item_url=LINK,brand=BRAND,price=item['price'])
			# item.save()
		
	except(ConnectionError, Exception):
		return False

def jdot(query):
	try:
		link = "https://www.junaidjamshed.com/catalogsearch/result/?q="+query
		#print(link)
		req = requests.get(link)
		soup = BeautifulSoup(req.text, 'lxml')
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
			LINK = titles[i].get('href')
			BRAND = "Junaid Jamshed"
			#print(titles[i].text)
			item = {
				'title': TITLE,
				'price': PRICE,
				'img': IMAGE,
				'brand': BRAND,
				'link': LINK
			}
			#print(item)
			#items_list.append(item)
			query=	query.replace("+"," ")
			QuerySet(title=item['title'],image_url=item['img'],item_url=item['link'],brand=item['brand'],price=item['price'],category=query).save()
			# item.save()
		
	except(ConnectionError, Exception):
		return False

def gulahmed(query):
	try:
		link = "https://www.gulahmedshop.com/catalogsearch/result/?q="+query
		req = requests.get(link)
		soup = BeautifulSoup(req.text, 'lxml')
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
			#print(item)
			#items_list.append(item)
			query=	query.replace("+"," ")
			QuerySet(title=item['title'],image_url=item['img'],item_url=item['link'],brand=item['brand'],price=item['price'],category=query).save()
		
	except(ConnectionError, Exception):
		return False



def breakout(query):
	try:
		link = "https://breakout.com.pk/search?type=product&q="+query
		#print(link)
		req = requests.get(link)
		print('equest sussecfull')
		soup = BeautifulSoup(req.text, 'html.parser')
		print(soup)
		titles = soup.find_all('h2',{'class':'pt-title prod-thumb-title-color'})
		prices = soup.find_all('div',{'class':'pt-price'})
		img_url = soup.find_all('img',{'class':'lazyload'})
		print(img_url)
		#item_link = soup.find_all('a',{'class':'product-title'}, href=True)
		L = (len(titles))
		for i in range(0,L):
			#print("In Loop")
			TITLE = titles[i].text
			TITLE = TITLE.upper()	
			IMAGE = img_url[i].get('data-src')           
			LINK = "https://breakout.com.pk" + titles[i].find('a').get('href')
			PRICE = prices[i].text
			BRAND = "Breakout"
			item = {
				'title': TITLE,
				'price': PRICE,
				'img': IMAGE,
				'brand': BRAND,
				'link': LINK
			}
			print(item)
			#items_list.append(item)
			query=	query.replace("+"," ")
			QuerySet(title=item['title'],image_url=item['img'],item_url=item['link'],brand=item['brand'],price=item['price'],category=query).save()
			
	except(ConnectionError, Exception):
		return False

def focus(query):
	try:
		
		link = "https://focusclothing.pk/search?q=" + query
		req = requests.get(link)
		soup = BeautifulSoup(req.text, 'html.parser')
		titles = soup.find_all('div',{'class':'prod-title'})
		prices = soup.find_all('div',{'class':'onsale'})
		img_url = soup.find_all('noscript')
		item_link = soup.find_all('div',{'class':'product-info'})
		L = (len(titles))
		for i in range(0,L):
			TITLE = titles[i].text
			IMAGE = img_url[i].img.get('src')
			LINK = "https://focusclothing.pk" + item_link[i].a.get('href')
			PRICE = prices[i].text
			BRAND = "Focus"
			item = {
				'title': TITLE,
				'price': PRICE,
				'img': IMAGE,
				'brand': BRAND,
				'link': LINK
			}
			#items_list.append(item)
			query=	query.replace("+"," ")
			QuerySet(title=item['title'],image_url=item['img'],item_url=item['link'],brand=item['brand'],price=item['price'],category=query).save()
			
	except(ConnectionError, Exception):
		return False

def diners(query):
	try:
		link = "https://diners.com.pk/search?type=product&q="+query
	 
		req = requests.get(link)
		soup = BeautifulSoup(req.text, 'lxml')
		titles = soup.find_all('a',{'class':'product-title'})
		prices = soup.find_all('div',{'class':'price-box'})
		img_url = soup.find_all('span',{'class':'images-two'})
		#item_link = soup.find_all('div',{'class':'product-info'})
		L = (len(titles))
	 
		for i in range(0,L):
	   
			TITLE = titles[i].span.text
		   
			IMAGE = img_url[i].img.get('src')
	   
			LINK = "https://diners.com.pk/" + titles[i].get('href')
		 
			PRICE = prices[i].div.span.span.text
	   
			BRAND = "Diners"
			item = {
				'title': TITLE,
				'price': PRICE,
				'img': IMAGE,
				'brand': BRAND,
				'link': LINK
			}
			#print(item)
			#items_list.append(item)
			query=	query.replace("+"," ")
			query=	query.replace("+"," ")
			QuerySet(title=item['title'],image_url=item['img'],item_url=item['link'],brand=item['brand'],price=item['price'],category=query).save()
			
	except(ConnectionError, Exception):
		return False

'''
def fashionista(query):

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

def search(X):
	try:
		link = "https://fashionista.shoppingum.com/search?search="+X
		print(link)
		req = requests.get(link)
		soup = BeautifulSoup(req.text, 'html.parser')
		titles = soup.find_all('p',{'class':'mt-1 mb-1 overflow-hidden text-sm l-line-clamp-2 fs-theme-text-purple md:text-lg'})
		prices = soup.find_all('p',{'class':'font-bold md:text-xl'})
		img_url = soup.find_all('img',{'class':'absolute inset-0 object-contain w-full h-full rounded-lg lozad'})
		item_link = soup.find_all('a',{'class':'px-2 py-1 text-xs font-semibold text-gray-800 bg-white rounded-full md:text-base md:px-4 md:py-2 hover:shadow-xl'}, href=True)
		brand_name = soup.find_all('p',{'class':'text-xs leading-3 md:text-sm'})
		#print(titles)
		L = (len(titles))
		print(L)
		for i in range(0,L):
			print("In Loop")
			TITLE = titles[i].text
			TITLE = TITLE.replace("\t","")
			TITLE = TITLE.replace("\n","")
			TITLE = TITLE.upper()
			#print()
			#for x in titles:
			
			PRICE = prices[i].text
			PRICE = PRICE.replace("\t","")
			PRICE = PRICE.replace("\n","")
			IMAGE = "https://fashionista.shoppingum.com" + img_url[i].get('data-src')
			LINK = "https://fashionista.shoppingum.com" + item_link[i]['href']
			LINK = LINK.replace("similar","redirect")
			BRAND = brand_name[i].text
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
def getall():
	try:
		link = "https://fashionista.shoppingum.com/pakistani-dresses"
		req = requests.get(link)
		soup = BeautifulSoup(req.text, 'html.parser',on_duplicate_attribute='ignore')
		titles = soup.find_all('p',{'class':'mt-1 mb-1 overflow-hidden text-sm l-line-clamp-2 fs-theme-text-purple md:text-lg'})
		prices = soup.find_all('span',{'class':'fs-theme-text-pink-01'})
		img_url = soup.find_all('img',{'class':'absolute inset-0 object-contain w-full h-full rounded-lg lozad'})
		item_link = soup.find_all('a',{'class':'px-2 py-1 text-xs font-semibold text-gray-800 bg-white rounded-full md:text-base md:px-4 md:py-2 hover:shadow-xl'}, href=True)
		brand_name = soup.find_all('p',{'class':'text-xs leading-3 md:text-sm'})
		#print(titles)
		for i in range(0,len(titles)):
		#for x in titles:
			TITLE = titles[i].text
			PRICE = prices[i].text
			IMAGE = "https://fashionista.shoppingum.com" + img_url[i].get('data-src')
			LINK = "https://fashionista.shoppingum.com" + item_link[i]['href']
			LINK = LINK.replace("similar","redirect")
			BRAND = brand_name[i].text
			item = {
				'title': TITLE,
				'price': PRICE,
				'img': IMAGE,
				'brand': BRAND,
				'link': LINK
			}
			#print(item)
			#items_list.append(item)
			
	except(ConnectionError, Exception):
		return False
		'''
#https://fashionista.shoppingum.com/pakistani-dresses?page=1
#pakistani-dresses?page=

def get_search():
	cats = Preferences.objects.all()
	for cat in cats:
		query = cat.title
		query = query.replace(" ","+")

		diners(query)
		jdot(query)
		outfitters(query)
		#uniworth(query)
		#gulahmed(query)
		eden_robe(query)
		breakout(query)
		focus(query)
		print("Items Scraped!")



#from .libs import gulahmed
def search_query(query):
	QuerySet.objects.all().delete()
	diners(query)
	jdot(query)
	outfitters(query)
	#uniworth(query)
	#gulahmed(query)
	eden_robe(query)
	breakout(query)
	focus(query)
		
		
	

def get_all_products():
	search_query("all+products")   
	#print(items_list)


#get_all_products()





