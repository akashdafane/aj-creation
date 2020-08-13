from django.shortcuts import render
from .forms import Inputform
from django.contrib import messages


# Create your views here.

def index(request):
    return render(request, 'html/index.html')

def aboutme(request):
    return render(request, 'html/About-Me.html')
#
def aboutus(request):
    return render(request, 'html/About-Us.html')
#
def contact(request):
    fm = Inputform()
    if request.method == 'POST':
        fm = Inputform(request.POST)
        if fm.is_valid():
            messages.success(request, 'Feedback Submitted!')

            fm.save(commit=True)
            # messages.error(request,'we will contact soon')

    return render(request, 'html/contact.html', {'form': fm})
#
def fashion(request):
    return render(request, 'html/fashion.html')
#
def gallery(request):
    return render(request, 'html/gallery.html')
#
def night(request):
    return render(request, 'html/night.html')
#
def portrait(request):
    return render(request, 'html/portrait.html')
#
def prebabyshoot(request):
    return render(request, 'html/pre-babyshoot.html')
#
def preweddingshoot(request):
    return render(request, 'html/pre-wedding.html')
#
def Pricingpackage(request):
    return render(request, 'html/Pricing-package.html')
#
def wedding(request):
    return render(request, 'html/wedding.html')

# def showUserData(request):
#     return render(request, )