import datetime
from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags

# ===============================
# MAIN PAGE
# ===============================
@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")

    if filter_type == "all":
        product_list = Product.objects.all()
    else:
        product_list = Product.objects.filter(user=request.user)

    context = {
        'product_list': product_list,
        'last_login': request.COOKIES.get('last_login', 'Never')
    }
    return render(request, "main.html", context)


# ===============================
# CREATE PRODUCT (normal page)
# ===============================
@login_required(login_url='/login')
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        product_entry = form.save(commit=False)
        product_entry.user = request.user
        product_entry.save()
        messages.success(request, 'Product created successfully!')
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)


# ===============================
# PRODUCT DETAIL PAGE
# ===============================
@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    context = {'product': product}
    return render(request, "products_detail.html", context)


# ===============================
# SERIALIZERS
# ===============================
def show_xml(request):
    xml_data = serializers.serialize("xml", Product.objects.all())
    return HttpResponse(xml_data, content_type="application/xml")


def show_json(request):
    product_list = Product.objects.all()
    data = [
        {
            'id': str(p.id),
            'name': p.name,
            'description': p.description,
            'price': p.price,
            'category': p.category,
            'thumbnail': p.thumbnail,
            'created_at': p.created_at.isoformat() if p.created_at else None,
            'is_featured': p.is_featured,
            'user_id': p.user_id,
        }
        for p in product_list
    ]
    return JsonResponse(data, safe=False)


def show_xml_by_id(request, product_id):
    try:
        product_item = Product.objects.filter(pk=product_id)
        xml_data = serializers.serialize("xml", product_item)
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)


def show_json_by_id(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
        data = {
            'id': str(product.id),
            'name': product.name,
            'description': product.description,
            'price': product.price,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'created_at': product.created_at.isoformat() if product.created_at else None,
            'is_featured': product.is_featured,
            'user_id': product.user_id,
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)


# ===============================
# AUTH
# ===============================
def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form': form}
    return render(request, 'register.html', context)


def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response


# ===============================
# CREATE PRODUCT (AJAX)
# ===============================
@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
    name = strip_tags(request.POST.get("name"))
    description = strip_tags(request.POST.get("description"))
    category = request.POST.get("category")
    thumbnail = request.POST.get("thumbnail")
    is_featured = request.POST.get("is_featured") == 'on'
    user = request.user

    new_product = Product(
        name=name,
        description=description,
        category=category,
        thumbnail=thumbnail,
        is_featured=is_featured,
        user=user
    )
    new_product.save()

    return JsonResponse({"status": "created", "id": str(new_product.id)}, status=201)


# ===============================
# EDIT PRODUCT (AJAX)
# ===============================
@require_POST # Memastikan view ini hanya menerima request POST
def edit_product_entry_ajax(request):
    product_id = request.POST.get('id')

    # Jika ada 'id', berarti ini adalah operasi EDIT/UPDATE
    if product_id:
        try:
            # Ambil produk yang ada dari database
            product_instance = get_object_or_404(Product, pk=product_id)
            
            # Isi form dengan data request DAN instance produk yang akan diupdate
            form = ProductForm(request.POST, instance=product_instance)
        except Product.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Product not found.'}, status=404)
    
    # Jika tidak ada 'id', ini adalah operasi CREATE BARU
    else:
        form = ProductForm(request.POST)

    if form.is_valid():
        form.save()
        return JsonResponse({'status': 'success', 'message': 'Product saved successfully.'})
    else:
        # Mengembalikan error validasi jika form tidak valid
        return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)




# ===============================
# DELETE PRODUCT (AJAX + Normal)
# ===============================
@csrf_exempt
@require_POST
def delete_product(request, id=None):
    """
    Bisa dipanggil dari:
    - AJAX (POST ke /product/<id>/delete/)
    - Normal view redirect
    """
    if not id:
        return JsonResponse({"status": "missing id"}, status=400)

    product = get_object_or_404(Product, pk=id, user=request.user)
    product.delete()

    # jika request dari AJAX
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({"status": "deleted"}, status=200)

    # jika normal redirect
    return HttpResponseRedirect(reverse('main:show_main'))
