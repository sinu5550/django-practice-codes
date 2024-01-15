from django.urls import path,include
from . import views
app_name='album'
urlpatterns = [
    path('add/',views.AddAlbumCreateView.as_view(),name='add_album' ),
    path('edit/<int:id>',views.EditAlbumView.as_view(),name='edit_album' ),
    path('delete/<int:id>',views.DeleteAlbumView.as_view(),name='delete_album' ),
]