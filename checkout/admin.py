from django.contrib import admin
from .models import Order, OrderLineItem, DiscountCode


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    def get_discount_code_discount(self, obj):
        """
        Custom method to calculate and display the discount using the figure from the DiscountCode model.
        """
        if obj.discount_code:
            try:
                code_instance = DiscountCode.objects.get(code=obj.discount_code.code)
                discount = obj.order_total * code_instance.percentage / 100
                return round(discount, 2)
            except DiscountCode.DoesNotExist:
                pass
        return 0

    get_discount_code_discount.short_description = 'Discount Code Discount'

    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'discount_spend', 'discount_code', 
                       'grand_total', 'original_bag', 'stripe_pid',
                       'get_discount_code_discount')

    fields = ('order_number', 'user_profile', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'delivery_cost',
              'discount_spend', 'discount_code', 'get_discount_code_discount',
               'order_total', 'grand_total', 'original_bag', 'stripe_pid',)

    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'delivery_cost',
                    'grand_total',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
admin.site.register(DiscountCode)