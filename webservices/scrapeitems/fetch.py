
from bs4 import BeautifulSoup,SoupStrainer
import requests 
import sys
from price_parser import parse_price
from  account.models import Item,Preferences
#from ..price_extractor import parse_price
#from home.models import Items
items_list = []
def set_up_query(query):
	query = query.replace(" ","+")
	query = query.lower()
	return query

"""Brand Scraping Methods"""

def outfitters(string):
	query = set_up_query(string)
	try:
		link = "https://outfitters.com.pk/search?type=product&q="+query
		req = requests.get(link)
		soup = BeautifulSoup(req.text, 'lxml')
		titles = soup.find_all('a',{'class':'product-title'})
		prices = soup.find_all('span',{'class':'money'})
		img_url = soup.find_all('a', {'class':'product-grid-image'})
		item_link = [i['href'] for i in soup.find_all('a',{'class':'product-title'}, href=True) if i['href'] != "#"]
		for i in range(0,len(titles)):
			TITLE = titles[i].text
			TITLE = TITLE.replace("\t","")
			TITLE = TITLE.replace("\n","")
			PRICE = parse_price(prices[i].text).amount_float
			IMAGE = img_url[i].find('img').get('src')
			IMAGE = IMAGE.replace("?v=1599216010","")
			LINK = "https://outfitters.com.pk"  + item_link[i]
			# if Item.objects.filter(item_url=LINK):
			# 	continue
			BRAND = "Outfitters"
			item = {
				'title': TITLE,
				'price': PRICE,
				'img': IMAGE,
				'brand': BRAND,
				'link': LINK
			}
			print(BRAND,query)
			CAT = Preferences.objects.get(title=string)  
			Item(title=item['title'],image_url=item['img'],item_url=item['link'],brand=item['brand'],price=item['price'],category=CAT).save()
		
	except(ConnectionError, Exception):
		return False
def eden_robe(string):
	query = set_up_query(string)
	try:
		link = "https://edenrobe.com/catalogsearch/result/?q="+query
		req = requests.get(link)
		soup = BeautifulSoup(req.text, 'lxml')
		#print(soup.text)
		titles = soup.find_all('a',{'class':'product-item-link'})
		prices = soup.find_all('span',{'class':'price'})
		#img = [i['href'] for i in soup.find_all('a',{'class':'MagicZoom'}, href=True) if i['href'] != "#"]
		img = soup.find_all('img',{'class':'img-responsive product-image-photo img-thumbnail'})
		#print(img)
		for i in range(0,len(titles)):
			print("IN LOPOOP")
			TITLE = titles[i].text
			PRICE = parse_price(prices[i].text).amount_float
			if PRICE is None:
					continue
			IMAGE = img[i].get('data-src')
			print(IMAGE)
			BRAND = "Eden Robe"
			
			LINK = titles[i].get('href')
			# if Item.objects.filter(item_url=LINK):
			# 	continue
			item = {
				'title': TITLE,
				'price': PRICE,
				'img': IMAGE,
				'brand': BRAND,
				'link': LINK
			}
			
			#print(BRAND,string)
			CAT = Preferences.objects.get(title=query)  
			Item(title=item['title'],image_url=item['img'],item_url=item['link'],brand=item['brand'],price=item['price'],category=CAT).save()
	except(ConnectionError, Exception):
		return False

def couger(string):
	#print("functions")
	query = set_up_query(string)
	try:
		link = "https://www.cougar.com.pk/search?q="+str(query)+"&type=product"
		req = requests.get(link)
		soup = BeautifulSoup(req.text, 'lxml')
		#print(soup)
		titles = soup.find_all('span',{'class':'prod-title'})
		prices = soup.find_all('div',{'class':'prod-price'})
		#print(prices)
		img_url = soup.find_all('img', {'class':'lazyload-fade'})
		#print(img_url)
		item_link = soup.find_all('div',{'class':'product-info-inner'})
		#print(item_link)
		for i in range(0,len(titles)):
			#print('in loop')
			TITLE = titles[i].text
			#PRICE = prices[i].text
			PRICE = parse_price(prices[i].text).amount_float
			
			IMAGE = img_url[i].get('data-src')
			
			#IMAGE = IMAGE.replace("?v=1599216010","")
			x = item_link[i].find('a').get('href')
			LINK = "https://www.cougar.com.pk/"  + x
			# if Item.objects.filter(item_url=LINK):
			# 	continue
			#print(LINK)
			BRAND = "Couger"
			item = {
				'title': TITLE,
				'price': PRICE,
				'img': IMAGE,
				'brand': BRAND,
				'link': LINK
			}
			#print(item)
			print(BRAND,query)
			CAT = Preferences.objects.get(title=string)  
			Item(title=item['title'],image_url=item['img'],item_url=item['link'],brand=item['brand'],price=item['price'],category=CAT).save()
		
	except(ConnectionError, Exception):
		return False


def sana_safinaz(string):
	#print("functions")
	query = set_up_query(string)
	try:
		link = "https://www.sanasafinaz.com/pk/catalogsearch/result/index/?q="+str(query)+"&product_list_limit=60"
		req = requests.get(link)
		soup = BeautifulSoup(req.text, 'lxml')
		#print(soup)
		titles = soup.find_all('a',{'class':'product-item-link'})
		#print(titles)
		prices = soup.find_all('span',{'class':'price'})
		#print(prices)
		img_url = soup.find_all('img', {'class':'product-image-photo'})
		
		#print(img_url)
		#item_link = soup.find_all('div',{'class':'product-info-inner'})
		#print(item_link)
		for i in range(0,len(titles)):
			print('in loop')
			TITLE = titles[i].text
			TITLE = TITLE.replace('\n','')
			TTILE = TITLE.replace('\t','')
			#PRICE = prices[i].text
			#print(PRICE)
			PRICE = parse_price(prices[i].text).amount_float
			
			IMAGE = img_url[i].get('src')
			#print(IMAGE)
			#IMAGE = IMAGE.replace("?v=1599216010","")
			LINK = titles[i].get('href')
			# if Item.objects.filter(item_url=LINK):
			# 	continue
			#print(LINK)
			#LINK = "https://www.cougar.com.pk/"  + x
			#print(LINK)
			BRAND = "Sana Safinaz"
			item = {
				'title': TITLE,
				'price': PRICE,
				'img': IMAGE,
				'brand': BRAND,
				'link': LINK
			}
			#print(item)
			print(BRAND,query)
			CAT = Preferences.objects.get(title=string)  
			Item(title=item['title'],image_url=item['img'],item_url=item['link'],brand=item['brand'],price=item['price'],category=CAT).save()
		
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
			PRICE = parse_price(prices[i].text).amount_float
			IMAGE = img_url[i].get('data-src')
			LINK = item_link[i]
			if Item.objects.filter(item_url=LINK):
				continue
			BRAND = "Uniworth"
			item = {
				'title': TITLE,
				'price': PRICE,
				'img': IMAGE,
				'brand': BRAND,
				'link': LINK
			}
			#items_list.append(item)
			# item = Item(title=TITLE,image_url=IMAGE,item_url=LINK,brand=BRAND,price=item['price'])
			# item.save()
		
	except(ConnectionError, Exception):
		return False

def jdot(string):
	query  = set_up_query(string)
	try:
		page = 1
		link = "https://www.junaidjamshed.com/catalogsearch/result/index/?p="+str(page)+"&product_list_limit=30&q="+query
		query=	query.replace("+"," ")
		req = requests.get(link)
		soup = BeautifulSoup(req.text, 'lxml')
		titles = soup.find_all('a',{'class':'product-item-link'})
		prices = soup.find_all('span',{'class':'price'})
		img_url = soup.find_all('img', {'class':'product-image-photo lazy'})
		X = (len(titles))
		for i in range(0,X):
		
			TITLE = titles[i].text
			TITLE = TITLE.replace("\t","")
			TITLE = TITLE.replace("\n","")
			PRICE = parse_price(prices[i].text).amount_float
			IMAGE = img_url[i].get('data-original')
			LINK = titles[i].get('href')
			# if Item.objects.filter(item_url=LINK):
			# 	continue
			BRAND = "Junaid Jamshed"
			item = {
				'title': TITLE,
				'price': PRICE,
				'img': IMAGE,
				'brand': BRAND,
				'link': LINK
			}
			print(item)
			CAT = Preferences.objects.get(title=string)  
			print(query)
			Item(title=item['title'],image_url=item['img'],item_url=item['link'],brand=item['brand'],price=item['price'],category=CAT).save()
		
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
			PRICE = parse_price(prices[i].text).amount_float
			IMAGE = img_url[i].get('src')
			#IMAGE = IMAGE.replace(".pagespeed.ic.py1u_bk3_f.webp","")
			LINK = item_link[i]
			# if Item.objects.filter(item_url=LINK):
			# 	continue
			BRAND = "Gul Ahmed"
			item = {
				'title': TITLE,
				'price': PRICE,
				'img': IMAGE,
				'brand': BRAND,
				'link': LINK
			}
			# query=	query.replace("+"," ")
			# Item(title=item['title'],image_url=item['img'],item_url=item['link'],brand=item['brand'],price=item['price'],category=query).save()
			
	except(ConnectionError, Exception):
		return False

def beechtree(string):
	print("functions")
	query = set_up_query(string)
	try:
		link = "https://www.beechtree.pk/pk/catalogsearch/result/?q="+str(query)+"#/page/1"
		req = requests.get(link)
		soup = BeautifulSoup(req.text, 'lxml')
		#print(soup)
		titles = soup.find_all('h2',{'class':'product-name'})
		#print(titles)
		prices = soup.find_all('span',{'class':'price'})
		#print(prices)
		img_url = soup.find_all('a', {'class':'product-image'})
		
		#print(img_url)
		#item_link = soup.find_all('div',{'class':'product-info-inner'})
		#print(item_link)
		for i in range(0,len(titles)):
			print('in loop')
			TITLE = titles[i].text
			TITLE = TITLE.replace('\n','')
			TTILE = TITLE.replace('\t','')
			#PRICE = prices[i].text
			#print(PRICE)
			PRICE = parse_price(prices[i].text).amount_float
			
			IMAGE = img_url[i].find('img').get('src')
			#print(IMAGE)
			#IMAGE = IMAGE.replace("?v=1599216010","")
			LINK = img_url[i].get('href')
			# if Item.objects.filter(item_url=LINK):
			# 	continue
			#print(LINK)
			#LINK = "https://www.cougar.com.pk/"  + x
			#print(LINK)
			BRAND = "Beechtree"
			item = {
				'title': TITLE,
				'price': PRICE,
				'img': IMAGE,
				'brand': BRAND,
				'link': LINK
			}
			#print(item)
			print(BRAND,query)
			CAT = Preferences.objects.get(title=string)  
			Item(title=item['title'],image_url=item['img'],item_url=item['link'],brand=item['brand'],price=item['price'],category=CAT).save()
		
	except(ConnectionError, Exception):
		return False
def kross_kulture(string):
	print("functions")
	query = set_up_query(string)
	try:
		link = "https://krosskulture.com/search/"+str(query)+"/?type=product"
		req = requests.get(link)
		soup = BeautifulSoup(req.text, 'lxml')
		#print(soup.prettify())
		
		titles = soup.find_all('div',{'class':'post-details'})
		#print(titles)
		prices = soup.find_all('ins')
		#print(prices)
		img_url = soup.find_all('div', {'class':'post-thumbnail'})
		
		#print(img_url)
		#item_link = soup.find_all('li',{'class':'snize-product'})
		#print(item_link)
		for i in range(0,len(titles)):
			print('in loop')
			TITLE = titles[i].find('h3').text
			TITLE = TITLE.replace('\n','')
			TTILE = TITLE.replace('\t','')
			p = prices[i].find('span').text
			#print(PRICE)
			PRICE = parse_price(p).amount_float
			
			IMAGE = img_url[i].find('img').get('src')
			#print(IMAGE)
			#IMAGE = IMAGE.replace("?v=1599216010","")
			LINK = titles[i].find('a').get('href')
			# if Item.objects.filter(item_url=LINK):
			# 	continue
			#print(LINK)
			#LINK = "https://www.cougar.com.pk/"  + x
			#print(LINK)
			BRAND = "Kross Kulture"
			item = {
				'title': TITLE,
				'price': PRICE,
				'img': IMAGE,
				'brand': BRAND,
				'link': LINK
			}
			#print(item)
			print(BRAND,query)
			CAT = Preferences.objects.get(title=string)  
			Item(title=item['title'],image_url=item['img'],item_url=item['link'],brand=item['brand'],price=item['price'],category=CAT).save()
		
	except(ConnectionError, Exception):
		return False
def breakout(string):
	query = set_up_query(string)
	try:
		page = 1
		##print(page)
		link = "https://breakout.com.pk/search?page="+str(page)+"&q="+query
		##print("query"+query)
		cat=query.replace("+"," ")
		##print(link)
		req = requests.get(link)
		soup = BeautifulSoup(req.text, 'html.parser')
		nextBtn = soup.find('a',{'class':'btn-next'})
		
		while nextBtn.text == "Next":
			#print(page)
			#print(nextBtn)
			link = "https://breakout.com.pk/search?page="+str(page)+"&q="+query
			##print("query"+query)
			cat=query.replace("+"," ")
			#print(link)
			req = requests.get(link)
			##print('request sussecfull')
			soup = BeautifulSoup(req.text, 'html.parser')
			##print(soup)
			titles = soup.find_all('h2',{'class':'pt-title prod-thumb-title-color'})
			prices = soup.find_all('div',{'class':'pt-price'})
			#rint(prices)
			img_url = soup.find_all('img',{'class':'lazyload'})
			##print(img_url)
			#item_link = soup.find_all('a',{'class':'product-title'}, href=True)
			L = (len(titles))
			nextBtn = soup.find('a',{'class':'btn-next'})
			for i in range(0,L):
				#print("In Loop")
				TITLE = titles[i].text
				TITLE = TITLE.upper()	
			
				IMAGE = img_url[i].get('data-src')  
			
				LINK = "https://breakout.com.pk" + titles[i].find('a').get('href')
				# if Item.objects.filter(item_url=LINK):
				# 	continue
			
				PRICE = parse_price(prices[i].text).amount_float
				if PRICE is None:
					continue
			
				BRAND = "Breakout"
				item = {
					'title': TITLE,
					'price': PRICE,
					'img': IMAGE,
					'brand': BRAND,
					'link': LINK
				}
				CAT = Preferences.objects.get(title=string)  
				Item(title=item['title'],image_url=item['img'],item_url=item['link'],brand=item['brand'],price=item['price'],category=CAT).save()
			page = page + 1
		
	except(ConnectionError, Exception):
		return False

def focus(string):
	query = set_up_query(string)
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
			# if Item.objects.filter(item_url=LINK):
			# 	continue
			PRICE = parse_price(prices[i].text).amount_float
			BRAND = "Focus"
			item = {
				'title': TITLE,
				'price': PRICE,
				'img': IMAGE,
				'brand': BRAND,
				'link': LINK
			}
			print(BRAND,query)
			CAT = Preferences.objects.get(title=string)  
			Item(title=item['title'],image_url=item['img'],item_url=item['link'],brand=item['brand'],price=item['price'],category=CAT).save()
	except(ConnectionError, Exception):
		return False

def diners(string):
	query = set_up_query(string)
	try:
		link = "https://diners.com.pk/search?page=&q="+query
		req = requests.get(link)
		soup = BeautifulSoup(req.text, 'lxml')
		titles = soup.find_all('a',{'class':'product-title'})
		prices = soup.find_all('div',{'class':'price-box'})
		img_url = soup.find_all('span',{'class':'images-two'})
		L = (len(titles))

		for i in range(0,L):
			TITLE = titles[i].span.text
		
			IMAGE = img_url[i].img.get('src')
	
			LINK = "https://diners.com.pk/" + titles[i].get('href')
			# if Item.objects.filter(item_url=LINK):
			# 	continue
		
			PRICE = parse_price(prices[i].text).amount_float
			if PRICE is None:
				pass
			BRAND = "Diners"
			item = {
				'title': TITLE,
				'price': PRICE,
				'img': IMAGE,
				'brand': BRAND,
				'link': LINK
			}
			print(item)
			print(BRAND,query)		
			CAT = Preferences.objects.get(title= string)  
			print(CAT)
			Item(title=item['title'],image_url=item['img'],item_url=item['link'],brand=item['brand'],price=item['price'],category=CAT).save()
	
	except(ConnectionError, Exception):
		return False


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
		##print(link)
		req = requests.get(link)
		soup = BeautifulSoup(req.text, 'html.parser')
		titles = soup.find_all('p',{'class':'mt-1 mb-1 overflow-hidden text-sm l-line-clamp-2 fs-theme-text-purple md:text-lg'})
		prices = soup.find_all('p',{'class':'font-bold md:text-xl'})
		img_url = soup.find_all('img',{'class':'absolute inset-0 object-contain w-full h-full rounded-lg lozad'})
		item_link = soup.find_all('a',{'class':'px-2 py-1 text-xs font-semibold text-gray-800 bg-white rounded-full md:text-base md:px-4 md:py-2 hover:shadow-xl'}, href=True)
		brand_name = soup.find_all('p',{'class':'text-xs leading-3 md:text-sm'})
		###print(titles)
		L = (len(titles))
		##print(L)
		for i in range(0,L):
			##print("In Loop")
			TITLE = titles[i].text
			TITLE = TITLE.replace("\t","")
			TITLE = TITLE.replace("\n","")
			TITLE = TITLE.upper()
			###print()
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
			###print(item)
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
		###print(titles)
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
			###print(item)
			#items_list.append(item)
			
	except(ConnectionError, Exception):
		return False
		
#https://fashionista.shoppingum.com/pakistani-dresses?page=1
#pakistani-dresses?page=
"""Calling Scrape Methods to Update DB"""
def update_products():
	Item.objects.all().delete()
	cats = Preferences.objects.values_list("title").distinct()
	for cat in cats:
		cat = cat[0] #cleaning data
		"""Calling Brands Methods to Scrape All Available Items by RealTime"""
		jdot(cat)
		outfitters(cat)
		eden_robe(cat)
		breakout(cat)
		focus(cat)
		diners(cat)
		sana_safinaz(cat)
		couger(cat)
		beechtree(cat)
		kross_kulture(cat)
		 
		











	

