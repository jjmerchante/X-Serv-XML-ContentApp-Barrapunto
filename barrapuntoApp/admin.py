from django.contrib import admin

# Register your models here.
from models import Page, News

admin.site.register(Page)
admin.site.register(News)
