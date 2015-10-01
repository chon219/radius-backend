# -*- coding: utf-8 -*-

from django.contrib import admin

from radius.models import Cui
from radius.models import Nas
from radius.models import Radpostauth
from radius.models import Radreply
from radius.models import Radusergroup
from radius.models import Radcheck
from radius.models import Radgroupcheck
from radius.models import Radgroupreply
from radius.models import Radippool
from radius.models import Radacct


class CuiAdmin(admin.ModelAdmin):
    pass


class NasAdmin(admin.ModelAdmin):
    list_display = ('nasname', 'shortname', 'type', 'ports',)
    list_filter = ('type',)
    ordering = ('nasname', )
    search_fields = ('nasname', 'shortname', 'ports',)


class RadpostauthAdmin(admin.ModelAdmin):
    pass


class RadreplyAdmin(admin.ModelAdmin):
    list_display = ('username', 'attribute', 'op', 'value',)
    list_filter = ('username',)
    search_fields = ('attribute', 'value',)


class RadusergroupAdmin(admin.ModelAdmin):
    list_display = ('groupname', 'username',)
    list_filter = ('groupname',)
    search_fields = ('username',)


class RadcheckAdmin(admin.ModelAdmin):
    list_display = ('username', 'attribute', 'op', 'value',)
    list_filter = ('username',)
    search_fields = ('attribute', 'value',)


class RadgroupcheckAdmin(admin.ModelAdmin):
    list_display = ('groupname', 'attribute', 'op', 'value',)
    list_filter = ('groupname',)


class RadgroupreplyAdmin(admin.ModelAdmin):
    list_display = ('groupname', 'attribute', 'op', 'value',)
    list_filter = ('groupname',)


class RadippoolAdmin(admin.ModelAdmin):
    list_display = (
        'pool_name',
        'framedipaddress', 'nasipaddress', 'username', 'expiry_time',)
    list_filter = ('pool_name', 'nasipaddress',)
    search_fields = ('framedipaddress', 'username')


class RadacctAdmin(admin.ModelAdmin):
    list_display = (
        'acctuniqueid',
        'username', 'nasipaddress', 'acctstarttime', 'acctsessiontime',)
    list_filter = ('nasipaddress',)


admin.site.register(Cui, CuiAdmin)
admin.site.register(Nas, NasAdmin)
admin.site.register(Radpostauth, RadpostauthAdmin)
admin.site.register(Radreply, RadreplyAdmin)
admin.site.register(Radusergroup, RadusergroupAdmin)
admin.site.register(Radcheck, RadcheckAdmin)
admin.site.register(Radgroupcheck, RadgroupcheckAdmin)
admin.site.register(Radgroupreply, RadgroupreplyAdmin)
admin.site.register(Radippool, RadippoolAdmin)
admin.site.register(Radacct, RadacctAdmin)
