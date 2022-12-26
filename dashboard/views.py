from django.shortcuts import render 

# Create views here
def index(request):
    return render(request, 'dashboard/index.html')