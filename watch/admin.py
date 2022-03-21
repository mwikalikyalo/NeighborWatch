from django.contrib import admin
from watch.models import Business, Category, Location, Neighborhood, Post

# Register your models here.
admin.site.register(Neighborhood)
admin.site.register(Location)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Business)