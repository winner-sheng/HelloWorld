# -*- coding: utf-8 -*-

from django.contrib import admin
from Computer.models import Computer, Manufacturer


# Register your models here.
class ComputerAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'm_board', 'cpu_info', 'mem_info', 'hdd_info', 'mac_address', 'user', 'buy_date', 'notes')
    #    list_filter = ['postcode']
    search_fields = ['name', 'user', 'tv_id']
    #    inlines = [TagInline]   # Inline
    fieldsets = (
        [u'主要信息', {
            'fields': ('name', 'brand', 'm_board', 'cpu_info', 'mem_info', 'hdd_info', 'mac_address', 'user', 'notes'),
        }],
        [u'其他信息', {
            'classes': ('collapse',),  # CSS
            'fields': ('tv_id', 'tv_password'),
        }]
    )


class ManufacturerAdmin(admin.ModelAdmin):
#    list_display = ('brand')
    search_fields = ['manufacturer']


admin.site.register(Computer, ComputerAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)
