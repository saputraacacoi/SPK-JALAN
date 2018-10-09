from django.shortcuts import render, redirect, get_list_or_404
from django.views.generic import View
from django.http import HttpResponse
from django.contrib import messages
from orm.models import Alternatif
# Create your views here.

class ListAlternatifView(View):
    def get(self, request):
        template = 'alternatif/index.html'
        alternatif = Alternatif.objects.all()
        data = {
            
            'alternatif' : alternatif,
        }
        return render(request, template, data)