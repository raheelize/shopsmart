from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
import uuid
from django.conf import settings

# Create your models here.
from shopSmart.managers import CustomUserManager


class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    message = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name


class Preferences(models.Model):
    PREF_TYPES = (
        ('summer_wear', 'Summer Wear'),
        ('winter_wear', 'Winter Wear'),
        ('foot_wear', 'Foot Wear'),
        ('ethnic_wear', 'Ethnic Wear'),
        ('western_wear', 'Western Wear'),
        ('accessories', 'Accessories'),
        ('fragrances', 'Fragrances'),
    )
    title = models.CharField(max_length=30, unique=True)
    pref_type = models.CharField("Type",max_length=30,choices=PREF_TYPES, default='top_wear')
    class Meta:
        verbose_name = 'Preferences'
        verbose_name_plural = 'Preferences'
        ordering = ['title']
    def __str__(self):
        return self.title + " - "+self.pref_type

class Item(models.Model):
    item_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    title = models.CharField(max_length=100)
    image_url = models.CharField(max_length=200)
    item_url = models.CharField(max_length=200)
    brand = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Preferences, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['price']
    def __str__(self):
        return self.title
    @staticmethod
    def get_all():
        return Item.objects.all()
    @staticmethod
    def get_items_by_brand(brand):
        if brand:
            return Item.objects.filter(brand=brand)
        else:
            return Item.objects.all()
class QuerySet(models.Model):
    item_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    title = models.CharField(max_length=100)
    image_url = models.CharField(max_length=200)
    item_url = models.CharField(max_length=200)
    brand = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    def __str__(self):
        return self.title


# # Create your models here.
class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, name, contact, password=None):
        if not email:
            raise ValueError('User Must Have an Email')
        if not username:
            raise ValueError('User Must Have an Username')
        if not name:
            raise ValueError('User Must Have a Name')
        if not contact:
            raise ValueError('User Must Provide a Contact Number')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            name=name,
            contact=contact,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, name, contact, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            name=name,
            contact=contact,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser, PermissionsMixin):
    user_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    contact = models.CharField(max_length=11, unique=True)
    name = models.CharField(max_length=50)
    #notifications
    email_noification = models.BooleanField(default=False)
    sms_noification = models.BooleanField(default=False)

    # required for customizing user
    date_joined = models.DateField(verbose_name="date_joined", auto_now_add=True)
    last_login = models.DateField(verbose_name="last_login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'name', 'contact']

    #objects = MyAccountManager()
    objects = CustomUserManager()
    def __str__(self):
        return self.name

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
    #setter functions
    def set_name(self, name):
        self.name = name
        self.save()
    def set_email(self,email):
        self.email = email
        self.save()
    def set_contact(self,contact):
        self.contact = contact
        self.save()
    def set_email_notification(self):
        self.email_noification = True
        self.save()
    def set_sms_notification(self):
        self.sms_noification = True
        self.save()
    def del_email_notification(self):
        self.email_noification = False
        self.save()
    def del_sms_notification(self):
        self.sms_noification = False
        self.save()










User = get_user_model()
class Profile(models.Model):
    user = models.OneToOneField(settings.USER_AUTH_MODEL, on_delete=models.CASCADE)
    products = models.ManyToManyField(Item,blank=True)
    def __str__(self):
        return self.user.name

def post_save_profile_create(sender,instance,created,*args, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)

post_save.connect(post_save_profile_create,sender = settings.AUTH_USER_MODEL)
class Favorite(models.Model):
    owner = models.ForeignKey(Account, on_delete=models.CASCADE)
    item_id = models.CharField(max_length=200)
    title = models.CharField(max_length=100)
    image_url = models.CharField(max_length=200)
    item_url = models.CharField(max_length=200)
    brand = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)


    def __str__(self):
        return self.owner.name + " - " + self.title
# class UserFavorite(models.Model):
#     owner = models.ForeignKey(Account, on_delete=models.CASCADE) 
#     item_id = models.CharField(max_length=200)
#     title = models.CharField(max_length=100)
#     image_url = models.CharField(max_length=200)
#     item_url = models.CharField(max_length=200)
#     brand = models.CharField(max_length=100)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     category = models.CharField(max_length=100)
#     def __str__(self):
#         return self.owner +" - "+ self.title
class UserPreferences(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)  
    category = models.ForeignKey(Preferences,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.name + "-" + self.category.title
    
    def add_category(self,user,categoy):
        UserPreferences(user,category).save()
    def get_prefered_items(user):
        prefered = UserPreferences.objects.filter(user=user).distinct()
        items_list = []
        for cat in prefered:
            items = Item.objects.filter(category=cat.category.title).distinct()
            items_list.append(items)
        return items_list
class Sale(models.Model):
    catalog = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    img_url = models.CharField(max_length=200)
    sale_url = models.CharField(max_length=200)
    def __str__(self):
        return self.catalog
    