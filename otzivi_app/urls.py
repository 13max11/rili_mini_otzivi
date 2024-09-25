from django.urls import path
from otzivi_app.views import reviews

urlpatterns = [
    path('', reviews, name='reviews')
]