from django.urls import path
from react_backend import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('upload-csv/', views.upload_csv, name='upload_csv'),
    path('get-filtered-data/', views.get_filtered_data, name='get-filtered-data'),
]