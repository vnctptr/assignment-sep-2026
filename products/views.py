from django.http import HttpResponse
from django.template import loader

from .models import Product, Category, Tag

from django.db.models import Q


def search(request):
    # Parse query parameters
    query = request.GET.get("q", "")
    category_id = request.GET.get("category", "")
    tag_id = request.GET.get("tag", "")

    # Filter products
    products = Product.objects.all()
    if query:
        products = products.filter(Q(name__icontains=query) | Q(description__icontains=query))
    if category_id:
        products = products.filter(categories__id=category_id)
    if tag_id:
        products = products.filter(tags__id=tag_id)

    categories = Category.objects.all()
    tags = Tag.objects.all()

    template = loader.get_template("products/index.html")
    return HttpResponse(template.render(context={"products": products,
                                                 "categories": categories, "tags": tags,
                                                 "selected_category": category_id,
                                                 "selected_tag": tag_id,
                                                 "query": query}, request=request)
                        )
