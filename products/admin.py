from django.contrib import admin

from products.models import Basket, Product, ProductCategory

admin.site.register(ProductCategory)


@admin.register(Product)  # переопределим админку для продуктов
class ProductAdmin(admin.ModelAdmin):  # наследуемся от админки
    list_display = ('name', 'price', 'quantity', 'category')
    # картедж в котредже что бы выводить на одну строку
    fields = ('image', 'name', 'description', ('price', 'quantity'), 'category')
    readonly_fields = ('description',)  # сделать поле только не для редактирования
    search_fields = ('name',)  # добавляем поле для поиска
    # добавление сортировки, если вместо 'name' сделать '-name' будет в обратном порядке
    ordering = ('name', 'price', 'quantity', 'category')


# админка как часть другой админки, в закладке пользователей добавляем таблицу с товарами в корзине в админке
class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity')  # добавить поле таймстамп
    extra = 0  # делаем что бы не было полей для добавления товаров в карзину пользователя из админки
