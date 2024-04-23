from django.shortcuts import render

def blogs_page(request):
    return render(request, 'blogs_page.html')
