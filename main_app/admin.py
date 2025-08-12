from django.contrib import admin
from .models import Contact
from django.contrib import admin
from .models import Feedback
from django.contrib import admin
from .models import VisitorLog

from .models import Application

admin.site.register(Application)

@admin.register(VisitorLog)
class VisitorLogAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'timestamp', 'cookies_accepted')
    search_fields = ('ip_address', 'user_agent')
    list_filter = ('cookies_accepted',)


admin.site.register(Feedback)

admin.site.register(Contact)
# Register your models here.

