from django.contrib import admin
from todo.models import List


@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    """Отображение модели List в админке."""

    # def total_sum(self, obj):
    #     """Вычисляемое значение для только-читаемого поля."""
    #     return obj.total_sum

    # def amount(self, obj):
    #     """Вычисляемое значение для только-читаемого поля."""
    #     return obj.amount

    list_display = (
        "id",
        "name",
        "is_done",
        "start_dt",
        "end_dt",
    )
    readonly_fields = ["start_dt", "end_dt"]
    search_fields = ["name"]  # по каким полям будет производиться поиск
    list_filter = ["is_done", "name"]  # фильтры в правой части экрана
    # actions = [deactivate] # Добавление дополнительного действия в выпадающем меню
