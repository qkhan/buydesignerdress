from django.views.generic import ListView, DetailView

from django.shortcuts import render
from django.http import Http404
from items.models import Item
from django.utils import timezone

# Create your views here.

# class ProductListView(ListView):
#
#     model = Product
#     print ("ProductListView")
#     template_name = "products/product_list.html"
#
#     def get_queryset(self, *args, **kwargs):
#         #qs = super(BookListView, self).get_queryset(*args, **kwargs).filter(title__startswith="Ye")
#         qs = super(ProductListView, self).get_queryset(*args, **kwargs).order_by("-productTimestamp")
#         print ("QK1:", qs)
#         return qs
#
#     def get_context_data(self, **kwargs):
#         context = super(ProductListView, self).get_context_data(**kwargs)
#         context['now'] = timezone.now()
#         return context


class ProductListView(ListView):
    #queryset = Product.objects.all()
    template_name = "products/list.html"

    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductListView, self).get_context_data(*args, **kwargs)
    #     print(context)
    #     return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Item.objects.all()

class ProductDetailSlugView(DetailView):
    print("Hello Qaisar Khan")
    queryset = Item.objects.all()
    template_name = "products/detail.html"

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        try:
            instance = Item.objects.get(slug=slug, active=True)
        except Item.DoesNotExist:
            raise Http404("Not Found")
        except Item.MultipleObjectsReturned:
            qs = Item.objects.filter(slug=slug, active=True)
            instance = qs.first()
        except:
            raise Http404("Issue accessing the web page")
        return instance


class ProductDetailView(DetailView):
    print("Hello Qaisar")
    queryset = Item.objects.all()
    template_name = "products/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        return Product.objects.filter(pk=pk)
