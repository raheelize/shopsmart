import django_filters
from account.models import Item
class ItemFilter(django_filters.FilterSet):
    
    class Meta:
        model = Item
        fields = ('title','category','brand')