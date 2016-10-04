from django.contrib import admin
from .models import Category,Blog
# Register your models here.



class BlogAdmin(admin.ModelAdmin):
    '''
        Admin View for Blog
    '''
    fieldsets = (
        (None, {
            'fields': ( 'title', 'description','image','category', 'pub_date')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('meta_title', 'meta_description'),
        }),
    )


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)