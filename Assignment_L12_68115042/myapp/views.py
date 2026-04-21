from django.shortcuts import render, redirect, get_object_or_404
from .models import Person

def home(request):
    all_person = Person.objects.all()
    return render(request, 'index.html', {'all_person': all_person})

def form(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")

        Person.objects.create(
            name=name,
            age=age
        )

        return redirect('/')
    
    return render(request, 'form.html')

def edit(request, person_id):
    person = get_object_or_404(Person, pk=person_id)

    if request.method == "POST":
        person.name = request.POST.get("name")
        person.age = request.POST.get("age")
        person.save()
        return redirect('/')
    
    return render(request, 'edit.html', {'person': person})

def delete(request, person_id):
    person = get_object_or_404(Person, pk=person_id)
    person.delete()
    return redirect('/')