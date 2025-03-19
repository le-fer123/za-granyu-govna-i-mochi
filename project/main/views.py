import os

from django.http import FileResponse, Http404, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from .models import File


def index(request):
    return render(request, 'main/index.html')


def filegetview(request, url):
    file_obj = get_object_or_404(File, url=url)
    context = {'file': file_obj, 'is_File': True}

    if file_obj.content is None:
        context['is_file'] = False

    return render(request, 'main/filedet.html', context)

@csrf_exempt
def filepostview(request):
    if request.method == 'GET':
        return render(request, 'main/filepostview.html')
    title = request.POST.get('title', '')
    data = request.POST.get('data', '')
    try:
        uploaded_file = request.FILES['file']
    except:
        uploaded_file = None

    if uploaded_file:
        file_obj = File(title=title, content=uploaded_file, content_text=data)
    else:
        file_obj = File(title=title, content_text=data)

    try:
        file_obj.save()
    except:
        return HttpResponse('File with this title already exists')

    context = {'url': request.build_absolute_uri(file_obj.get_absolute_url()),}
    if file_obj.content is None:
        context['is_file'] = False
    return render(request, 'main/success_url.html', context)
