from django.contrib import admin  
from django.urls import path,include  
from products.views import SearchResultsView,HomePageView
urlpatterns = [  
    path('admin/', admin.site.urls),  
    path('home/',HomePageView.as_view(), name="home"),
    path('index/', SearchResultsView.as_view(),name='search_results'),  
]   

