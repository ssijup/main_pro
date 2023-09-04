from django.db import models

class Court(models.Model):
    name=models.CharField(max_length=200)
    type=models.CharField(max_length=200)
    estd_date = models.DateField(default='9999-99-99')
    address=models.CharField(max_length=200)
    contact_no=models.CharField(max_length=200)
    description=models.CharField(max_length=200)
    def __str__(self): 
        return self.name 

class Jurisdiction(models.Model):
    name=models.CharField(max_length=200)
    area=models.CharField(max_length=200)
    court=models.ForeignKey(Court, on_delete=models.CASCADE)
    def __str__(self): 
        return self.name 
    
class Association(models.Model):
    name=models.CharField(max_length=200)
    estd_date=models.DateField(default='9999-99-99')
    court=models.ForeignKey(Court, on_delete=models.CASCADE)
    address=models.CharField(max_length=200)
    website=models.CharField(max_length=200)
    contact_no=models.CharField(max_length=200)
    email=models.EmailField()
    is_suspend=models.BooleanField(default=False)


class MembershipPlan(models.Model):
    duration = models.IntegerField()
    unit_of_plan = models.CharField(max_length=20)
    membership_price = models.CharField(max_length=10 ,default='1')


class MembershipFineAmount(models.Model):
    fine_amount = models.IntegerField(default= 500)


class Notification(models.Model):
    association=models.ForeignKey(Association,on_delete=models.CASCADE, default=0)
    title=models.CharField(max_length=250)
    content=models.TextField()
    created_at=models.DateField(auto_now=True)


class AssociationMembershipPayment(models.Model):
    for_payment_plan =models.ForeignKey(MembershipPlan ,on_delete=models.SET_NULL ,null=True)
    for_user_details = models.ForeignKey('userapp.Advocate' ,on_delete= models.SET_NULL ,null = True,related_name='useradvocate')
    payment_id =models.CharField(max_length=200)
    payment_status = models.BooleanField(default = False)
    payment_done_at = models.DateField(auto_now_add= True)  
    payment_expiry_date = models.DateField(default='2020-07-20')
    payment_total_amount_paid = models.IntegerField(default=0)
    payment_status_of_gateway = models.CharField(max_length=25 ,default= 'failed')


class AssociationPaymentRequest(models.Model):
    payment_request_id = models.CharField(max_length=300)
    payment_requested_user = models.ForeignKey('userapp.Advocate',on_delete=models.CASCADE)
    payment_requested_plan = models.ForeignKey(MembershipPlan,on_delete=models.CASCADE)
    payment_expiry_date = models.DateField(default='2020-07-20')
    payment_total_amount_paid = models.IntegerField(default=0)

