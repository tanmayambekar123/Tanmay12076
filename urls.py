from django.urls import path
from mycar import views
urlpatterns = [
    path('', views.all_data),
   # path('all_data',views.all_data),
]
