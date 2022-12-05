from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'petsitter'

urlpatterns = [
    path('', views.getloc, name='getloc'),
    path('send/', views.send, name='send'),
    path('upload/', views.uploadFile, name='upload'),
    #path('test/', views.practice, name='test'),
    path('download/', views.downloadFile, name='down'),
    path('videolist/', views.videoList, name='video'),
    path('petimg/', views.uploadPetImage, name='pet')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)