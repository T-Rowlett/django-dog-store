from django.shortcuts import render, redirect
from app.models import DogProduct, Purchase, DogTag
# Create your views here.

def home(request):
    dog_products = DogProduct.objects.all()
    return render(request, "home.html", {"dog_products": dog_products})

def dog_product_detail(request, id):
    dog_product = dog_product.objects.get(id=id)
    return render(request, "dog_product_detail.html", {"dog_product": dog_product})

def purchase_dog_product(request, id):
    item = DogProduct.objects.get(id=id)
    if item.quanity > 0:
        item.quanity -= 1
        item.save()
        return redirect("dog_product_detail")
    else:
        return redirect("dog_product_detail")

def purchase_detail(request, id):
    purchase = Purchase_detail.objects.all()
    return render(request, "purchase_detail.html", {"purchase": purchase})

def new_dog_tag(request, id):
    dog_tag = DogTag.objects.get(id=id)
    if request.method == "GET":
        return render(request, "new_dog_template.html", {"dog_tag": dog_tag})

def dog_tag_list(request, id):
    dog_tag = DogTag.objects.get(id=id)
    return render(request, "dog_tag_list.html", {"dog_tag": dog_tag})