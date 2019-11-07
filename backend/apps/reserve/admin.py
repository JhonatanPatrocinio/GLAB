from django.contrib import admin

from apps.reserve.models import Reserve


class ReserveAdmin(admin.ModelAdmin):
    list_display = ('user', 'laboratory', )

    class Meta:
        fields = '__all__'


admin.site.register(Reserve, ReserveAdmin)
