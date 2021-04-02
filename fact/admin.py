from django.contrib import admin
from django.utils.safestring import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from .models import Fact, Category

class FactAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Fact
        fields = '__all__'


class FactAdmin(admin.ModelAdmin):
    form = FactAdminForm
    list_display = ['id', 'title', 'category', 'created_at', 'is_published', 'get_photo']
    list_display_links = ['title']
    search_fields = ['id', 'title', ]
    list_editable = ['is_published', ]
    list_filter = ['is_published', 'category']
    fields = ['title', 'category', 'content', 'photo', 'get_photo', 'is_published', 'views', 'created_at', 'updated_at']
    readonly_fields = ['get_photo', 'created_at', 'updated_at', 'views']

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75">')
        else:
            return 'не установлено'

    get_photo.short_description = 'фото'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['title']
    search_fields = ['title', ]


admin.site.register(Fact, FactAdmin)
admin.site.register(Category, CategoryAdmin)
