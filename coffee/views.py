from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Coffee
from django.shortcuts import render, redirect

def home(request):
    coffee = Coffee.objects.all()
    return render(request, 'home.html', {'coffee': coffee})


def cart(request):
    cart_items = request.session.get('cart', [])
    coffee_ids = [item['id'] for item in cart_items]
    coffees = Coffee.objects.filter(id__in=coffee_ids)

    # Gán số lượng cho từng sản phẩm trong giỏ hàng
    for coffee in coffees:
        for item in cart_items:
            if item['id'] == coffee.id:
                coffee.quantity = item['quantity']

    context = {
        'coffees': coffees,
    }
    return render(request, 'cart.html', context)

def add_to_cart(request, coffee_id):
    cart = request.session.get('cart', [])
    for item in cart:
        if item['id'] == coffee_id:
            item['quantity'] += 1
            break
    else:
        cart.append({'id': coffee_id, 'quantity': 1})

    request.session['cart'] = cart
    return redirect('cart')