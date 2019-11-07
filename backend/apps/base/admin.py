from django.contrib import admin

from apps.base.models import Laboratory


class LaboratoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'n_computers', )

    class Meta:
        fields = '__all__'


admin.site.register(Laboratory, LaboratoryAdmin)
