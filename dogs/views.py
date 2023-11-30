from django.shortcuts import render, get_object_or_404
from dogs.models import Dog, Categories





def home(request):
    categories=Categories.objects.all()[:3]

    context = {
        'object_list': categories
    }

    return render(request, 'dogs/index.html', context)


def catalog(request):
    categories=Categories.objects.all()

    context = {
        'object_list': categories
    }

    return render(request, 'dogs/catalog.html', context)



def dog(request, pk):
    category = get_object_or_404(Categories, id=pk)
    dog_list = Dog.objects.filter(categories=category)
    context = {
        'object': dog_list,
        'category': category
    }
    return render(request, 'dogs/dog.html', context)

