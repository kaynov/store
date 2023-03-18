from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from rest_framework import mixins, viewsets
from rest_framework.schemas.openapi import AutoSchema

from common.views import TitleMixin
from products.models import Basket, Product, ProductCategory

from .filters import ProductFilterSet
from .serializers import ProductSerializer


# IndexView и ProductsListView - классовое представление
# переопределяем индексвью для продуктов через класс бейзд вью(миксины)
class IndexView(TitleMixin, TemplateView):
    template_name = 'products/index.html'
    title = 'Store'


# переопределяем индексвью для продуктов через класс бейзд вью(миксины)
class ProductsListView(TitleMixin, ListView):
    model = Product  # работаем с моделью Продуктов
    template_name = 'products/products.html'
    paginate_by = 3
    title = 'Store - Каталог'

    def get_queryset(self):  # фильтрация по категориям из запроса
        queryset = super(ProductsListView, self).get_queryset()
        category_id = self.kwargs.get('category_id')  # все параметры в том числе для фильтрации по категори ID/
        # , делаем через словарь что бы в случае когда мы на исходной при обращение к ключу из словаря возврат был None
        return queryset.filter(category_id=category_id) if category_id else queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsListView, self).get_context_data()
        context['categories'] = ProductCategory.objects.all()
        return context


# basket_add и basket_remove - функциональное представление
@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


class ProductViewSet(
    mixins.ListModelMixin,  # GET /tasks
    mixins.CreateModelMixin,  # POST /tasks
    mixins.RetrieveModelMixin,  # GET /articles/1
    mixins.DestroyModelMixin,  # DELETE /articles/1
    mixins.UpdateModelMixin,  # PUT /articles/1
    viewsets.GenericViewSet
):
    queryset = Product.objects.all().order_by("-id")
    serializer_class = ProductSerializer
    filterset_class = ProductFilterSet

    schema = AutoSchema(
        tags=['ProductList'],
        component_name=' Product',
        operation_id_base=' Product',
    )
