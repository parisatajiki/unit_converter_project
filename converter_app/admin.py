from django.contrib import admin
from .models import Quantity,Units
# Register your models here.


class UnitsInline(admin.TabularInline):
    model = Units

@admin.register(Quantity)
class QuantityAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = (UnitsInline,)