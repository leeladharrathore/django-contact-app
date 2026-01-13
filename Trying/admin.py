from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'user','created_at')
    search_fields = ('name', 'email')
    list_filter = ('created_at',)
    ordering = ('-created_at',)

def save_model(self, request, obj, form, change):
    if not obj.pk:
        obj.user = request.user
    super().save_model(request, obj, form, change)

