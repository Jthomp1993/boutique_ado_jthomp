from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment!")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51IX25PDfJZdrnwwz26s11nOBdkCmJAPc3LoENr1PNttOTxA0wJD6fjpYNXDbUVQ8Q9IsWE9oJG9VRAq6hwjKcvCe0065UwW9UR',
        'client_secret': 'Test client secret'
    }

    return render(request, template, context)

