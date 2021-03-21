from django.contrib import admin
from account.models import *
from django.contrib.auth.models import User,Group
from django.contrib.auth.admin import UserAdmin
admin.site.unregister(Group)
admin.site.register(Contact)
admin.site.register(QuerySet)
admin.site.register(Preferences)
admin.site.register(Favorite)
#admin.site.register(UserFavorite)
admin.site.register(UserPreferences)

#from home.models import Account
# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    list_display = ('title','brand','price','datetime')
    search_fields = ('title','brand')
    list_filter = ('brand')
    #required
    filter_horizontal = ()
    list_filter = ()
    fieldsets  = ()

class AccountAdmin(UserAdmin):
    readonly_fields = ('date_joined','last_login','username')
    list_display = ('name','username','email','date_joined','last_login','is_admin','is_staff',)
    search_fields = ('name','email','username')
    readonly_fields = ('username','date_joined','last_login')

    #required
    filter_horizontal = ()
    list_filter = ()
    fieldsets  = ()

admin.site.register(Account,AccountAdmin)
admin.site.register(Item,ItemAdmin)