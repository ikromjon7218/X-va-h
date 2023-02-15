from django.contrib import admin
from .models import *

admin.site.register(Togri)
admin.site.register(Xato)

# @admin.register(Xato)
# class Notogri(admin.ModelAdmin):
#     list_display = "id", "notogri"
#     list_display_links = 'id', 'notogri'
#     list_filter = 'id', 'notogri'
#     list_per_page = 5
    # search_fields = 'id', 'notogri'
#
# @admin.register(Togri)
# class Togri(admin.ModelAdmin):
#     list_display = "id", "soz"
#     list_display_links = 'id', 'soz'
#     list_filter = 'id', 'soz'
#     list_per_page = 5
    # search_fields = 'id', 'soz'
#