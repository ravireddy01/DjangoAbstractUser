from django.contrib import admin
from django.urls import path
from .views import CustomUser1ListView


urlpatterns = [
    #path('admin/', admin.site.urls),
    path('customlist/',CustomUser1ListView.as_view()),
    path('customlist/<int:id>/',CustomUser1ListView.as_view()),
    #path('customuser1list/',CustomUser1ListView.as_view()),
]
