from tkinter import CASCADE
from django.db import models
from django.core.validators import RegexValidator
from indian_cities.dj_city import cities
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Enquiry(models.Model):
    fullname = models.CharField(max_length=100,null=True)
    mail = models.EmailField()
    mob = models.IntegerField()
    city = models.CharField(max_length=50)
    pan_no = models.CharField(max_length=10)
    loan_amt = models.IntegerField()
    income = models.FloatField()
    tenure = models.IntegerField()

class PreviousLoanDetails(models.Model):
    MY_CHOICES=(
        ("Home Loan","Home Loan"),
        ("Vehical Loan","vehical Loan"),
        ("Personal Loan","Personal Loan"),
        ("Gold Loan","Gold Loan"),
        ("Buisness Loan","Buisness Loan")
    )
    loan_type=models.CharField(max_length=40,choices=MY_CHOICES)
    loan_amt=models.FloatField()
    loan_account_no=models.CharField(max_length=100)
    financing_Bank=models.CharField(max_length=300)
    Tenure=models.CharField(max_length=40)
    Monthly_EMI=models.FloatField()
    open_date=models.DateField()
    close_date=models.DateField()


class PersonalDetail(models.Model):
    adhar_no = models.IntegerField(primary_key=True)
    fname = models.CharField(max_length=50)
    mname = models.CharField(max_length=50,)
    lname = models.CharField(max_length=50,)
    dob = models.DateField()
    gender = models.CharField(max_length=10,)
    marital_status = models.CharField(max_length=10)
    spouse_name = models.CharField(max_length=50, blank=True, null=True)
    pan_no = models.CharField(max_length=10)
    mob1 = models.IntegerField(null=True)
    mob2 = models.IntegerField(blank=True, null=True)
    mail = models.EmailField()

    def _str_(self):
        return f'{self.fname} {self.lname}'

class OccupatinalDetails(models.Model):
    TYPES = (
        ('Public company', 'Public company'),
        ('Private company', 'Private company'),
        ('companies limited by Guarantee', 'companies limited by Guarantee'),
        ('Unlimited companies', 'Unlimited companies')
    )
    AAdhar = models.OneToOneField(PersonalDetail, on_delete=models.CASCADE)
    Company_type = models.CharField(max_length=100,choices=TYPES, default=None,)
    Company_name = models.CharField(max_length=100)
    Company_address = models.CharField(max_length=100)
    EMPLOYEMENT = (
        ('Full Time', 'Full Time'),
        ('Part time', 'Part time'),
        ('Goverment Employee', 'Goverment Employee'),
    )
    Employement_type = models.CharField(max_length=100,choices=EMPLOYEMENT, default=None,)
    Experience = models.IntegerField()
    

    def __str__(self):
        return self.Company_name

class BoccupationalDetails(models.Model):
    AAdhar = models.OneToOneField(PersonalDetail, on_delete=models.CASCADE)
    Firm_type = models.CharField(max_length=100)
    Firm_name = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)
    Profile = models.CharField(max_length=100)
    Experience = models.IntegerField()

    def __str__(self):
        return self.Firm_name

class Guranteer(models.Model):
    AAdhar = models.ForeignKey(PersonalDetail, on_delete=models.CASCADE)
    Full_name = models.CharField(max_length=100)
    RELATION = (
        ('Friend', 'Friend'),
        ('Family Member', 'Family Member'),
        ('Bussiness Partner', 'Bussiness Partner'),
        ('others', 'others')
    )
    Relation_with_client = models.CharField(max_length=100,choices=RELATION, default=None,)
    Date_of_Birth = models.DateField(max_length=8)
    Contact = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])
    Email = models.EmailField()
    Address_line_1 = models.CharField(max_length=400)
    Address_line_2 = models.CharField(max_length=400)
    City = models.CharField(max_length=50)
    State = models.CharField(max_length=50, null=True)
    Pincode = models.IntegerField(null=True)
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others')
    )
    Gender = models.CharField(max_length=50, choices=GENDER, default=None, null=True)
    TYPE = (
        ('Public company', 'Public company'),
        ('Private company', 'Private company'),
        ('companies limited by Guarantee', 'companies limited by Guarantee'),
        ('Unlimited companies', 'Unlimited companies')
    )
    Occupation = models.CharField(max_length=50, choices=TYPE, default=None, null=True)
    Passport_photo = models.FileField(default=None,null=True)
    PAN_Card = models.FileField(default=None,null=True)
    Aadhar =  models.FileField(default=None,null=True)

    def __str__(self):
        return self.Email

class Document(models.Model):
    AAdhar = models.OneToOneField(PersonalDetail, on_delete=models.CASCADE)
    Pass_Port_size_Photo=models.FileField(default=None,null=True)
    Adhar_Card=models.FileField(default=None,null=True)
    Pan_Card=models.FileField(default=None,null=True)
    Bank_Statement=models.FileField(default=None,null=True)
    Bank_NOC=models.FileField(default=None,null=True)
    Salary_Slip=models.FileField(default=None,null=True)
    form_16_OR_ITR=models.FileField(default=None,null=True)
    signature=models.FileField(default=None,null=True)

class CurrentAddress(models.Model):
    AAdhar = models.OneToOneField(PersonalDetail, on_delete=models.CASCADE)
    flat_no=models.CharField(max_length=30)
    street_name=models.CharField(max_length=30)
    area=models.CharField(max_length=20)
    landmark=models.CharField(max_length=20)
    city=models.CharField(max_length=20,choices=cities,null=False)
    district=models.CharField(max_length=20)
    state=models.CharField(max_length=15)
    pincode=models.IntegerField()
    country=models.CharField(max_length=15)

    def __str__(self):
        return f'{self.flat_no},{self.street_name},{self.area},{self.landmark},{self.city},{self.district},{self.state},{self.pincode},{self.country}'

class PermanentAddress(models.Model):
    pflat_no=models.CharField(max_length=30)
    pstreet_name=models.CharField(max_length=30)
    parea=models.CharField(max_length=20)
    plandmark=models.CharField(max_length=20)
    pcity=models.CharField(max_length=20,choices=cities,null=False)
    pdistrict=models.CharField(max_length=20)
    pstate=models.CharField(max_length=15)
    ppincode=models.IntegerField()
    pcountry=models.CharField(max_length=15)

    def __str__(self):
        return f'{self.pcust_name},{self.pflat_no},{self.pstreet_name},{self.parea},{self.plandmark},{self.pcity},{self.pdistrict},{self.pstate},{self.ppincode},{self.pcountry}'
    

class BankDetails(models.Model):
    AAdhar = models.OneToOneField(PersonalDetail, on_delete=models.CASCADE, null=True)
    bank_name=models.CharField(max_length=20)
    accholder_name=models.CharField(max_length=25)
    acc_number=models.IntegerField()
    confirm_acc_num=models.IntegerField()
    account_type=(

            ("SavingsAccount","SavingsAccount"),
            ("CurrentAccount","CurrentAccount"),
            ("SalaryAccount","SalaryAccount"),
            ("NRI_Account","NRI_Account"),
            ("RD_Account","RD_Account"),
            ("FD_Account","FD_Account"),
            )
    Account_type=models.CharField(max_length=25,choices=account_type)
    ifsc_code=models.CharField(max_length=25)
    branch_name=models.CharField(max_length=25)
    branch_code=models.CharField(max_length=20)

    def __str__(self):
        return f'{self.bank_name},{self.accholder_name},{self.acc_number},{self.confirm_acc_num},{self.Account_type},{self.ifsc_code},{self.branch_name},{self.branch_code}'

class User(AbstractUser):
    isrmanager = models.BooleanField('if relational manager',default=False)
    isomanager = models.BooleanField('if operational manager',default=False)
    iscustomer = models.BooleanField('if customer',default=False)
