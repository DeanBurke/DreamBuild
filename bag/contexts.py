from decimal import Decimal
from django.conf import settings
from django.shortcuts import redirect, get_object_or_404
from products.models import Product
from checkout.forms import DiscountForm, TipForm
from checkout.models import DiscountCode

def bag_contents(request):
    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.price
            product_count += item_data
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })
        else:
            product = get_object_or_404(Product, pk=item_id)
            for size, quantity in item_data['items_by_size'].items():
                total += quantity * product.price
                product_count += quantity
                bag_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'size': size,
                })

    if total > settings.ORDER_DISCOUNT:
        discount = total * Decimal(settings.DISCOUNT_PERCENTAGE / 100)
    else:
        discount = 0

    discount2 = 0

    if 'discount_code' in request.session:
        discount_code = request.session['discount_code']
        try:
            code_instance = DiscountCode.objects.get(code=discount_code)
            discount2 = total * Decimal(code_instance.percentage / 100)
        except DiscountCode.DoesNotExist:
            messages.error(request, 'Invalid discount code')
            return redirect(reverse('checkout'))

    total_discount = discount + discount2

    tip_amount = 0
    
    if 'tip_percentage' in request.session:
        tip_percentage = request.session['tip_percentage']
        try:
            tip_amount = total * Decimal(int(tip_percentage) / 100)
        except TypeError:
            messages.error(request, 'Invalid Tip Ampunt')
            return redirect(reverse('checkout'))

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0
    
    grand_total = delivery + total - total_discount + tip_amount
    
    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'total_discount': total_discount,
        'discount_threshold': settings.ORDER_DISCOUNT,
        'discount_percentage': settings.DISCOUNT_PERCENTAGE,
        'delivery': delivery,
        'tip_amount': tip_amount,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
