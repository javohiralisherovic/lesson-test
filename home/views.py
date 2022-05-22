import datetime
from django.http import HttpResponse
from django.shortcuts import redirect, render

from book_store.models import Book


# Create your views here.

def index(request):
    books = {'book_list': Book.objects.all()}
    return render(request, './index.html', context=books)

def contacts(request):
    html = """
        <h2>Biz bilan aloqa</h2>
        <strong>Tel: 99-087-45-54</strong><br>
        <strong>email: index@index.com</strong>
    """
    return HttpResponse(html)

def get_regions(request, id=None):
    if request.method == "GET":
        if 'name' in request.GET:
            searched_text = request.GET['name']
            html = ""
            for item in Region.objects():
                if searched_text.lower() in item.name.lower():
                    html += f'<a href={item.id}>{item.name}</a><br>'
            return HttpResponse(html)
    if id is not None:
        reg = Region.get_by_id(id)
        return HttpResponse(reg.name)
    else:
        html = "<a href='/regions/edit/'>Add</a> <br>"
        for item in Region.objects():
            html += f'<a href=edit/?id={item.id}>{item.name}</a><br>'
        return HttpResponse(html)

def edit_region(request):
    if request.GET:
        id = int(request.GET['id'])
        
        if 'name' in request.GET:
            name = request.GET['name']

            if id == 0:
                reg = Region(name)
                reg.save()
            else:
                reg = Region(name, id)
                reg.save()
            return redirect('/regions/')
        else:
            reg = Region.get_by_id(id)
            return render(request, 'reg-edit.html', context={'reg': reg})
    return render(request, 'reg-edit.html', context={'reg': ''})

def find_by_name(request, text):
    html = ""
    array = text.split('-')
    for item in Region.objects():
        if item.name in array:
            html += f'<a href={item.id}>{item.name}</a><br>'
    return HttpResponse(html)
