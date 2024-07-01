from django import forms
from .models import Product


class UserForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    age = forms.IntegerField(min_value=0, max_value=120)


class ImageForm(forms.Form):
    image = forms.ImageField()


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'quantity', 'photo']

# class ManyFieldsForm(forms.Form):
#     name = forms.CharField(max_length=50)
#     email = forms.EmailField()
#     age = forms.IntegerField(min_value=18)
#     height = forms.FloatField()
#     is_active = forms.BooleanField(required=False)
#     birthdate = forms.DateField(initial=datetime.date.today)
#     gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')])
