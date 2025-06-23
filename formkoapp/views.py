from urllib.request import Request
from django.http import HttpResponse
from django.shortcuts import render, redirect
from formkoapp.forms import AddForm,FetchForm
from formkoapp.models import FormData

def options(request):
    return render(request,'formkoapp/options.html')

def form(request,type):
    if (type=='ADD' or type=='UPDATE'):
        form=AddForm()
        return render(request,'formkoapp/form.html',{'form':form,'type':type})
    else:
        form=FetchForm()
        return render(request,'formkoapp/form.html',{'form':form,'type':type})


def submission(request,fetch_all):
    if fetch_all=='true':
        person = FormData.objects.all()
        return render(request, 'formkoapp/fetched.html', {'person': person})

    else:
        action = request.POST.get('action')
        if action == 'FETCH':
            name = request.POST.get('name')
            person = FormData.objects.filter(name__iexact=name)
            return render(request, 'formkoapp/fetched.html', {'person': person})

        elif action == 'ADD':
            form = AddForm(request.POST)
            if form.is_valid():
                form.save()
                return render(request, 'formkoapp/submitted.html')
            return HttpResponse("form isn't valid!")
        elif action == 'DELETE':
            name = request.POST.get('name')
            FormData.objects.filter(name__iexact=name).delete()
            return render(request, 'formkoapp/deleted.html')

        else:
            name = request.POST.get('name')
            new_age = request.POST.get('age')
            new_sex = request.POST.get('sex')
            FormData.objects.filter(name__iexact=name).update(age=new_age, sex=new_sex)
            return render(request, 'formkoapp/updated.html', {'name': name})

    return HttpResponse('no method is selected!')


def submitted(request):
    return render(request, 'formkoapp/submitted.html')
