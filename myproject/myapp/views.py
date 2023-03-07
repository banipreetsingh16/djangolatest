from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse,Http404
from myapp.forms import DataBaseForm
from myapp.models import DataBase
# Create your views here.

def create_database(request):
    form = DataBaseForm()
    if request.method == 'POST':
        form = DataBaseForm(request.POST)
        if form.is_valid():
            form.save()
            # data = form.save()
            # data.is_published = True
            # data.save()
    # return render(request, 'create.html', {'form': data})
    return render(request, 'create.html', {'form':form})
def list_database(request):
    data = DataBase.objects.all()
    return render(request, 'list.html', {'data': data})


def update_database(request, **kwargs):
    context = {}
    form = DataBaseForm()
    if request.method == 'POST':
        if pk:= kwargs.get('pk'):
            obj = DataBaseForm.objects.get(pk=pk)
            form = DataBaseForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                context['form'] = form
                HttpResponseRedirect('/demo/list')
    return render(request, 'update.html' ,context)

def delete_database(request, **kwargs):
    error_message = ""
    # import pdb; pdb.set_trace()
    if pk := kwargs.get('pk'):
        try:
            data = DataBase.objects.get(pk=pk)  #(database pk, request pk) and blog here is primary key
            data.delete()
        except Exception as e:
            error_message = "Blog does not exist."
    data = DataBase.objects.all()
    return render(request, 'list.html',{'data':data})
