from django.contrib import admin

from .models import Laboratory, Reservation, AcademicCenter, Course


class LaboratoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'n_computers', 'capacity')

    class Meta:
        fields = '__all__'


class ReservationAdmin(admin.ModelAdmin):
    list_display = ('user', 'laboratory', 'date', 'initial_time', 'end_time', 'status')
    search_fields = ('user', 'laboratory', 'date')
    list_filter = ('laboratory', 'status')
    readonly_fields = ('update_at', )

    class Meta:
        fields = '__all__'


class AcademicCenterAdmin(admin.ModelAdmin):
    list_display = ('name', 'shortening')
    search_fields = ('name', 'shortening')
    readonly_fields = ('update_at', )

    class Meta:
        fields = '__all__'


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'cod')
    search_fields = ('name', 'cod')
    readonly_fields = ('update_at', )

    class Meta:
        fields = '__all__'


admin.site.register(Course, CourseAdmin)
admin.site.register(AcademicCenter, AcademicCenterAdmin)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Laboratory, LaboratoryAdmin)


admin.site.site_header = 'GLAB :: Painel Administrativo'
admin.site.index_title = 'GLAB - UFAC'
admin.site.site_title = 'GLAB'
