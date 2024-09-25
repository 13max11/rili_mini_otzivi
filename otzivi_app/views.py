from django.shortcuts import render
from otzivi_app.models import Review

# Create your views here.

def reviews(request):
    reviews = Review.objects.all()
    context = {
        'reviews': reviews
    }
    return render(request=request, template_name='otzivi_app/index.html', context=context)