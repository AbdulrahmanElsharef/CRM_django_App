from django.db import models

class Governorate(models.Model):
    Governorate = models.CharField(('Governorate'),max_length=50,unique=True)
    note=models.CharField(("Note"), max_length=50,null=True,blank=True)
    def __str__(self) :
        return f"""{self.Governorate}"""
    
    class Meta:
        verbose_name_plural ="City"
#_________________________________


class SourceChannel(models.Model):
    Source = models.CharField(('Source'),max_length=300,unique=True)
    note=models.CharField(("Note"), max_length=50,null=True,blank=True)
    def __str__(self) :
        return f"""{self.Source}""" 
    class Meta:
        verbose_name_plural ="Source"
#_________________________________


class Order_Status(models.Model):
    status = models.CharField(('Status'),max_length=300,unique=True)
    note=models.CharField(("Note"), max_length=50,null=True,blank=True)
    def __str__(self) :
        return f"""{self.status}"""    


    class Meta:
            verbose_name_plural ="Order_Status"
    #_________________________________
class Order_Feedback(models.Model):
    Feedback = models.CharField(('Feedback'),max_length=300,unique=True)
    note=models.CharField(("Note"), max_length=50,null=True,blank=True)
    def __str__(self) :
        return f"""{self.Feedback}"""    


    class Meta:
            verbose_name_plural ="Order_Feedback"
    #_________________________________
class Designer(models.Model):
    name=models.CharField(("Designer"), max_length=50,unique=True)
    note=models.CharField(("Note"), max_length=50,null=True,blank=True)

    def __str__(self) :
        return f"""{self.name}"""


    class Meta:
        verbose_name_plural ="Designer"
    #_________________________________    

class Item(models.Model):
    Item = models.CharField(('Item'),max_length=50,unique=True)
    note=models.CharField(("Note"), max_length=50,null=True,blank=True)
    def __str__(self) :
        return f"""{self.Item}"""
    
    class Meta:
        verbose_name_plural ="Items"
#___________________________________
class inquiry_Status(models.Model):
    inquiry = models.CharField(('Inquiry'),max_length=50,unique=True)
    note=models.CharField(("Note"), max_length=50,null=True,blank=True)
    def __str__(self) :
        return f"""{self.inquiry}"""
    
    class Meta:
        verbose_name_plural ="inquiry_Status"
#_________________________________
#___________________________________
class Inquiry_Feedback(models.Model):
    inq_Feedback = models.CharField(('inq_Feedback'),max_length=50,unique=True)
    note=models.CharField(("Note"), max_length=50,null=True,blank=True)
    def __str__(self) :
        return f"""{self.inq_Feedback}"""
    
    class Meta:
        verbose_name_plural ="Inquiry_Feedback"
#_________________________________




