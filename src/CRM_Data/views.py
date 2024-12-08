from django.shortcuts import render,get_object_or_404
from Dr_Print.models import Dr_Print_Order,Dr_Print_Customer,Dr_Print_FeedBack,Dr_Print_Inquiry
from Etbaly_Shokran.models import Etbaly_Shokran_Order,Etbaly_Shokran_Customer,Etbaly_Shokran_FeedBack,Etbaly_Shokran_Inquiry
from Melouk_Eltibah.models import Melouk_Eltibah_Order,Melouk_Eltibah_Customer,Melouk_Eltibah_FeedBack,Melouk_Eltibah_Inquiry
from Print_Square.models import Print_Square_Order,Print_Square_Customer,Print_Square_FeedBack,Print_Square_Inquiry
# from New_Project_1.models import New_Project_1_Order,New_Project_1_Customer,New_Project_1_FeedBack,New_Project_1_Inquiry
# from New_Project_2.models import New_Project_2_Order,New_Project_2_Customer,New_Project_2_FeedBack,New_Project_2_Inquiry
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

@login_required
def Dashboard(request):
    return render(request, 'Dashboard.html',{})

#___________________________________________________________________
@login_required
def Dr_Print_invoice(request, id):
        obj = get_object_or_404(Dr_Print_Order, id=id)
        context={'order':obj}
        return render(request, 'Dr_Print/Dr_Print_invoice.html', context)
    
    
@login_required
def Dr_Print_order_list(request):
    # Retrieve all records from the database
    orders = Dr_Print_Order.objects.select_related("Customer").all().order_by("-id")
    # paginator = Paginator(orders, 100)
    # page_number = request.GET.get("page")
    # page_obj = paginator.get_page(page_number)
    # Render a template with the records
    Dr_Printorders = int(Dr_Print_Order.objects.all().count())
    Customers = int(Dr_Print_Customer.objects.all().count())
    Inquiries = int(Dr_Print_Inquiry.objects.all().count())
    FeedBacks = int(Dr_Print_FeedBack.objects.all().count())
    # Dr_Print(status)
    Return = int(Dr_Print_Order.objects.filter(Status__status='Return').count())
    Return_percentage  = (Return / Dr_Printorders) * 100
    Delivered = int(Dr_Print_Order.objects.filter(Status__status='Delivered').count())
    Delivered_percentage  = (Delivered / Dr_Printorders) * 100
    Shipping = int(Dr_Print_Order.objects.filter(Status__status='Shipping').count())
    Shipping_percentage  = (Shipping / Dr_Printorders) * 100
    Cancel_Order = int(Dr_Print_Order.objects.filter(Status__status='Shipping').count())
    Cancel_Order_percentage  = (Cancel_Order / Dr_Printorders) * 100
    Progress = int(Dr_Print_Order.objects.filter(Status__status='Progress').count())
    Progress_percentage  = (Progress / Dr_Printorders) * 100
    Created = int(Dr_Print_Order.objects.filter(Status__status='Created').count())
    Created_percentage  = (Created / Dr_Printorders) * 100
    High_Price = int(Dr_Print_Order.objects.filter(Status__status='High_Price').count())
    High_Price_percentage  = (High_Price / Dr_Printorders) * 100
    Just_Ask = int(Dr_Print_Order.objects.filter(Status__status='Just_Ask').count())
    Just_Ask_percentage  = (Just_Ask / Dr_Printorders) * 100
    Follow_Up = int(Dr_Print_Order.objects.filter(Status__status='Follow_Up').count())
    Follow_Up_percentage  = (Follow_Up / Dr_Printorders) * 100
    New_Lead = int(Dr_Print_Order.objects.filter(Status__status='New_Lead').count())
    New_Lead_percentage  = (New_Lead / Dr_Printorders) * 100
    # Dr_Print(SourceChannel)
    Whatsapp = Dr_Print_Order.objects.filter(Source__Source='Whatsapp').count()
    Whatsapp_percentage  = (Whatsapp / Dr_Printorders) * 100
    Instagram = Dr_Print_Order.objects.filter(Source__Source='Instagram').count()
    Instagram_percentage  = (Instagram / Dr_Printorders) * 100
    Facebook = Dr_Print_Order.objects.filter(Source__Source='Facebook').count()
    Facebook_percentage  = (Facebook / Dr_Printorders) * 100
    # Dr_Print(inquiry_Status)
    Complaint = Dr_Print_Inquiry.objects.filter(inquiry__inquiry='Complaint').count()
    Complaint_percentage  = (Complaint / Dr_Printorders) * 100
    Order_Late = Dr_Print_Inquiry.objects.filter(inquiry__inquiry='Order_Late').count()
    Order_Late_percentage  = (Order_Late / Dr_Printorders) * 100
    # Dr_Print(Inquiry_Feedback)
    Wrong_Inquiry = Dr_Print_FeedBack.objects.filter(Status__inq_Feedback='Wrong_Inquiry').count()
    Wrong_Inquiry_percentage  = (Wrong_Inquiry / Dr_Printorders) * 100
    Solved = Dr_Print_FeedBack.objects.filter(Status__inq_Feedback='Solved').count()
    Solved_percentage  = (Solved / Dr_Printorders) * 100
    Follow_Up = Dr_Print_FeedBack.objects.filter(Status__inq_Feedback='Follow_Up').count()
    Follow_Up_percentage  = (Follow_Up / Dr_Printorders) * 100
    # Dr_Print(Inquiry_Feedback)
    
    context = {
        'orders': orders,
        'count':Dr_Printorders,
        "Customers" : Customers,
        "Inquiries" : Inquiries,
        "FeedBacks" : FeedBacks,
        # Dr_Print(status)
        "Return" : Return,
        "Return_percentage":Return_percentage,
        "Delivered" :Delivered,
        "Delivered_percentage"  : Delivered_percentage,
        "Shipping":Shipping,
        "Shipping_percentage"  : Shipping_percentage,
        "Cancel_Order" : Cancel_Order,
        "Cancel_Order_percentage"  : Cancel_Order_percentage,
        "Progress" : Progress,
        "Progress_percentage"  : Progress_percentage,
        "Created" :Created,
        "Created_percentage" :Created_percentage,
        "High_Price" : High_Price,
        "High_Price_percentage"   : High_Price_percentage,
        "Just_Ask" : Just_Ask,
        "Just_Ask_percentage" :Just_Ask_percentage,  
        "Follow_Up" : Follow_Up,
        "Follow_Up_percentage"  : Follow_Up_percentage,
        "New_Lead" :New_Lead,
        "New_Lead_percentage"  :New_Lead_percentage,
        # Dr_Print(SourceChannel)
        "Whatsapp" : Whatsapp,
        "Whatsapp_percentage"  :Whatsapp_percentage, 
        "Instagram" : Instagram,
        "Instagram_percentage"  : Instagram_percentage,
        "Facebook" : Facebook,
        "Facebook_percentage"  : Facebook_percentage,
        # Dr_Print(inquiry_Status)
        "Complaint":Complaint,   
        "Complaint_percentage" : Complaint_percentage,
        "Order_Late" : Order_Late, 
        "Order_Late_percentage" :Order_Late_percentage,
        # Dr_Print(Inquiry_Feedback)
        "Wrong_Inquiry" : Wrong_Inquiry,
        "Wrong_Inquiry_percentage"  : Wrong_Inquiry_percentage,
        "Solved" : Solved,
        "Solved_percentage" : Solved_percentage,
        "Follow_Up" : Follow_Up,
        "Follow_Up_percentage"  : Follow_Up_percentage,       
                
            }
    return render(request, 'Dr_Print/Dr_Print_Orders.html', context)


    
    
    
#_________________________________________________________________________
@login_required
def Etbaly_Shokran_invoice(request, id):
        obj = get_object_or_404(Etbaly_Shokran_Order, id=id)
        context={'order':obj}
        return render(request, 'Etbaly_Shokran/Etbaly_Shokran_invoice.html', context)



@login_required
def Etbaly_Shokran_order_list(request):
    # Retrieve all records from the database
    orders = Etbaly_Shokran_Order.objects.select_related("Customer").all().order_by("-id")
    # paginator = Paginator(orders, 100)
    # page_number = request.GET.get("page")
    # page_obj = paginator.get_page(page_number)
    # Render a template with the records
    Etbaly_Shokranorders = Etbaly_Shokran_Order.objects.all().count()
    Customers = Etbaly_Shokran_Customer.objects.all().count()
    Inquiries = Etbaly_Shokran_Inquiry.objects.all().count()
    FeedBacks = Etbaly_Shokran_FeedBack.objects.all().count()
    # Etbaly_Shokran(status)
    Return = int(Etbaly_Shokran_Order.objects.filter(Status__status='Return').count())
    Return_percentage  = (Return / Etbaly_Shokranorders) * 100
    Delivered = int(Etbaly_Shokran_Order.objects.filter(Status__status='Delivered').count())
    Delivered_percentage  = (Delivered / Etbaly_Shokranorders) * 100
    Cancel_Order = int(Etbaly_Shokran_Order.objects.filter(Status__status='Shipping').count())
    Cancel_Order_percentage  = (Cancel_Order / Etbaly_Shokranorders) * 100
    Progress = int(Etbaly_Shokran_Order.objects.filter(Status__status='Progress').count())
    Progress_percentage  = (Progress / Etbaly_Shokranorders) * 100
    Created = int(Etbaly_Shokran_Order.objects.filter(Status__status='Created').count())
    Created_percentage  = (Created / Etbaly_Shokranorders) * 100
    High_Price = int(Etbaly_Shokran_Order.objects.filter(Status__status='High_Price').count())
    High_Price_percentage  = (High_Price / Etbaly_Shokranorders) * 100
    Just_Ask = int(Etbaly_Shokran_Order.objects.filter(Status__status='Just_Ask').count())
    Just_Ask_percentage  = (Just_Ask / Etbaly_Shokranorders) * 100
    Follow_Up = int(Etbaly_Shokran_Order.objects.filter(Status__status='Follow_Up').count())
    Follow_Up_percentage  = (Follow_Up / Etbaly_Shokranorders) * 100
    New_Lead = int(Etbaly_Shokran_Order.objects.filter(Status__status='New_Lead').count())
    New_Lead_percentage  = (New_Lead / Etbaly_Shokranorders) * 100
    # Etbaly_Shokran(SourceChannel)
    Whatsapp = Etbaly_Shokran_Order.objects.filter(Source__Source='Whatsapp').count()
    Whatsapp_percentage  = (Whatsapp / Etbaly_Shokranorders) * 100
    Instagram = Etbaly_Shokran_Order.objects.filter(Source__Source='Instagram').count()
    Instagram_percentage  = (Instagram / Etbaly_Shokranorders) * 100
    Facebook = Etbaly_Shokran_Order.objects.filter(Source__Source='Facebook').count()
    Facebook_percentage  = (Facebook / Etbaly_Shokranorders) * 100
    # Etbaly_Shokran(inquiry_Status)
    Complaint = Dr_Print_Inquiry.objects.filter(inquiry__inquiry='Complaint').count()
    Complaint_percentage  = (Complaint / Etbaly_Shokranorders) * 100
    Order_Late = Dr_Print_Inquiry.objects.filter(inquiry__inquiry='Order_Late').count()
    Order_Late_percentage  = (Order_Late / Etbaly_Shokranorders) * 100
    # Etbaly_Shokran(Inquiry_Feedback)
    Wrong_Inquiry = Etbaly_Shokran_FeedBack.objects.filter(Status__inq_Feedback='Wrong_Inquiry').count()
    Wrong_Inquiry_percentage  = (Wrong_Inquiry / Etbaly_Shokranorders) * 100
    Solved = Etbaly_Shokran_FeedBack.objects.filter(Status__inq_Feedback='Solved').count()
    Solved_percentage  = (Solved / Etbaly_Shokranorders) * 100
    Follow_Up = Etbaly_Shokran_FeedBack.objects.filter(Status__inq_Feedback='Follow_Up').count()
    Follow_Up_percentage  = (Follow_Up / Etbaly_Shokranorders) * 100
    # Etbaly_Shokran(Inquiry_Feedback)
    context = {
        'orders': orders,
        'count':Etbaly_Shokranorders,
        "Customers" : Customers,
        "Inquiries" : Inquiries,
        "FeedBacks" : FeedBacks,
        # Etbaly_Shokran(status)
        "Return" : Return,
        "Return_percentage":Return_percentage,
        "Delivered" :Delivered,
        "Delivered_percentage"  : Delivered_percentage,
        "Cancel_Order" : Cancel_Order,
        "Cancel_Order_percentage"  : Cancel_Order_percentage,
        "Progress" : Progress,
        "Progress_percentage"  : Progress_percentage,
        "Created" :Created,
        "Created_percentage" :Created_percentage,
        "High_Price" : High_Price,
        "High_Price_percentage"   : High_Price_percentage,
        "Just_Ask" : Just_Ask,
        "Just_Ask_percentage" :Just_Ask_percentage,  
        "Follow_Up" : Follow_Up,
        "Follow_Up_percentage"  : Follow_Up_percentage,
        "New_Lead" :New_Lead,
        "New_Lead_percentage"  :New_Lead_percentage,
        # Etbaly_Shokran(SourceChannel)
        "Whatsapp" : Whatsapp,
        "Whatsapp_percentage"  :Whatsapp_percentage, 
        "Instagram" : Instagram,
        "Instagram_percentage"  : Instagram_percentage,
        "Facebook" : Facebook,
        "Facebook_percentage"  : Facebook_percentage,
        # Etbaly_Shokran(inquiry_Status)
        "Complaint":Complaint,   
        "Complaint_percentage" : Complaint_percentage,
        "Order_Late" : Order_Late, 
        "Order_Late_percentage" :Order_Late_percentage,
        # Etbaly_Shokran(Inquiry_Feedback)
        "Wrong_Inquiry" : Wrong_Inquiry,
        "Wrong_Inquiry_percentage"  : Wrong_Inquiry_percentage,
        "Solved" : Solved,
        "Solved_percentage" : Solved_percentage,
        "Follow_Up" : Follow_Up,
        "Follow_Up_percentage"  : Follow_Up_percentage,       
                
            }
    return render(request, 'Etbaly_Shokran/Etbaly_Shokran_Orders.html', context)


#____________________________________________________________________________

@login_required
def Melouk_Eltibah_invoice(request, id):
        obj = get_object_or_404(Melouk_Eltibah_Order, id=id)
        context={'order':obj}
        return render(request, 'Melouk_Eltibah/Melouk_Eltibah_invoice.html', context)



@login_required
def Melouk_Eltibah_order_list(request):
    # Retrieve all records from the database
    orders = Melouk_Eltibah_Order.objects.select_related("Customer").all().order_by("-id")
    # paginator = Paginator(orders, 100)
    # page_number = request.GET.get("page")
    # page_obj = paginator.get_page(page_number)
    # Render a template with the records
    Melouk_Eltibahorders = Melouk_Eltibah_Order.objects.all().count()
    Customers = Melouk_Eltibah_Customer.objects.all().count()
    Inquiries = Melouk_Eltibah_Inquiry.objects.all().count()
    FeedBacks = Melouk_Eltibah_FeedBack.objects.all().count()
    # Melouk_Eltibah(status)
    Return = int(Melouk_Eltibah_Order.objects.filter(Status__status='Return').count())
    Return_percentage  = (Return / Melouk_Eltibahorders) * 100
    Delivered = int(Melouk_Eltibah_Order.objects.filter(Status__status='Delivered').count())
    Delivered_percentage  = (Delivered / Melouk_Eltibahorders) * 100
    Cancel_Order = int(Melouk_Eltibah_Order.objects.filter(Status__status='Shipping').count())
    Cancel_Order_percentage  = (Cancel_Order / Melouk_Eltibahorders) * 100
    Progress = int(Melouk_Eltibah_Order.objects.filter(Status__status='Progress').count())
    Progress_percentage  = (Progress / Melouk_Eltibahorders) * 100
    Created = int(Melouk_Eltibah_Order.objects.filter(Status__status='Created').count())
    Created_percentage  = (Created / Melouk_Eltibahorders) * 100
    High_Price = int(Melouk_Eltibah_Order.objects.filter(Status__status='High_Price').count())
    High_Price_percentage  = (High_Price / Melouk_Eltibahorders) * 100
    Just_Ask = int(Melouk_Eltibah_Order.objects.filter(Status__status='Just_Ask').count())
    Just_Ask_percentage  = (Just_Ask / Melouk_Eltibahorders) * 100
    Follow_Up = int(Melouk_Eltibah_Order.objects.filter(Status__status='Follow_Up').count())
    Follow_Up_percentage  = (Follow_Up / Melouk_Eltibahorders) * 100
    New_Lead = int(Melouk_Eltibah_Order.objects.filter(Status__status='New_Lead').count())
    New_Lead_percentage  = (New_Lead / Melouk_Eltibahorders) * 100
    # Melouk_Eltibah(SourceChannel)
    Whatsapp = Melouk_Eltibah_Order.objects.filter(Source__Source='Whatsapp').count()
    Whatsapp_percentage  = (Whatsapp / Melouk_Eltibahorders) * 100
    Instagram = Melouk_Eltibah_Order.objects.filter(Source__Source='Instagram').count()
    Instagram_percentage  = (Instagram / Melouk_Eltibahorders) * 100
    Facebook = Melouk_Eltibah_Order.objects.filter(Source__Source='Facebook').count()
    Facebook_percentage  = (Facebook / Melouk_Eltibahorders) * 100
    # Melouk_Eltibah(inquiry_Status)
    Complaint = Dr_Print_Inquiry.objects.filter(inquiry__inquiry='Complaint').count()
    Complaint_percentage  = (Complaint / Melouk_Eltibahorders) * 100
    Order_Late = Dr_Print_Inquiry.objects.filter(inquiry__inquiry='Order_Late').count()
    Order_Late_percentage  = (Order_Late / Melouk_Eltibahorders) * 100
    # Melouk_Eltibah(Inquiry_Feedback)
    Wrong_Inquiry = Melouk_Eltibah_FeedBack.objects.filter(Status__inq_Feedback='Wrong_Inquiry').count()
    Wrong_Inquiry_percentage  = (Wrong_Inquiry / Melouk_Eltibahorders) * 100
    Solved = Melouk_Eltibah_FeedBack.objects.filter(Status__inq_Feedback='Solved').count()
    Solved_percentage  = (Solved / Melouk_Eltibahorders) * 100
    Follow_Up = Melouk_Eltibah_FeedBack.objects.filter(Status__inq_Feedback='Follow_Up').count()
    Follow_Up_percentage  = (Follow_Up / Melouk_Eltibahorders) * 100
    # Melouk_Eltibah(Inquiry_Feedback)
    context = {
        'orders': orders,
        'count':Melouk_Eltibahorders,
        "Customers" : Customers,
        "Inquiries" : Inquiries,
        "FeedBacks" : FeedBacks,
        # Melouk_Eltibah(status)
        "Return" : Return,
        "Return_percentage":Return_percentage,
        "Delivered" :Delivered,
        "Delivered_percentage"  : Delivered_percentage,
        "Cancel_Order" : Cancel_Order,
        "Cancel_Order_percentage"  : Cancel_Order_percentage,
        "Progress" : Progress,
        "Progress_percentage"  : Progress_percentage,
        "Created" :Created,
        "Created_percentage" :Created_percentage,
        "High_Price" : High_Price,
        "High_Price_percentage"   : High_Price_percentage,
        "Just_Ask" : Just_Ask,
        "Just_Ask_percentage" :Just_Ask_percentage,  
        "Follow_Up" : Follow_Up,
        "Follow_Up_percentage"  : Follow_Up_percentage,
        "New_Lead" :New_Lead,
        "New_Lead_percentage"  :New_Lead_percentage,
        # Melouk_Eltibah(SourceChannel)
        "Whatsapp" : Whatsapp,
        "Whatsapp_percentage"  :Whatsapp_percentage, 
        "Instagram" : Instagram,
        "Instagram_percentage"  : Instagram_percentage,
        "Facebook" : Facebook,
        "Facebook_percentage"  : Facebook_percentage,
        # Melouk_Eltibah(inquiry_Status)
        "Complaint":Complaint,   
        "Complaint_percentage" : Complaint_percentage,
        "Order_Late" : Order_Late, 
        "Order_Late_percentage" :Order_Late_percentage,
        # Melouk_Eltibah(Inquiry_Feedback)
        "Wrong_Inquiry" : Wrong_Inquiry,
        "Wrong_Inquiry_percentage"  : Wrong_Inquiry_percentage,
        "Solved" : Solved,
        "Solved_percentage" : Solved_percentage,
        "Follow_Up" : Follow_Up,
        "Follow_Up_percentage"  : Follow_Up_percentage,       
                
            }
    return render(request, 'Melouk_Eltibah/Melouk_Eltibah_Orders.html', context)







#______________________________________________________________________________

@login_required
def Print_Square_invoice(request, id):
        obj = get_object_or_404(Print_Square_Order, id=id)
        context={'order':obj}
        return render(request, 'Print_Square/Print_Square_invoice.html', context)
    
    
    
@login_required
def Print_Square_order_list(request):
    # Retrieve all records from the database
    orders = Print_Square_Order.objects.select_related("Customer").all().order_by("-id")
    # paginator = Paginator(orders, 100)
    # page_number = request.GET.get("page")
    # page_obj = paginator.get_page(page_number)
    # Render a template with the records
    Print_Squareorders = Print_Square_Order.objects.all().count()
    Customers = Print_Square_Customer.objects.all().count()
    Inquiries = Print_Square_Inquiry.objects.all().count()
    FeedBacks = Print_Square_FeedBack.objects.all().count()
    # Print_Square(status)
    Return = int(Print_Square_Order.objects.filter(Status__status='Return').count())
    Return_percentage  = (Return / Print_Squareorders) * 100
    Delivered = int(Print_Square_Order.objects.filter(Status__status='Delivered').count())
    Delivered_percentage  = (Delivered / Print_Squareorders) * 100
    Cancel_Order = int(Print_Square_Order.objects.filter(Status__status='Shipping').count())
    Cancel_Order_percentage  = (Cancel_Order / Print_Squareorders) * 100
    Progress = int(Print_Square_Order.objects.filter(Status__status='Progress').count())
    Progress_percentage  = (Progress / Print_Squareorders) * 100
    Created = int(Print_Square_Order.objects.filter(Status__status='Created').count())
    Created_percentage  = (Created / Print_Squareorders) * 100
    High_Price = int(Print_Square_Order.objects.filter(Status__status='High_Price').count())
    High_Price_percentage  = (High_Price / Print_Squareorders) * 100
    Just_Ask = int(Print_Square_Order.objects.filter(Status__status='Just_Ask').count())
    Just_Ask_percentage  = (Just_Ask / Print_Squareorders) * 100
    Follow_Up = int(Print_Square_Order.objects.filter(Status__status='Follow_Up').count())
    Follow_Up_percentage  = (Follow_Up / Print_Squareorders) * 100
    New_Lead = int(Print_Square_Order.objects.filter(Status__status='New_Lead').count())
    New_Lead_percentage  = (New_Lead / Print_Squareorders) * 100
    # Print_Square(SourceChannel)
    Whatsapp = Print_Square_Order.objects.filter(Source__Source='Whatsapp').count()
    Whatsapp_percentage  = (Whatsapp / Print_Squareorders) * 100
    Instagram = Print_Square_Order.objects.filter(Source__Source='Instagram').count()
    Instagram_percentage  = (Instagram / Print_Squareorders) * 100
    Facebook = Print_Square_Order.objects.filter(Source__Source='Facebook').count()
    Facebook_percentage  = (Facebook / Print_Squareorders) * 100
    # Print_Square(inquiry_Status)
    Complaint = Dr_Print_Inquiry.objects.filter(inquiry__inquiry='Complaint').count()
    Complaint_percentage  = (Complaint / Print_Squareorders) * 100
    Order_Late = Dr_Print_Inquiry.objects.filter(inquiry__inquiry='Order_Late').count()
    Order_Late_percentage  = (Order_Late / Print_Squareorders) * 100
    # Print_Square(Inquiry_Feedback)
    Wrong_Inquiry = Print_Square_FeedBack.objects.filter(Status__inq_Feedback='Wrong_Inquiry').count()
    Wrong_Inquiry_percentage  = (Wrong_Inquiry / Print_Squareorders) * 100
    Solved = Print_Square_FeedBack.objects.filter(Status__inq_Feedback='Solved').count()
    Solved_percentage  = (Solved / Print_Squareorders) * 100
    Follow_Up = Print_Square_FeedBack.objects.filter(Status__inq_Feedback='Follow_Up').count()
    Follow_Up_percentage  = (Follow_Up / Print_Squareorders) * 100
    # Print_Square(Inquiry_Feedback)
    context = {
        'orders': orders,
        'count':Print_Squareorders,
        "Customers" : Customers,
        "Inquiries" : Inquiries,
        "FeedBacks" : FeedBacks,
        # Melouk_Eltibah(status)
        "Return" : Return,
        "Return_percentage":Return_percentage,
        "Delivered" :Delivered,
        "Delivered_percentage"  : Delivered_percentage,
        "Cancel_Order" : Cancel_Order,
        "Cancel_Order_percentage"  : Cancel_Order_percentage,
        "Progress" : Progress,
        "Progress_percentage"  : Progress_percentage,
        "Created" :Created,
        "Created_percentage" :Created_percentage,
        "High_Price" : High_Price,
        "High_Price_percentage"   : High_Price_percentage,
        "Just_Ask" : Just_Ask,
        "Just_Ask_percentage" :Just_Ask_percentage,  
        "Follow_Up" : Follow_Up,
        "Follow_Up_percentage"  : Follow_Up_percentage,
        "New_Lead" :New_Lead,
        "New_Lead_percentage"  :New_Lead_percentage,
        # Melouk_Eltibah(SourceChannel)
        "Whatsapp" : Whatsapp,
        "Whatsapp_percentage"  :Whatsapp_percentage, 
        "Instagram" : Instagram,
        "Instagram_percentage"  : Instagram_percentage,
        "Facebook" : Facebook,
        "Facebook_percentage"  : Facebook_percentage,
        # Melouk_Eltibah(inquiry_Status)
        "Complaint":Complaint,   
        "Complaint_percentage" : Complaint_percentage,
        "Order_Late" : Order_Late, 
        "Order_Late_percentage" :Order_Late_percentage,
        # Melouk_Eltibah(Inquiry_Feedback)
        "Wrong_Inquiry" : Wrong_Inquiry,
        "Wrong_Inquiry_percentage"  : Wrong_Inquiry_percentage,
        "Solved" : Solved,
        "Solved_percentage" : Solved_percentage,
        "Follow_Up" : Follow_Up,
        "Follow_Up_percentage"  : Follow_Up_percentage,       
                
            }
    return render(request, 'Print_Square/Print_Square_Orders.html', context)


#______________________________________________________________________________

