from django.contrib import admin
from news.models import News, Comment_news

admin.site.register(News)
admin.site.register(Comment_news)
