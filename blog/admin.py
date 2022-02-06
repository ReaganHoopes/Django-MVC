from django.contrib import admin

# Register your models here.
from blog.models import Blog
from blog.models import Comments

admin.site.register(Blog)
admin.site.register(Comments)

