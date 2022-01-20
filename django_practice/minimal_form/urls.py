from django.urls import path
from .views import homeView, infoViewer, viewForm
urlpatterns = [
    path('',homeView,name='forms_index'),
    path('form/',viewForm,name='view_form'),
    path('displaydata/',infoViewer,name='display_data')
    
]
