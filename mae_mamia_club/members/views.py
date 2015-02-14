from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from .forms import MemberForm


class MemberAddView(TemplateView):
    form_class = MemberForm
    template = 'member_add.html'

    def get(self, request):
        form = self.form_class()

        return render(
            request,
            self.template,
            {
                'form': form
            }
        )
