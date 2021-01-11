from django.contrib import admin

from .models import Laboratory, Reservation


class LaboratoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'n_computers', )

    class Meta:
        fields = '__all__'


class ReservationAdmin(admin.ModelAdmin):
    list_display = ('user', 'laboratory', 'date', 'initial_time', 'end_time', 'status')
    search_fields = ('user', 'laboratory', 'date')
    list_filter = ('laboratory', 'status')

    class Meta:
        fields = '__all__'


admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Laboratory, LaboratoryAdmin)


admin.site.site_header = 'GLAB :: Painel Administrativo'
admin.site.index_title = 'GLAB - UFAC'
admin.site.site_title = 'GLAB'