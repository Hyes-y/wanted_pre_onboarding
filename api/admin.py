from django.contrib import admin
from .models import Company, Post, User, Apply

admin.site.register(Company)
admin.site.register(Post)
admin.site.register(User)
admin.site.register(Apply)

