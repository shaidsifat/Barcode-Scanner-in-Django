from django import forms 
 
class SearchForm(forms.Form):  
    searchfield = forms.CharField(label="Enter barcode:",max_length=50)  
 