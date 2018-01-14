import os
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def mysum(request, numbers):
    result = sum(map(lambda s: int(s or 0), numbers.split('/')))
    return HttpResponse(result)

def hello(request, name, age):
    return HttpResponse('안녕하세요. {}님, {}살이시네요.'.format(name, age))

def post_list1(request):
    name = '공유'
    return HttpResponse('''
<h1>Ask Django</h1>
<p>{name}</p>
<p>여러분의 파이썬&장고 페이스메이커가 되겠습니다.</p>
'''.format(name = name))

def post_list2(request):
    name='공유'
    response = render(request, 'dojo/post_list.html', {'name':name})
    return response

def excel_download(request):
    # filepath = './크린토피아요금표.xls
    filepath = os.path.join(settings.BASE_DIR, '크린토피아요금표.xls')
    filename = os.path.basename(filepath)

    with open(filepath,'rb') as f:
        response = HttpResponse(f, content_type = 'application/vnd.ms-excel')
        t = 'attachment; filename="{}"'.format(filename)
        response['Content-Disposition'] = t

    return response
