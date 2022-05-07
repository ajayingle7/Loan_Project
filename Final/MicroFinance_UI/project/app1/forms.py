from select import select
from django import forms
from app1.models import PreviousLoanDetails, OccupatinalDetails, BoccupationalDetails,Guranteer, Document, CurrentAddress, PermanentAddress,BankDetails
from django.contrib.auth.forms import UserCreationForm
from app1.models import User

class PreviousLoanDetailsForm(forms.ModelForm):
    class Meta:
        model=PreviousLoanDetails
        fields="__all__"
        widget={
            'open_date':forms.DateInput(
                attrs={
                    'type':'date'
                }
            ),
            'close_date':forms.DateInput(
                attrs={
                    'type':'date'
                }
            )
        }
        
class OccupationalDetailsForm(forms.ModelForm):
    class Meta:
        model = OccupatinalDetails
        fields = "__all__"
        labels = {
            'Experience': 'Years of Employment'
        }
        

class BoccupationalDetailsForm(forms.ModelForm):
    class Meta:
        model = BoccupationalDetails
        fields = "__all__"
        labels = {
            'Experience': 'Years in Bussiness'
        }

class GuranteerForm(forms.ModelForm):
    class Meta:
        model = Guranteer
        fields = "__all__"
        widget = {
            'Address_line_1':forms.TextInput(
                attrs={
                    'placeholder': 'eg.Building name,Lane number'
        
                }
            ),
            'Address_line_2':forms.TextInput(
                attrs={
                    'placeholder': 'eg.Area/Colony name'
                }
            ),
             'City':forms.TextInput(
                attrs={
                    'placeholder': 'eg.Pune'
                }
            ),
            
        }

class DocumentForm(forms.ModelForm):
    class Meta:
        model=Document
        fields="__all__"
        labels={
            'Salary_Slip':"Salary Slip(if salarized)",
            'form_16_OR_ITR':'Form No 16/ITR'
        }

class CurrentadrForm(forms.ModelForm):
    class Meta:
        model=CurrentAddress
        fields="__all__"

        labels={
           
            'flat_no':"FLAT NO",
            'street_name':"STREET NAME",
            'area':"AREA",
            'landmark':"LANDMARK",
            'city':"CITY",
            'district':"DISTRICT",
            'state':'STATE',
            'pincode':"PINCODE",
            'country':"COUNTRY"
            }
class PermanentadrForm(forms.ModelForm):
    class Meta:
        model=PermanentAddress
        fields="__all__"

        labels={
            
            'pflat_no':"FLAT NO",
            'pstreet_name':"STREET NAME",
            'parea':"AREA",
            'plandmark':"LANDMARK",
            'pcity':"CITY",
            'pdistrict':"DISTRICT",
            'pstate':'STATE',
            'ppincode':"PINCODE",
            'pcountry':"COUNTRY"
            }

class BankDetailForm(forms.ModelForm):
    class Meta:
        model=BankDetails
        fields="__all__"

        labels={
            
            'bank_name':"Bank Name",
            'accholder_name':'Account Holder Name',
            'acc_number':'Account Number',
            'confirm_acc_num':'Confirm Account Number',
            'Account_type':'Account Type',
            'ifsc_code':'IFSC Code',      
            'branch_name':'Branch Name',
            'branch_code':'Branch Code'
        }

class LoginForm(forms.Form):
    username = forms.CharField(
       widget = forms.TextInput(
            attrs={
                "class":"form-control"
            }
        )
    )
    password = forms.CharField(
       widget = forms.PasswordInput(
            attrs={
                "class":"form-control"
            }
        )
    )


user_choice = (
    ("isrmanager","isrmanager"),
    ("isomanager","isomanager"),
    ("iscustomer","iscustomer"),

)
class SignupForm(UserCreationForm):
    username = forms.CharField(
       widget = forms.TextInput(
            attrs={
                "class":"form-control"
            }
        )
    )
    password1 = forms.CharField(
       widget = forms.PasswordInput(
            attrs={
                "class":"form-control"
            }
        )
    )
    password2 = forms.CharField(
       widget = forms.PasswordInput(
            attrs={
                "class":"form-control"
            }
        )
    )
    email = forms.CharField(
       widget = forms.TextInput(
            attrs={
                "class":"form-control"
            }
        )
    )
    
    user = forms.ChoiceField(choices=user_choice)
    class Meta:
        model = User
        fields = ('username','email','password1','password2','isrmanager','isomanager','iscustomer')
        
   