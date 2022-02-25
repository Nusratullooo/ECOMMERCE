from django.contrib.auth.models import User
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from django.http import HttpResponseRedirect
from django.utils import translation

from news.models import News
from order.models import ShopCart
from product.models import Category, Product, Images, Comment
from django.shortcuts import render, redirect
from home.models import ContactMessage, FAQ, NewsLetter, Information
from home.forms import ContactForm, NewsLetterForm
from django.contrib import messages

from user.models import Client


def home(request):
    category = Category.objects.all()
    product = Product.objects.all().order_by('?')
    news = News.objects.all()
    information = Information.objects.all()
    content = {
        'category': category,
        'product': product,
        'news': news,
        'information': information,
    }
    return render(request, 'index.html', content)


def contact(request):
    category = Category.objects.all()
    information = Information.objects.all()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.phone = form.cleaned_data['phone']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Message is successfully saved !")
            return redirect('home')
    form = ContactForm
    content = {
        'form': form,
        'category': category,
        'information': information,
    }
    return render(request, 'contact.html', content)


def faq(request):
    faq = FAQ.objects.all()
    category = Category.objects.all()
    content = {
        'faq': faq,
        'category': category,
    }
    return render(request, 'faq.html', content)


def about(request):
    category = Category.objects.all()
    content = {
        'category': category,
    }
    return render(request, 'about.html', content)


def category(request, id, slug):
    category = Category.objects.all()
    # client = Client.objects.get(user=request.user)
    # shopcart = ShopCart.objects.filter(user=client)
    # shopcart_count = shopcart.count()
    # total = 0
    # for rs in shopcart:
    #     total += rs.product.sell_price * rs.quantity
    categories = Category.objects.filter(id=id)
    products = Product.objects.filter(category_id=id)
    product_latest = Product.objects.filter(status='True').order_by('-id')[:8]
    paginator = Paginator(products, 1)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    context = {
        'category': category,
        'categories': categories,
        'products': products,
        # 'client': client,
        'product_latest': product_latest,
        # 'shopcart': shopcart,
        # 'shopcart_count': shopcart_count,
        # 'total': total,
    }
    return render(request, 'category.html', context)


def product(request, id, slug):
    product = Product.objects.get(pk=id)
    product_all = Product.objects.all()
    # client = Client.objects.get(user=request.user)
    # shopcart = ShopCart.objects.filter(user=client)
    # shopcart_count = shopcart.count()
    category = Category.objects.all().order_by('id')
    # client = Client.objects.get(user=request.user)
    comments = Comment.objects.filter(product_id=id)
    images = Images.objects.filter(product_id=id)
    # total = 0
    # for rs in shopcart:
    #     total += rs.product.sell_price * rs.quantity
    context = {
        'product': product,
        'product_all': product_all,
        'category': category,
        'images': images,
        # 'client': client,
        'comments': comments,
        # 'shopcart': shopcart,
        # 'shopcart_count': shopcart_count,
        # 'total': total,
    }
    return render(request, 'product.html', context)


def search(request):
    # client = Client.objects.get(user=request.user)
    # shopcart = ShopCart.objects.filter(user=client)
    # shopcart_count = shopcart.count()
    # total = 0
    # for rs in shopcart:
    #     total += rs.product.sell_price * rs.quantity
    if request.method == 'POST':
        searched = request.POST['searched'].upper()
        product = Product.objects.filter(title__contains=searched)
        # category = Category.objects.filter(status='True').order_by('-id')
    context = {
        # 'category': category,
        'searched': searched,
        'product': product,
        # 'client': client,
        # 'shopcart': shopcart,
        # 'shopcart_count': shopcart_count,
        # 'total': total,
    }
    return render(request, 'search.html', context)


def newsLetter(request):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            data = NewsLetter()
            data.email = form.cleaned_data['email']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Message is successfully saved !")
            return HttpResponseRedirect(url)
    return HttpResponseRedirect(url)


def selectlanguage(request):
    if request.method == 'POST':
        cur_language = translation.get_language()
        lasturl = request.META.get('HTTP_REFERER')
        lang = request.POST['language']
        translation.activate(lang)
        request.session['translation.LANGUAGE_SESSION_KEY'] = lang
        return HttpResponseRedirect("/" + lang)
