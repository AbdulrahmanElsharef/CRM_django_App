from django.db import models
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# Melouk_Eltibah
from CRM_Data.models import  SourceChannel,Governorate,Order_Status,Order_Feedback,Designer,Item,inquiry_Status,Inquiry_Feedback


class Melouk_Eltibah_Customer(models.Model):
    Company=models.CharField(("Company"), max_length=100,unique=True)
    Client=models.CharField(("Client"), max_length=100)
    Phone_1=models.CharField(("Phone 1 "), max_length=11,unique=True)
    Phone_2=models.CharField(("Phone 2 "), max_length=11,null=True,blank=True,unique=True)
    Governorate = models.ForeignKey(Governorate,related_name='Melouk_Eltibah_Customer_city',on_delete=models.PROTECT)
    Address=models.TextField(("Address"), max_length=250)
    Email=models.CharField(("Email"), max_length=50 ,null=True,blank=True,unique=True)
    Note=models.CharField(("Note"), max_length=50,null=True,blank=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated= models.DateTimeField(auto_now=True)
    def __str__(self) :
        return f"""{self.Company}"""

    class Meta:
        verbose_name_plural ="Customers"
        
        
    def Orders(self):
        total = 0
        Orders = self.Melouk_Eltibah_order_customer.all()
        for order in Orders:
            total +=1
        return total

    #______________________________________________________________________________
       
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    # return "{0}--{1}".format(instance.customer, filename)
    return f"{instance.Customer}--order{instance.id}"


class Melouk_Eltibah_Order(models.Model):
    Sales = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, related_name='Melouk_Eltibah_Order_Sales',) 
    Customer = models.ForeignKey(Melouk_Eltibah_Customer,related_name='Melouk_Eltibah_order_customer',on_delete=models.PROTECT)
    Source=models.ForeignKey(SourceChannel,related_name='Melouk_Eltibah_order_Source',on_delete=models.PROTECT)
    Status=models.ForeignKey(Order_Status,related_name='Melouk_Eltibah_order_status',on_delete=models.PROTECT)
    Feedback=models.ForeignKey(Order_Feedback,related_name='Melouk_Eltibah_Order_Feedback',on_delete=models.PROTECT)
    Designer=models.ForeignKey(Designer,related_name='Melouk_Eltibah_order_Designer',on_delete=models.PROTECT)
    Design = models.FileField(upload_to=user_directory_path,null=True,blank=True)
    #Cash=models.IntegerField(("Cash"),default=0)
    Discount=models.IntegerField(("Discount"),default=0)
    Delivery=models.IntegerField(("Delivery"),default=0)
    Design_Fees=models.IntegerField(("Design_Fees"),default=0)
    Transfer=models.IntegerField(("Transfer"),default=0)
    Shipping = models.TextField(("Shipping"),max_length=250)
    Order_Note=models.CharField(("Note"), max_length=50,null=True,blank=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated= models.DateTimeField(auto_now=True)
        
    def __str__(self) :
        return f"""Order-{self.id}"""

    class Meta:
        verbose_name_plural ="Orders" 
             
            
    def Order_Total(self):
        total = 0
        Order_detail = self.Melouk_Eltibah_order_Detail.all()
        for order in Order_detail:
            total+=int(1)*int(order.Price)
        return total
    
    def Cost(self):
        cost = self.Order_Total()+int(self.Delivery)+int(self.Design_Fees)-int(self.Discount)-int(self.Transfer)
        return cost
    
    #def Net(self):
       # Total=self.Cost()-int(self.Transfer)-int(self.Cash)
        #return Total
    
    def ITEMS(self):
        total = 0
        Order_detail = self.Melouk_Eltibah_order_Detail.all()
        for order in Order_detail:
            total +=1
        return total

    
class Melouk_Eltibah_OrderDetail(models.Model):
    Order = models.ForeignKey(Melouk_Eltibah_Order,related_name='Melouk_Eltibah_order_Detail',on_delete=models.CASCADE)
    Item = models.ForeignKey(Item,related_name='Melouk_Eltibah_Item_Category',on_delete=models.PROTECT)
    Item_Name = models.TextField(("Item_Name"),max_length=250)
    Quantity = models.IntegerField(("Quantity"),default=0)
    Price = models.IntegerField(("Price"),default=0)
    Note=models.CharField(("Note"), max_length=50,null=True,blank=True)

    
    def __str__(self):
        return str(self.Order)

    class Meta:
        verbose_name_plural ="Order_Items"
        
    def Order_Total(self):
        order_total=int(self.Quantity)*int(self.Price)
        return order_total


#_______________________________________________________________________________

class Melouk_Eltibah_Inquiry(models.Model):
    Sales = models.ForeignKey(get_user_model(), on_delete=models.PROTECT,related_name='Melouk_Eltibah_Inquiry_Sales',) 
    Order = models.ForeignKey(Melouk_Eltibah_Order,related_name='Melouk_Eltibah_order_Inquiry',on_delete=models.PROTECT)
    inquiry =models.ForeignKey(inquiry_Status,related_name='Melouk_Eltibah_inquiry_Status',on_delete=models.PROTECT)
    Details= models.TextField(("Details"),max_length=250,)
    Created = models.DateTimeField(auto_now_add=True)
    Note=models.CharField(("Note"), max_length=50,default='No_Note')
    
    def __str__(self) :
        return f"""INQ-{self.id}"""

    class Meta:
        verbose_name_plural ="Inquiry"
        
        
      
#_______________________________________________________________________________

class Melouk_Eltibah_FeedBack(models.Model):
    Cus_Service = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, related_name='Melouk_Eltibah_FeedBack_Cus_Service',) 
    Inquiry = models.ForeignKey(Melouk_Eltibah_Inquiry,related_name='Melouk_Eltibah_FeedBack_Inquiry',on_delete=models.PROTECT)
    feedback= models.TextField(("FeedBack"),max_length=250)
    Status =models.ForeignKey(Inquiry_Feedback,related_name='Melouk_Eltibah_Inquiry_Feedback',on_delete=models.PROTECT)
    Created = models.DateTimeField(auto_now_add=True)
    note=models.CharField(("Note"), max_length=50,default='No_Note')
    
    def __str__(self):
        return str(self.Inquiry)

    class Meta:
        verbose_name_plural ="FeedBack"

    def order(self):
        order_id= self.Inquiry.Order
        return order_id
    
    def sales_(self):
        order_sales= self.Inquiry.Sales
        return order_sales
#_______________________________________________________________________________

