from django.contrib import admin
from .models import Poll, PollQuestion, User

# Register your models here.
admin.site.site_header = "Приложение для опросов"
admin.site.site_title = "Приложение для опросов - Панель управления"


class PollQuestions(admin.TabularInline):
    model = PollQuestion


class PollAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'active'
    )
    inlines = [PollQuestions]


admin.site.register(Poll, PollAdmin)
admin.site.register(User)
