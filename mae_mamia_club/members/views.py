from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic import TemplateView



class MemberAddView(TemplateView):
    def get(self, request):
        return HttpResponse()
