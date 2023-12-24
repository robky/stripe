from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

import stripe
from config import settings
from orders.models import Order

success_url = settings.DOMAIN_URL + 'success/'
cancelled_url = settings.DOMAIN_URL + 'cancelled/'
stripe.api_key = settings.STRIPE_API_KEY


def create_checkout_session(request, order_id):
    if request.method != 'GET':
        return JsonResponse({'error': 'Not supported method'})

    order = get_object_or_404(Order, id=order_id)
    items = order.items.prefetch_related('item')
    line_items = []
    for i in items:
        line_items.append(
            {
                'price_data': {
                    'currency': 'usd',
                    'unit_amount': i.item.price,
                    'product_data': {
                        'name': i.item.name,
                        'description': i.item.description,
                    },
                },
                'quantity': i.quantity,
            }
        )

    try:
        checkout_session = stripe.checkout.Session.create(
            success_url=success_url,
            cancel_url=cancelled_url,
            mode='payment',
            line_items=line_items,
        )
        return JsonResponse({'sessionId': checkout_session['id']})
    except Exception as e:
        return JsonResponse({'error': str(e)})


def to_checkout(request, order_id):
    template = 'checkout.html'
    order = get_object_or_404(Order, id=order_id)
    items = order.items.prefetch_related('item')
    context = {
        'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY,
        'order_id': order_id,
        'items': items,
    }
    return render(request, template, context)


def index(request):
    template = 'index.html'
    orders = Order.objects.all()
    context = {'orders': orders}
    return render(request, template, context)
