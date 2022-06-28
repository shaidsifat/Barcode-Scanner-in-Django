from urllib import request
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from products.models import Product,ProductDetails
from .forms import SearchForm  
from django.views.generic import TemplateView, ListView

def index(request):  
    
   
    student =  SearchForm()  
    print(student)
    return render(request,"index.html",{'form':SearchForm}) 

class HomePageView(TemplateView):
    template_name = 'home.html'

class SearchResultsView(ListView):
    model = ProductDetails
    template_name = "index.html"

    def get_queryset(self):  # new
        query = self.request.GET.get("q") 
        print(query)
        #query = self.request.query_params.get('q') 
        object_list = ProductDetails.objects.filter(barcode=query)
        print(object_list)
        return object_list
