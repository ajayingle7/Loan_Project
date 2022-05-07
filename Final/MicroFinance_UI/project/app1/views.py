from django.shortcuts import render, redirect
from .models import Enquiry, PersonalDetail, BankDetails, PreviousLoanDetails, Guranteer, Document
from app1.forms import PreviousLoanDetailsForm,OccupationalDetailsForm,BoccupationalDetailsForm, GuranteerForm,DocumentForm,CurrentadrForm, PermanentadrForm,BankDetailForm,SignupForm,LoginForm
from django.conf import settings
from django.core.mail import send_mail 
from django.contrib import messages
from random import randint
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import random

otp = randint(1000,9999)


def index(request):
    return render(request, 'home/home.html')



def enquiryView(request):
    template_name = 'app1/enquiry.html'
    context = {}
    if request.method == 'POST':
        fn = request.POST.get('fn')
        mail = request.POST.get('mail')
        mob = request.POST.get('contact')
        city = request.POST.get('city')
        pan = request.POST.get('pan')
        amt = request.POST.get('amount')
        income = request.POST.get('income')
        tenure = request.POST.get('tenure')
        enq = Enquiry(fullname=fn,mail=mail,mob=mob,city=city,pan_no=pan,loan_amt=amt,income=income,tenure=tenure)
        enq.save()
        email = request.POST.get('mail')
        subject = 'OTP for Loan Application'
        message = f'Hello, Welcome to B25 Micro-Finance Bank. You have applied for loan enquiry. Your OTP is {otp}'
        email_from = 'settings.EMAIL_HOST_USER'
        recipients_list = [email]
        send_mail(subject, message, email_from, recipients_list)


        return redirect('verifyurl')
    return render(request, template_name, context)

def showEnquiryView(request):
    template_name = 'app1/showenquiry.html'
    obj = Enquiry.objects.all()
    context = {'obj': obj}
    return render(request, template_name, context)

def personalDetailView(request):
    template_name = 'app1/personaldetail.html'
    context = {}
    if request.method == 'POST':
        fn = request.POST.get('fn')
        mn = request.POST.get('mn')
        ln = request.POST.get('ln')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        ms = request.POST.get('mstatus')
        sn = request.POST.get('spname')
        adhar = request.POST.get('adhar')
        pan = request.POST.get('pan')
        mob1 = request.POST.get('mob1')
        mob2 = request.POST.get('mob2')
        mail = request.POST.get('mail')
        pers = PersonalDetail(fname=fn,mname=mn,lname=ln,dob=dob,gender=gender,marital_status=ms,spouse_name=sn,adhar_no=adhar,pan_no=pan,mob1=mob1,mob2=mob2,mail=mail)
        pers.save()
        return redirect('addressurl')
    return render(request, template_name, context)

def showPersonalDetailView(request):
    template_name = 'app1/showpersonaldetail.html'
    obj = PersonalDetail.objects.all()
    context = {'obj': obj}
    return render(request, template_name, context)

def Pre_Loan_DetaildView(request):
    form=PreviousLoanDetailsForm()
    template_name="app1/preloandetails.html"
    context={'form':form}
    if request.method=='POST':
        form=PreviousLoanDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('confirmurl')
        
    return render(request,template_name,context)

def occupation(request):
    form = OccupationalDetailsForm()
    template_name = "app1/occupation.html"
    
    if request.method == "POST":
        form = OccupationalDetailsForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect ('guaranteerurl')
    context = {'form':form}
    return render(request, template_name, context)

def boccupation(request):
    form = BoccupationalDetailsForm()
    template_name = "app1/boccupation.html"
    
    if request.method == "POST":
        form = BoccupationalDetailsForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect ('guaranteerurl')
    context = {'form':form}
    return render(request, template_name, context)

def confirm(request):
    template_name = 'app1/confirm.html'
    context = {}
    return render(request, template_name, context)

def lconfirm(request):
    template_name = 'app1/lconfirm.html'
    context = {}
    return render(request, template_name, context)

def guaranteer(request):
    form = GuranteerForm()
    template_name = "app1/guaranteer.html"
    
    if request.method == "POST":
        form = GuranteerForm(request.POST,request.FILES )
        if form.is_valid():
            form.save()
            return redirect ('documenturl')
    context = {'form':form}
    return render(request, template_name, context)

def Document_uploadView(request):
    form=DocumentForm()
    if request.method=='POST':
        form=DocumentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        
    return render(request,"app1/document.html",{'form':form})

def addressView(request):
    cform=CurrentadrForm()
    pform=PermanentadrForm()
    print(cform,'---',pform)
    template_name='app1/address.html'
    context={'cform':cform,'pform':pform}
    if request.method =="POST":
       cform=CurrentadrForm(request.POST)
       pform=PermanentadrForm(request.POST)
       if cform.is_valid and pform.is_valid:
            cform.save()
            pform.save()
            return redirect ('bankurl')
    return render(request,template_name, context)


def twostepView(request):
    template_name = "app1/twostep.html"
    context = {}
    if request.method=="POST":
        otp1 = request.POST.get("otp")
        otp2 = int(otp1)

        if otp2 == otp:
            return redirect("personaldetailurl")
        else:
            messages.error(request,"invalid otp")

    return render(request,template_name,context)

@login_required()
def bankdetailfView(request):
    form=BankDetailForm()
    template_name='app1/bank.html'
    context={'form':form}
    if request.method=="POST":
        form=BankDetailForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('lconfirmurl')
    return render(request,template_name,context)

def register(request):
    msg = None
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect ('loginurl')
        else:
            msg = 'form is not valid'
    else:
        form = SignupForm()
    return render(request, 'app1/register.html',{'form':form, 'msg':msg})

def login_view(request):
    form = LoginForm()
    msg = None
    template_name = "app1/login.html"
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.iscustomer:
                login(request,user)
                return redirect ('homeurl')
            if user is not None and user.isrmanager:
                login(request,user)
                return redirect ('rmanagerurl')
            if user is not None and user.isomanager:
                login(request,user)
                return redirect ('omanagerurl')
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, template_name, {'form':form, 'msg':msg})

def logoutView(request):
    logout(request)
    return redirect('loginurl')

def home(request):
    return render(request, 'app1/customer.html')

@login_required()
def rmanager(request):
    obj = Enquiry.objects.all()
    num = random.randint(1000,9999)

    context = {'obj':obj,'num':num}
    return render(request, 'app1/rmanager.html',context)

@login_required()
def omanager(request):
    obj = Enquiry.objects.all()
    num = random.randint(1000,9999)
    obj1 = PersonalDetail.objects.all()
    obj2 = BankDetails.objects.all()
    obj3 = PreviousLoanDetails.objects.all()
    obj4 = Guranteer.objects.all()
    doc = Document.objects.all()
    context = {'obj':obj,'num':num,'obj1':obj1,'obj2':obj2,"obj3":obj3,'obj4':obj4,'doc':doc}
    return render(request, 'app1/omanager.html',context)

def submission(request):
    template_name = 'app1/submission.html'
    return render(request, template_name)


def success(request,mail):
    template_name = 'app1/success.html'
    context = {}
    subject = "Loan Status"
    message = "Your Loa is Approved"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [mail, ]

    send_mail(subject, message, email_from, recipient_list)
    return render(request, template_name,context)



def deleteView(request,id):
    template_name = "app1/deleteconfirm.html"
    obj = Enquiry.objects.get(id=id)
    context = {"data":obj}

    if request.method=="POST":
        obj.delete()

        return redirect("rmanagerurl")
    return render(request,template_name,context)


def deleteView1(request,mail):
    template_name = "app1/deleteconfirm1.html"
    obj1 = Enquiry.objects.get(mail=mail)
    context = {"data":obj1}

    if request.method=="POST":
        obj1.delete()

        subject = "Loan Status"
        message = "Your Loan IS Not Approved"
        email_from  = settings.EMAIL_HOST_USER
        recipient_list = [mail,]


        send_mail(subject,message,email_from,recipient_list)


        return redirect("omanagerurl")

    return render(request,template_name,context)
