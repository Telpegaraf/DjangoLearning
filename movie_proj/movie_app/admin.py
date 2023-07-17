from django.contrib import admin, messages
from .models import Movie, Director, Actor, DressingRoom
from django.db.models import QuerySet

# Register your models here.
admin.site.register(Director)
admin.site.register(Actor)
#admin.site.register(DressingRoom)


@admin.register(DressingRoom)
class DressingRoomAdmin(admin.ModelAdmin):
    list_display = ['floor', 'number', 'actor']


class BudgetFilter(admin.SimpleListFilter): # лист фильтров
    title = 'Фильтр по бюджету'
    parameter_name = 'бюджет'

    def lookups(self, request, model_admin):
        return [
            ('<500000', 'Низкий бюджет'),
            ('От 500000 до 1000000', 'Средний бюджет'),
            ('>=1000000', 'Большой бюджет')
        ]

    def queryset(self, request, queryset: QuerySet):
        if self.value()=='<500000':
            return queryset.filter(budget__lt=500000)
        return queryset


@admin.register(Movie) # Декоратор регистрации класса
class MovieAdmin(admin.ModelAdmin):
    exclude = ['slug'] # добавление нового, что не будет показывать
    readonly_fields = ['year'] # Что нельзя редактировать при добавлении нового (Должно быть blank=True в models)
    list_display = ['name', 'rating', 'director', 'rating_status', 'currency'] # Поле отображения
    list_editable = ['rating', 'director', 'currency'] # Лист редактирования, не должно повторяться первое поле отображения в display
    ordering = ['name', '-rating'] # Сортировка по колонке
    filter_horizontal = ['actors'] # фильтр для связи Many-to-many (виджет)
    list_per_page = 3 # сколько отображается на странице
    actions = ['set_dollars', 'set_euro']
    search_fields = ['name'] # Поля, по которым идет поиск
    list_filter = ['name', BudgetFilter] # Фильтр справа

    @admin.display(description='Статус') #Название колонки вручную, а не как называется функция
    def rating_status(self, mov: Movie): #Дополнительная колонка с описанием
        if mov.rating < 50:
            return f'Зачем это смотреть?'
        elif mov.rating < 70:
            return f'Разок можно глянуть'
        else:
            return f'Топчик'

    @admin.action(description='Установить валюту в долларах')
    def set_dollars(self, request, qs: QuerySet):
        qs.update(currency=Movie.USD)

    @admin.action(description='Установить валюту в евро')
    def set_euro(self, request, qs: QuerySet):
        count = qs.update(currency=Movie.EUR)
        self.message_user(
            request,
            f'Было обновлено {count} записей',
            messages.ERROR # Отображение красным (from django.contrib import admin, messages)
        )