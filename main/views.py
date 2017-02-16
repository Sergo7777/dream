from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from datetime import *
import random
import string
from main.models import *
from cart.forms import CartAddProductForm
 
def place_search(request):
	category = Category.objects.all()
	cart_product_form = CartAddProductForm()
	errors = {}
	if 'q' in request.GET:
		q = request.GET['q']
		if not q:
			errors = 'Введите название товара для поиска.'
		elif len(q) > 20:
			errors = 'Введите не более 20 символов.'
		else:
			products = Product.objects.filter(name__icontains=q)
			return render(request, 'search.html',
				{'products': products, 'categories': category, 
					'query': q, 'cart_product_form': cart_product_form })
	return render(request, 'search.html',
		{'errors': errors, 'categories': category, 
			'cart_product_form': cart_product_form})


def home(request,):
	category = Category.objects.all()
	products = Product.objects.all()

	cart_product_form = CartAddProductForm()
	# paginate
	paginator = Paginator(products, 4)
	page = request.GET.get('page')
	try:
		products = paginator.page(page)
	except PageNotAnInteger:
		products = paginator.page(1)
	except EmptyPage:
		products = paginator.page(paginator.num_pages)

	return render(request, 'home.html', 
					{'products':products, 'categories': category, 
						'cart_product_form': cart_product_form})


def item(request, alias):
	try:
		category = Category.objects.all()
		product = Product.objects.get(alias=alias)
		cart_product_form = CartAddProductForm()
	except:
		raise Http404('Объект не найден')
	context = {
	    'product': product,
	    'categories': category,
	    'cart_product_form': cart_product_form,
	}
	return HttpResponse(render_to_string('tovar.html', context))

def get_category(request, alias):
	try:
		category = Category.objects.get(alias=alias)
		products = Product.objects.filter(category=category)
		cart_product_form = CartAddProductForm()
	except:
		raise Http404('Объект не найден')
	return render(request, 'item3.html', 
					{'products': products, 'category':category, 
						'cart_product_form': cart_product_form})

	#view for menu

def products(request):
	category = Category.objects.all()
	products = Product.objects.all()
	cart_product_form = CartAddProductForm()
	# try to order products list
	order_by = request.GET.get('order_by', '')
	if order_by in ('name', 'price'):
		products = products.order_by(order_by)
		if request.GET.get('reverse', '') == '1':
			products = products.reverse()

	# paginate
	paginator = Paginator(products, 8)
	page = request.GET.get('page')
	try:
		products = paginator.page(page)
	except PageNotAnInteger:
		products = paginator.page(1)
	except EmptyPage:
		products = paginator.page(paginator.num_pages)

	return render(request, 'products.html', 
					{'products':products, 'categories': category, 
					 'cart_product_form': cart_product_form})

def dostavka(request):
	category = Category.objects.all()
	return render(request, 'dostavka.html', {'categories':category})

def garantia(request):
	category = Category.objects.all()
	context = {
	    'category': category,
	}
	return render(request, 'garantia.html', {'categories': category})


