from django.shortcuts import render, redirect
from collections import defaultdict
from .models import Sale
from .forms import SaleForm
import json



def home(request):

    if request.method == 'POST':

        form = SaleForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/')

    else:
        form = SaleForm()

    query = request.GET.get('q')

    if query:
        sales = Sale.objects.filter(product_name__icontains=query)

    else:
        sales = Sale.objects.all()

    total_revenue = 0

    product_names = []
    product_totals = []

    for sale in sales:

        revenue = sale.quantity * sale.price

        total_revenue += revenue

        product_names.append(sale.product_name)
        product_totals.append(revenue)

    total_orders = sales.count()
    monthly_data = defaultdict(int)
    for sale in sales:
        month = sale.created_at.strftime('%B')
        monthly_data[month] += sale.quantity * sale.price
        months = list(monthly_data.keys())
        monthly_revenue = list(monthly_data.values())

    context = {
        'sales': sales,
        'total_revenue': total_revenue,
        'total_orders': total_orders,
        'product_names': json.dumps(product_names),
        'product_totals': json.dumps(product_totals),
        'form': form,
        'months': json.dumps(months),
        'monthly_revenue': json.dumps(monthly_revenue),
    }

    return render(request, 'home.html', context)


def edit_sale(request, id):

    sale = Sale.objects.get(id=id)

    if request.method == 'POST':

        form = SaleForm(request.POST, instance=sale)

        if form.is_valid():
            form.save()

            return redirect('/')

    else:

        form = SaleForm(instance=sale)

    return render(request, 'edit.html', {'form': form})


def delete_sale(request, id):

    sale = Sale.objects.get(id=id)

    sale.delete()

    return redirect('/')