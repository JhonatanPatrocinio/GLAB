from django.contrib import admin

from apps.reserve.models import Reserve


class ReserveAdmin(admin.ModelAdmin):
    list_display = ('user', 'laboratory', 'date', 'initial_time', 'end_time', 'status')
    search_fields = ('user', 'laboratory', 'date')
    list_filter = ('laboratory', 'status')

    class Meta:
        fields = '__all__'


admin.site.register(Reserve, ReserveAdmin)
