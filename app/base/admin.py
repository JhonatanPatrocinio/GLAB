from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from base.models import Hall, Department, TypePlace, Place, Reservation


class HallAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'short_name')

    class Meta:
        fields = '__all__'


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'hall', 'maintainer', 'contact')

    class Meta:
        fields = '__all__'


class TypePlaceAdmin(admin.ModelAdmin):
    list_display = ('name', )

    class Meta:
        fields = '__all__'


class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'department')

    fieldsets = (
        (_('Informações Básicas'), {'fields': ('name', 'type', 'department', 'map_link', 'is_active')}),
        (_('Informações sobre o Espaço'), {
            'classes': ('wide', ),
            'fields': ('capacity', 'is_washroom', 'is_water', 'is_air_conditioner', 'is_board', 'is_projector'),
        }),
        (_('Informações sobre Laboratório'), {
            'classes': ('wide', ),
            'fields': ('n_computers', 'is_internet')
        }),
        (_('Informações sobre Auditório'), {
            'classes': ('wide', ),
            'fields': ('is_soundbox', )
        }),
        (_('Informações sobre Quadra'), {
            'classes': ('wide', ),
            'fields': ('is_bleachers', 'is_roof', 'type_court')
        }),
    )


    class Meta:
        fields = '__all__'


class ReservationAdmin(admin.ModelAdmin):
    list_display = ('user', 'place', 'date', 'initial_time', 'end_time', 'status')
    search_fields = ('user', 'place', 'date')
    list_filter = ('place', 'status')
    readonly_fields = ('update_at', 'user', 'place', 'date', 'initial_time', 'end_time', 'phone', 'reason', 'obs')

    class Meta:
        fields = '__all__'


admin.site.register(Hall, HallAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(TypePlace, TypePlaceAdmin)
admin.site.register(Place, PlaceAdmin)
admin.site.register(Reservation, ReservationAdmin)


admin.site.site_header = 'GLAB :: Painel Administrativo'
admin.site.index_title = 'GLAB - UFAC'
admin.site.site_title = 'GLAB'
