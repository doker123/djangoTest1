from django.contrib import admin
from .models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'position', 'academic_degree', 'age', 'gender')
    list_filter = ('gender', 'marital_status', 'has_children', 'position')
    search_fields = ('full_name', 'position', 'academic_degree')
    readonly_fields = ('date_added',)

    fieldsets = (
        ('Основная информация', {
            'fields': ('full_name', 'position', 'academic_degree')
        }),
        ('Личные данные', {
            'fields': ('gender', 'age', 'marital_status', 'has_children')
        }),
        ('Системная информация', {
            'fields': ('date_added', 'added_by'),
            'classes': ('collapse',)
        }),
    )
