from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export.admin import ExportActionMixin,ImportExportMixin

# Register your models here.
from CRM_Data.models import *


@admin.register(Governorate)
class GovernorateAdmin(ImportExportModelAdmin):
    list_display = ['Governorate', 'note']
    list_filter = ['Governorate',]
    search_fields=['Governorate',]

# __________________________________________________________

@admin.register(SourceChannel)
class SourceChannelAdmin(admin.ModelAdmin):
    list_display = ['Source', 'note']
    list_filter = ['Source',]
    search_fields=['Source',]

# __________________________________________________________

@admin.register(Order_Status)
class Order_StatusAdmin(admin.ModelAdmin):
    list_display = ['status', 'note']
    list_filter = ['status',]
    search_fields=['status',]

# ______________________________________

@admin.register(Order_Feedback)
class Order_FeedbackAdmin(admin.ModelAdmin):
    list_display = ['Feedback', 'note']
    list_filter = ['Feedback',]
    search_fields=['Feedback',]

# ______________________________________

@admin.register(Designer)
class DesignerAdmin(admin.ModelAdmin):
    list_display = ["__str__",'name', 'note']
    list_filter = ['name',]
    search_fields=['name',]

# ______________________________________

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['Item', 'note']
    list_filter = ['Item',]
    search_fields=['Item',]


# __________________________________________________________

@admin.register(inquiry_Status)
class inquiry_StatusAdmin(admin.ModelAdmin):
    list_display = ['inquiry', 'note']
    list_filter = ['inquiry',]
    search_fields=['inquiry',]


# __________________________________________________________
@admin.register(Inquiry_Feedback)
class Inquiry_FeedbackAdmin(admin.ModelAdmin):
    list_display = ['inq_Feedback', 'note']
    list_filter = ['inq_Feedback',]
    search_fields=['inq_Feedback',]


# __________________________________________________________
