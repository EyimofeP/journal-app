from django.contrib import admin

from .models import Diary

# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ("user", "name", "color")
#     list_display_link = ("user",)
#     list_filter = ("user",)

## Admin View For Diary Page
class DiaryAdmin(admin.ModelAdmin):
    list_display = ("user", "title",)
    list_display_link = ("user",)
    list_filter = ("user","date")

# admin.site.register(Category, CategoryAdmin)
admin.site.register(Diary, DiaryAdmin)