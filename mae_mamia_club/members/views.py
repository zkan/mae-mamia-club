from PIL import Image, ImageDraw, ImageFont

from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.views.generic import TemplateView

from .forms import MemberForm
from .models import Member
from mappings.models import Word


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

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            member_id = form.save()

        return render(
            request,
            self.template,
            {
                'form': form,
                'member_id': member_id
            }
        )


class MemberView(TemplateView):
    def get(self, request):
        member_id = request.GET.get('id')

        try:
            member = Member.objects.get(id=member_id)
        except ObjectDoesNotExist:
            raise Http404

        background = Image.open('48G.jpg')
        foreground = Image.open('marble.png')
        background.paste(foreground, (250, 230), foreground)

        # Name
        prefix_name = Word.objects.get(id=13).text
        draw = ImageDraw.Draw(background)
        red = (255, 0, 0)
        #black = (0, 0, 0)
        text_pos = (195, 555)
        text = prefix_name + member.name
        font = ImageFont.truetype('layijimahaniyom1.ttf', 70)
        draw.text(text_pos, text, fill=red, font=font)
        del draw

        # Birthdate
        born_text = Word.objects.get(id=14).text
        day = str(member.birthdate.day)
        month = Word.objects.get(id=member.birthdate.month).text
        year = str(member.birthdate.year)

        draw = ImageDraw.Draw(background)
        red = (255, 0, 0)
        #black = (0, 0, 0)
        text_pos = (150, 610)
        text = born_text + ' ' + day + ' ' + month + ' ' + year
        font = ImageFont.truetype('layijimahaniyom1.ttf', 50)
        draw.text(text_pos, text, fill=red, font=font)
        del draw

        # Dad and Mom
        prefix_dad_name = Word.objects.get(id=15).text
        prefix_mom_name = Word.objects.get(id=16).text

        draw = ImageDraw.Draw(background)
        red = (255, 0, 0)
        #black = (0, 0, 0)
        text_pos = (230, 655)
        text = prefix_dad_name + member.dad_name + ' ' + prefix_mom_name + member.mom_name
        font = ImageFont.truetype('layijimahaniyom1.ttf', 35)
        draw.text(text_pos, text, fill=red, font=font)
        del draw

        # Member Number
        prefix_member_number = Word.objects.get(id=17).text

        draw = ImageDraw.Draw(background)
        red = (255, 0, 0)
        #black = (0, 0, 0)
        text_pos = (235, 690)
        text = prefix_member_number + ' ' + str(member.id)
        font = ImageFont.truetype('layijimahaniyom1.ttf', 50)
        draw.text(text_pos, text, fill=red, font=font)
        del draw

        response = HttpResponse(content_type='image/png')
        # now, we tell the image to save as a PNG to the
        # provided file-like object
        background.save(response, 'PNG')

        return response # and we're done!
