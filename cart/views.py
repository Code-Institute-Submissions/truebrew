from django.shortcuts import render, redirect
from products.models import Product


# gets products to populate navbar dropdown in all views
products = Product.objects.all()


# Create your views here.
def view_cart(request):
    return render(request, 'cart.html', {'products': products})


def add_to_cart(request, id):
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if id in cart:
        cart[id] = int(cart[id]) + quantity
    else:
        cart[id] = cart.get(id, quantity)

    request.session['cart'] = cart
    return redirect('cart')


def adjust_quantity(request, id):
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[str(id)] = quantity
    else:
        cart.pop(str(id))

    request.session['cart'] = cart
    return redirect('cart')


def delete_subscription(request, id):
    cart = request.session.get('cart', {})

    cart.pop(str(id))

    request.session['cart'] = cart
    return redirect('cart')
