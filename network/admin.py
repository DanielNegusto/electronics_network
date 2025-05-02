from django.contrib import admin
from django.utils.html import format_html

from .models import Contact, Product, NetworkNode


class NetworkNodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'contacts', 'level', 'debt', 'supplier_link', 'created_at')
    list_filter = ('contacts__city',)  # Фильтр по городу
    search_fields = ('name', 'contacts__city')  # Поиск по названию и городу

    actions = ['clear_debt']  # Добавление действия

    def supplier_link(self, obj):
        if obj.supplier:
            return format_html('<a href="/admin/network/networknode/{}/">{}</a>', obj.supplier.id, obj.supplier.name)
        return "Нет поставщика"

    supplier_link.short_description = 'Поставщик'

    def clear_debt(self, request, queryset):
        """Очищает задолженность перед поставщиком у выбранных объектов."""
        queryset.update(debt=0)
        self.message_user(request, "Задолженность успешно очищена у выбранных объектов.")
    clear_debt.short_description = "Очистить задолженность у выбранных объектов"


admin.site.register(Contact)
admin.site.register(Product)
admin.site.register(NetworkNode, NetworkNodeAdmin)
