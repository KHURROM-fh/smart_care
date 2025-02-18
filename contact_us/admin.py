from django.contrib import admin
from . models import Contact_us
# Register your models here.

class ConcactUsModelAdmin(admin.ModelAdmin):
    list_display = ["name","mobile_no", "problem"]

admin.site.register(Contact_us, ConcactUsModelAdmin)