from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *

# Create your views here.
def recipes(request):
    if request.method == "POST":
        data = request.POST
        
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        recipe_image = request.FILES.get('recipe_image')

        Recipes.objects.create(
            recipe_name = recipe_name,
            recipe_description = recipe_description,
            recipe_image = recipe_image)

        return redirect('/recipes/')
    search = request.GET.get('search')

    if search:
        queryset = Recipes.objects.filter(
            recipe_name__icontains=search
        ).order_by('recipe_name')
    else:
        queryset = Recipes.objects.all()

    context = {
        'recipes': queryset,
        'search': search
    }

    return render(request, 'recipes.html', context)


def update_recipe(request, id):
    queryset = Recipes.objects.get(id=id)

    if request.method == "POST":
        recipe_name = request.POST.get('recipe_name')
        recipe_description = request.POST.get('recipe_description')
        recipe_image = request.FILES.get('recipe_image')

        queryset.recipe_name = recipe_name
        queryset.recipe_description = recipe_description

        # update image only if new image uploaded
        if recipe_image:
            queryset.recipe_image = recipe_image
        queryset.save()
        return redirect('/recipes/')

    context = {'recipe': queryset}
    return render(request, 'update_recipes.html', context)

def delete_recipe(request,id):
    queryset = Recipes.objects.get(id=id)
    queryset.delete()
    return redirect('/recipes/')
