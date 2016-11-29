# -*- coding: utf-8 -*-

from django.contrib import admin
from TestModel.models import Contact, Tag


# Register your models here.
class TagInline(admin.TabularInline):
    model = Tag


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'gender', 'email', 'tele', 'address', 'postcode', 'notes')   # List
    list_filter = ['postcode']
    search_fields = ['name', 'tele', 'postcode']
#    inlines = [TagInline]   # Inline
    fieldsets = (
        [u'主要信息', {
            'fields': ('name', 'gender', 'email', 'tele', 'address', 'postcode', 'notes'),
        }],
        [u'其他信息', {
            'classes': ('collapse',),  # CSS
            'fields': ('age',),
        }]
    )


# admin.site.register(Test)
admin.site.register(Contact, ContactAdmin)
# admin.site.register(Tag)
