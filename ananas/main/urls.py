from django.urls import path
from .views import ServerTimeView

app_name = 'main'
urlpatterns = [
    path('', ServerTimeView.as_view(), name="index")
]