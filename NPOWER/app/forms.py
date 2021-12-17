from django import forms
from django.db.models import fields
from django.forms import ModelForm
from .models import ppleData

class dataForm(ModelForm):
    class Meta:
        model = ppleData
        fields = ("Surname", "Firstname", "Email", "Phone", "date_of_birth", "BVN", "address", "guarantor_name", "state_of_origin", "city", "school_degree")

        labels={
            "Surname":"Surname",
            "Firstname":"First Name",
            "Email":"Email Address",
            "Phone":"Phone Number",
            "date_of_birth":"Date Of Birth",
            "BVN":"BVN",
            "address":"Address",
            "guarantor_name":"Guarantor's Name",
            "state_of_origin":"State Of Origin",
            "city":"City",
            "school_degree":"Education Level",

                }
  
        widgets={
            "Surname":forms.TextInput(attrs={"class":"form-control", "placeholder":"Enter  Surname"}),
            "Firstname":forms.TextInput(attrs={"class":"form-control", "placeholder":"Enter  First Name"}),
            "Email":forms.EmailInput(attrs={"class":"form-control", "placeholder":"Enter  Email Address"}),
            "Phone":forms.TextInput(attrs={"class":"form-control", "placeholder":"Enter  Phone Contact"}),
            "date_of_birth":forms.TextInput(attrs={"class":"form-control", "placeholder":"Enter  Date Of Birth"}),
            "BVN":forms.TextInput(attrs={"class":"form-control", "placeholder":"Enter  Bank Verification Number"}),
            "address":forms.TextInput(attrs={"class":"form-control", "placeholder":"Enter  Address"}),
            "guarantor_name":forms.TextInput(attrs={"class":"form-control", "placeholder":"Enter  Guarantor's Name"}),
            "state_of_origin":forms.TextInput(attrs={"class":"form-control", "placeholder":"Enter  State Of Origin"}),
            "city":forms.TextInput(attrs={"class":"form-control", "placeholder":"Enter  City Name"}),
            "school_degree":forms.TextInput(attrs={"class":"form-control", "placeholder":"Enter  Highest School Certificate"}),
        }