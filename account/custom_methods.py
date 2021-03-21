from .models import *
from django.contrib import messages
import difflib

# adding items to user favorite block
def add_to_fav(request):
    req_id = request.POST.get('product_id')
    check = Favorite.objects.filter(item_id = req_id)
    if len(check)>=1:
        messages.add_message(request, messages.ERROR,  'Item Already exists in Favorites') 
    else:
        #print(req_id)
        fav_item = Item.objects.filter(item_id = req_id)[0]
        Favorite(owner=request.user,
                        item_id = fav_item.item_id,
                        title=fav_item.title,
                        image_url=fav_item.image_url,
                        item_url=fav_item.item_url,
                        brand=fav_item.brand,
                        price=fav_item.price,
                        category=fav_item.category).save()
        messages.success(request,   'Added to Favorites') 



# retrieving users prefered categories for personalization
def get_prefered_items(user):
    prefered = UserPreferences.objects.filter(user=user).distinct()
    items_list = []
    for cat in prefered:
        items = Item.objects.filter(category=cat.category).distinct()
        for x in items:
            items_list.append(x)
    return items_list



# matching queries with model items
def search_matches(searchs,item):
    string  = str(item.title.lower()) + str(item.brand.lower()) + str(item.category.title.lower())
    searchs = searchs.lower()
    # if  string.__contains__(searchs):
    #     return True
    sequence = difflib.SequenceMatcher(isjunk=None,a=searchs,b=string)
    difference = sequence.ratio()*100
    # if difference >50.0:
    #     return True
    # else:
    #     return False
    # for search in searchs:
    #     if search in item.title.lower() or search in item.brand.lower() or search in item.category.title.lower():
    #         return True
    #     else:
    #         return False
    if searchs in item.title.lower() or searchs in item.brand.lower() or searchs in item.category.title.lower():
        return True
    else:
        return False
   