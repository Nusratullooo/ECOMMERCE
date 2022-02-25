from django.contrib import messages
from django.http import HttpResponseRedirect

from news.forms import Comment_news_Form
from news.models import News, Comment_news
from django.core.paginator import (Paginator, PageNotAnInteger, EmptyPage)
from django.shortcuts import render

from product.models import Category


def news(request):
    category = Category.objects.all()
    news = News.objects.all()
    paginator = Paginator(news, 1)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)
    content = {
        'news': news,
        'category': category
    }
    return render(request, 'news.html', content)


def news_detail(request, id):
    category = Category.objects.all()
    news_detail = News.objects.get(pk=id)
    comment_news = Comment_news.objects.filter(news_id=id)
    comment_news_all = comment_news.count()
    context = {
        'category': category,
        'news_detail': news_detail,
        'comment_news': comment_news,
        'comment_news_all': comment_news_all,
    }
    return render(request, 'news_detail.html', context)


def comment_news(request, id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = Comment_news_Form(request.POST)
        if form.is_valid():
            data = Comment_news()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.comment = form.cleaned_data['comment']
            data.ip = request.META.get('REMOTE_ADDR')
            data.news_id = id
            data.save()
            messages.success(request, "Your message is successfully saved !")
            return HttpResponseRedirect(url)
    return HttpResponseRedirect(url)
