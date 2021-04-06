from django.contrib import admin
from .models import Poll, PollQuestion


# Register your models here.
@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'active'
    )
    list_filter = ('id',)


admin.site.register(PollQuestion)
