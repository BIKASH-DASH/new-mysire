from django.contrib import admin
from .models import Page,WhatWeDo,Social
# Register your models here.


class PageAdmin(admin.ModelAdmin):
    '''
        Admin View for Page
    '''
    fieldsets = (
        (None, {
            'fields': ( 'title', 'description', 'pub_date')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('meta_title', 'meta_description'),
        }),
    )


admin.site.register(Page, PageAdmin)

class WhatWeDoAdmin(admin.ModelAdmin):
    '''
        Admin View for WhatWeDo
    '''
    fieldsets = (
        (None, {
            'fields': ( 'title', 'description','image', 'pub_date')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('meta_title', 'meta_description'),
        }),
    )


admin.site.register(WhatWeDo, WhatWeDoAdmin)
admin.site.register(Social)