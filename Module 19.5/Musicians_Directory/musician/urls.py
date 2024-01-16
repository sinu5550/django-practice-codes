from django.urls import path,include
from . import views

app_name='musician'
urlpatterns = [
    
    path('add/',views.AddMusicianCreateView.as_view(),name='add_musician' ),
    path('edit/<int:id>',views.EditMusicianView.as_view(),name='edit_musician' ),
]