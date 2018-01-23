from django.shortcuts import render
from django import forms
from django.http import HttpResponse
import json
from work.models import UpFile
# Create your views here.


def login(request):
    return render(request, 'index.html')


class UpFiles(forms.Form):
    upfile = forms.FileField()


def upload(request):
    if request.method == "POST":
        up = UpFiles(request.POST, request.FILES)
        cc = UpFile(up_file=request.FILES['file'])
        cc.save()
        url = 'http://127.0.0.1/' + str(cc.up_file)
        resp = {'success':1,'message': "6666",'url': url}
        return HttpResponse(json.dumps(resp), content_type="application/json")
    else:
        resp = {'success': 0, 'message': "error meth"}
        return HttpResponse(json.dumps(resp), content_type="application/json")


