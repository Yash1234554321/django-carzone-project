from django.contrib import admin
from django.utils.html import format_html

from .models import Team

# Register your models here.
class TeamAdmin(admin.ModelAdmin):

    # def admin_thumbnail(self):
    #     return u'<img src="%s" />' % (self.photo.url)
    # admin_thumbnail.short_description = 'Thumbnail'
    # admin_thumbnail.allow_tags = True   

    # def thumbnail(self,object):
    #     return format_html('<img src="{}" width="40" style="border-radius:50px;" />'.format(object.photo.url))

    # thumbnail.short_description = "Photo"

    list_display = ("id","first_name","designation","created_date")
    list_display_links = ("id","first_name")
    search_fields = ("first_name","last_name","designation")
    list_filter = ("designation",)

admin.site.register(Team,TeamAdmin)

