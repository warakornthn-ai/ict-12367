from django.contrib import admin
from .models import Employee, Population


@admin.register(Population)
class PopulationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'age', 'created_at')
    search_fields = ('full_name',)
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'position', 'email', 'phone', 'created_at')
    list_filter = ('position',)
    search_fields = ('full_name', 'email', 'phone')
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)
