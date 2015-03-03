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
        form = self.form_class(request.POST, request.FILES)

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
            print request.GET
            member = Member.objects.get(id=member_id)
        except ObjectDoesNotExist:
            raise Http404

        if member.gender == 'g':
            foreground = Image.open('girl.png')
        else:
            foreground = Image.open('boy.png')
        background = Image.open('P3010313.png')
        background.paste(foreground, (0, 0), foreground)

        # Name
        prefix_name = Word.objects.get(id=17).text
        draw = ImageDraw.Draw(background)
        red = (0, 0, 0)
        #black = (0, 0, 0)
        text_pos = (140, 510)
        text = ' ' + prefix_name + ':    ' + member.nickname
        font = ImageFont.truetype('layijimahaniyom1.ttf', 27)
        draw.text(text_pos, text, fill=red, font=font)
        del draw

        # Birthdate
        born_text = Word.objects.get(id=14).text
        day = str(member.birthdate.day)
        month = Word.objects.get(id=member.birthdate.month).text
        year = str(member.birthdate.year)

        draw = ImageDraw.Draw(background)
        red = (0, 0, 0)
        #black = (0, 0, 0)
        text_pos = (138, 532)
        text = born_text + ':   ' + ' ' + day + ' ' + month + ' ' + year
        font = ImageFont.truetype('layijimahaniyom1.ttf', 27)
        draw.text(text_pos, text, fill=red, font=font)
        del draw

        # Dad and Mom
        prefix_parent = Word.objects.get(id=18).text
        prefix_dad_name = Word.objects.get(id=13).text
        prefix_mom_name = Word.objects.get(id=16).text

        draw = ImageDraw.Draw(background)
        red = (0, 0, 0)
        #black = (0, 0, 0)
        text_pos = (126, 557)
        text = prefix_parent + ':    ' + prefix_dad_name + member.dad_name + ' ' + prefix_mom_name + member.mom_name + " "
        font = ImageFont.truetype('layijimahaniyom1.ttf', 27)
        draw.text(text_pos, text, fill=red, font=font)
        del draw

        # Member Number
        #prefix_member_number = Word.objects.get(id=17).text

        draw = ImageDraw.Draw(background)
        white = (255, 255, 255)
        #black = (0, 0, 0)
        text_pos = (375, 380)
        #text = prefix_member_number + ' ' + str(member.id)
        text = '000' + str(member.id)
        font = ImageFont.truetype('layijimahaniyom1.ttf', 40)
        draw.text(text_pos, text, fill=white, font=font)
        del draw

        # branch
        prefix_branch = Word.objects.get(id=19).text
        draw = ImageDraw.Draw(background)
        red = (0, 0, 0)
        #black = (0, 0, 0)
        text_pos = (123, 580)
        text = ' ' + prefix_branch + ':    ' + member.province
        font = ImageFont.truetype('layijimahaniyom1.ttf', 27)
        draw.text(text_pos, text, fill=red, font=font)
        del draw

        response = HttpResponse(content_type='image/png')
        # now, we tell the image to save as a PNG to the
        # provided file-like object
        background.save(response, 'PNG')

        return response # and we're done!

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
