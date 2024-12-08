from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from django.urls import reverse
from import_export.admin import ExportActionMixin,ImportExportMixin
# Register your models here.
from Melouk_Eltibah.models import Melouk_Eltibah_Order,Melouk_Eltibah_Customer,Melouk_Eltibah_OrderDetail,Melouk_Eltibah_FeedBack,Melouk_Eltibah_Inquiry

class OrderInline(admin.TabularInline):
    model = Melouk_Eltibah_Order
    extra = 0
    # fields = ['OrderId','Source','Status','Feedback','Transfer',"Cash","Cost","Net","ITEMS","Shipping"]
    # exclude = ('Sales', )
    
@admin.register(Melouk_Eltibah_Customer)
class CustomerAdmin(admin.ModelAdmin):
    inlines = [OrderInline,]
    list_display = ["__str__",'Company','Client','Governorate',"Address","Created","Updated","Orders"]
    list_filter = ['Company','Client','Governorate',"Created","Updated"]
    search_fields=['Company','Client','Governorate','Phone_1',"Phone_2"]
    ordering=["-Updated"]
    list_per_page = 100

# __________________________________________________________

class OrderDetailInline(admin.TabularInline):
    model = Melouk_Eltibah_OrderDetail
    extra = 0
    
@admin.register(Melouk_Eltibah_Order)
class orderAdmin(admin.ModelAdmin):
    inlines = [OrderDetailInline]
    list_display = ['__str__','Sales',"Designer",'Customer','Source','Status','Feedback',"Order_Total",'Transfer',"Cost","ITEMS","Created","Updated"]
    list_filter = ['id','Sales','Customer','Source','Status','Feedback',"Designer","Created","Updated",]
    ordering=["-id"]
    search_fields = ['Customer__Company',"Customer__Phone_1","Customer__Phone_2",]
    # list_editable = ['Status',"Feedback","Transfer","Cash",]
    exclude = ("id", )
    list_per_page = 100
 
# ______________________________________
@admin.register(Melouk_Eltibah_OrderDetail)
class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ["Order",'Item','Item_Name',"Quantity","Price","Note"]
    list_filter = ['Order',"Order__Customer","Item","Item_Name","Price"]
    search_fields=['Item_Name',"Order__Customer__Company","Order__Customer__Phone_1","Order__Customer__Phone_2",]
    list_per_page = 100


# __________________________________________________________

class FeedBackInline(admin.TabularInline):
    model = Melouk_Eltibah_FeedBack
    extra = 0
    
@admin.register(Melouk_Eltibah_Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    inlines = [FeedBackInline]
    list_display = ['__str__','Sales','Order','inquiry','Details',"Created"]
    list_filter = ['Order',"Sales",'Order','inquiry']
    search_fields = ['Order','inquiry','Details']
    exclude = ("id",)
    list_per_page = 100

# ______________________________________


    
@admin.register(Melouk_Eltibah_FeedBack)
class FeedBackAdmin(admin.ModelAdmin):
    list_display = ["Cus_Service","sales_",'Inquiry',"order",'feedback',"Status","Created"]
    list_filter = ['Cus_Service',"Inquiry","Inquiry__Order__id","Inquiry__Order__Sales","Status"]
    search_fields=['Inquiry','feedback',"Status"]
    # exclude = ("Cus_Service",)

        #
    list_per_page = 100
        
