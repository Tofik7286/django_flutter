from django.contrib import admin
from .models import PassportData

@admin.register(PassportData)
class PassportDataAdmin(admin.ModelAdmin):
    list_display = ['passport_number', 'full_name', 'nationality', 'created_at']
    list_filter = ['nationality', 'created_at']
    search_fields = ['passport_number', 'full_name']
    readonly_fields = ['created_at', 'updated_at']
