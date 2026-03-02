from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    people = [
        {'name' : 'Riya Singh', 'age': 21},
        {'name' : 'Abhijeet Yadav', 'age': 24},
        {'name' : 'Abhishek Sharma', 'age': 26},
        {'name' : 'Rohan Singh', 'age': 15},
        {'name' : 'Shalak Nelson', 'age': 25}
    ]

    flowers = ['rose','mogra','sunflower','tulips']

    return render(request, "home/index.html", context= {'people':people, 'flowers':flowers})

def about(request):
    context = {'page': 'About'}
    return render(request, "home/about.html", context)

def contact(request):
    context = {'page': 'Contact'}
    return render(request, "home/contact.html", context)

def success_page(request):
    return HttpResponse("<h1>This is a Success Page</h1>.")

