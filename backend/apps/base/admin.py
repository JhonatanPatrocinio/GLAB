from django.contrib import admin

from apps.base.models import Laboratory


class LaboratoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'n_computers', )

    class Meta:
        fields = '__all__'


admin.site.register(Laboratory, LaboratoryAdmin)


admin.site.site_header = 'GLAB :: Painel Administrativo'
admin.site.index_title = 'GLAB - UFAC'
admin.site.site_title = 'GLAB'