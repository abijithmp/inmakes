# from django.core.paginator import Paginator,EmptyPage,InvalidPage
# from shopping_cart.models import Product,Category
# from django.shortcuts import render, redirect, get_object_or_404
#
#
# # Create your views here.
# def allProd(request,c_slug=None):
#     c_page=None
#     products_list=None
#     if c_slug!=None:
#         c_page=get_object_or_404(Category,slug=c_slug)
#         products_list=Product.objects.all().filter(category=c_page,available=True)
#     else:
#         products_list=Product.objects.all().filter(available=True)
#     paginator=Paginator(products_list,6)
#     try:
#         page=int(request.GET.get('page','1'))
#     except:
#         page=1
#     try:
#         products=paginator.page(page)
#     except (EmptyPage,InvalidPage):
#         products=paginator.page(paginator.num_pages)
#     return render(request,"category.html",{"category":c_page,"products":products})
