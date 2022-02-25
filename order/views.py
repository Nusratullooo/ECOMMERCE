from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from user.models import Client
from order.forms import ShopCartForm, OrderForm
from order.models import ShopCart, Order, OrderProduct
from product.models import Product, Category
from django.utils.crypto import get_random_string


@login_required(login_url='login_form')
def addtoshopcart(request, pk):
    url = request.META.get('HTTP_REFERER')
    product = Product.objects.get(id=pk)
    user = Client.objects.get(user=request.user)
    data, _ = ShopCart.objects.get_or_create(user=user, product=product)
    if request.method == "POST":
        form = ShopCartForm(request.POST)
        if form.is_valid():
            data.quantity += int(form.cleaned_data.get('quantity'))
            data.color += form.cleaned_data.get('color')
            data.size += form.cleaned_data.get('size')
            data.save()
            print('error_1_data')
            messages.success(request, 'Product succeccfully added to shopcart!')
            return redirect('shopcart')
    return redirect('shopcart')


def shopcart(request):
    category = Category.objects.all()
    current_user = request.user
    user = Client.objects.get(user=request.user)
    shopcart = ShopCart.objects.filter(user=user)
    shopcart_count = shopcart.count()
    total = 0
    total_qty = 0
    for rs in shopcart:
        total_qty += rs.quantity
        total += rs.product.sell_price * rs.quantity
    context = {
        'shopcart_count': shopcart_count,
        'user': user,
        'shopcart': shopcart,
        'total': total,
        'total_qty': total_qty,
        'current_user': current_user,
        'category': category,
    }
    return render(request, 'shopcart.html', context)


@login_required(login_url='login_form')
def deletefromcart(request, id):
    ShopCart.objects.filter(id=id).delete()
    messages.success(request, "Your item deleted from Shop Cart!")
    return redirect('shopcart')


@login_required(login_url='login_form')
def deleteallfromcart(request):
    ShopCart.objects.all().delete()
    messages.success(request, "Your item deleted from Shop Cart!")
    return redirect('shopcart')


def orderproduct(request):
    category = Category.objects.all()
    client = Client.objects.get(user=request.user)
    shopcart_ = ShopCart.objects.filter(user=client)
    order = OrderProduct.objects.filter(user=request.user)
    shopcart_count = shopcart_.count()
    current_user = request.user
    total_quantity = 0
    total = 0
    for rs in shopcart_:
        total += rs.product.sell_price * rs.quantity
        total_quantity += rs.quantity

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            data = Order()
            data.first_name = form.cleaned_data.get('first_name', None)
            data.last_name = form.cleaned_data.get('last_name', None)
            data.email = form.cleaned_data.get('email', None)
            data.phone = form.cleaned_data.get('phone', None)
            data.address = form.cleaned_data.get('address', None)
            data.zip_code = form.cleaned_data.get('zip_code', None)

            data.country = form.cleaned_data.get('country', None)
            data.city = form.cleaned_data.get('city', None)

            data.feedback = form.cleaned_data.get('feedback', None)

            data.user_id = request.user.id
            data.total = total
            data.total_quantity = total_quantity
            data.ip = request.META.get('REMOTE_ADDR')
            ordercode = get_random_string(10).upper()  # random code
            data.code = ordercode
            data.save()

            client = Client.objects.get(user=request.user)
            shopcart_ = ShopCart.objects.filter(user=client)
            for rs in shopcart_:
                detail = OrderProduct()
                detail.order_id = data.id
                detail.product_id = rs.product_id
                detail.user_id = current_user.id
                detail.quantity = rs.quantity
                detail.price = rs.product.sell_price
                detail.amount = rs.amount
                detail.size = rs.size
                detail.color = rs.color
                detail.save()
                product = Product.objects.get(id=rs.product_id)
                product.save()

            ShopCart.objects.filter(user=client).delete()
            request.session['cart_items'] = 0
            messages.success(request, "Your Order Has Been Completed! Thank you!")
            return render(request, 'ordercomplete.html', {
                'ordercode': ordercode,
                'order': order,
                'shopcart_count': shopcart_count,
                'category': category,
            })
        else:
            messages.warning(request, form.errors)
            return redirect('orderproduct')

    form = OrderForm
    client = Client.objects.get(user=request.user)
    shopcart_ = ShopCart.objects.filter(user_id=client)
    shopcart_count = shopcart_.count()
    context = {
        'shopcart': shopcart_,
        'total': total,
        'client': client,
        'form': form,
        'shopcart_count': shopcart_count,
        'category': category,
    }
    return render(request, 'checkout.html', context)
