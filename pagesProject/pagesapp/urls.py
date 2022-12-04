from django.urls import path
from .views import HomePageView, AboutViews, BasePageView

urlpatterns = [
    path('',HomePageView.as_view(), name = 'home'),
    path('about/',AboutViews.as_view(), name = 'about'),
    path('index/', BasePageView.as_view(), name = "index")
]