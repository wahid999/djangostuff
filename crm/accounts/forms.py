from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *

class CustomerForm(ModelForm):
	class Meta:
		model = Customer
		fields = '__all__'
		exclude = ['user']


class OrderForm(ModelForm):
	class Meta:
		model = Order
		fields = '__all__' #this will create all fields
		
		#fields = ['customer', 'product'] list is used for a few field to create
			
class createUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1','password2']
				
		