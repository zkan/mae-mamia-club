from PIL import Image, ImageDraw, ImageFont

from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.views.generic import TemplateView

from .forms import MemberForm, MemberGenerateImageForm
from .models import Member
from mappings.models import Word

import StringIO
from django.core.files.uploadedfile import InMemoryUploadedFile


class MemberAddView(TemplateView):
    form_class = MemberForm
    template = 'member_add.html'

    def get(self, request):
        form = self.form_class()

        return render(
            request,
            self.template,
            {
                'form': form,
                'root_url': request.get_host(),
                'members': Member.objects.all()
            }
        )

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        #member_id = 'None'
        if form.is_valid(): 
            member = form.save()
            member_id = member.id
            obj = Member.objects.get(id=member_id)
            obj.image.save('kid_images/'+str(member_id)+'.png', obj.image, save=True)
        else:
            raise Error("form is not valid")
        

        return render(
            request,
            self.template,
            {
                'form': self.form_class(),
                'member_id': member_id,
                'root_url': request.get_host(),
            }
        )


class MemberView(TemplateView):

    def get(self, request):
        member_id = request.GET.get('id')

        try:
            member = Member.objects.get(id=member_id)
        except ObjectDoesNotExist:
            raise Http404

        if member.gender == 'g':
            foreground = Image.open('girl.png')
        else:
            foreground = Image.open('boy.png')
        background = Image.open(member.image)

        
        #crop to width = 600
        width, height = background.size   # Get dimensions
        basewidth = 600
        wpercent = (basewidth / float(background.size[0]))
        hsize = int((float(background.size[1]) * float(wpercent)))
        background = background.resize((basewidth, hsize), Image.ANTIALIAS)

        background.info["dpi"] = (72, 72)
    
        #crop (left, top, right, bottom)
        background = background.crop((0, 0, 600, 800))
        background.paste(foreground, (0, 0), foreground)

        # Name
        prefix_name = Word.objects.get(id=17).text
        draw = ImageDraw.Draw(background)
        red = (0, 0, 0)
        #black = (0, 0, 0)
        text_pos = (140, 610)
        text = ' ' + prefix_name + ':    ' + member.nickname + ' '
        font = ImageFont.truetype('layijimahaniyom1.ttf', 35)
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
        text_pos = (137, 640)
        text = born_text + ':   ' + ' ' + day + ' ' + month + ' ' + year
        font = ImageFont.truetype('layijimahaniyom1.ttf', 35)
        draw.text(text_pos, text, fill=red, font=font)
        del draw

        # Dad and Mom
        prefix_parent = Word.objects.get(id=18).text
        prefix_dad_name = Word.objects.get(id=13).text
        prefix_mom_name = Word.objects.get(id=16).text

        draw = ImageDraw.Draw(background)
        red = (0, 0, 0)
        #black = (0, 0, 0)
        if member.dad_name != '':
            text_pos = (122, 670)
            text = prefix_parent + ':    ' + prefix_dad_name + member.dad_name + ' ' + prefix_mom_name + member.mom_name + " "
        else:
            text_pos = (122, 670)
            text = prefix_parent + ':    ' + prefix_mom_name + member.mom_name + " "
        font = ImageFont.truetype('layijimahaniyom1.ttf', 35)
        draw.text(text_pos, text, fill=red, font=font)
        del draw

        # branch
        prefix_branch = Word.objects.get(id=19).text
        prefix_province = Word.objects.get(id=15).text
        draw = ImageDraw.Draw(background)
        red = (0, 0, 0)
        #black = (0, 0, 0)
        text_pos = (120, 700)
        text = ' ' + prefix_branch + ':    ' + prefix_province + member.province + ' '
        font = ImageFont.truetype('layijimahaniyom1.ttf', 35)
        draw.text(text_pos, text, fill=red, font=font)
        del draw

        # Member Number
        #prefix_member_number = Word.objects.get(id=17).text

        draw = ImageDraw.Draw(background)
        white = (255, 255, 255)
        #black = (0, 0, 0)
        text_pos = (450, 460)
        #text = prefix_member_number + ' ' + str(member.id)
        text = '000' + str(member.id)
        member_id = str(member.id)
        if len(member_id) == 1 :
            text = '000' + member_id
        elif len(member_id) == 2 :
            text = '00' + member_id
        elif len(member_id) == 3 :
            text = '0' + member_id
        else:
            text = member_id
        font = ImageFont.truetype('layijimahaniyom1.ttf', 50)
        draw.text(text_pos, text, fill=white, font=font)
        del draw

        response = HttpResponse(content_type='image/png')
        # now, we tell the image to save as a PNG to the
        # provided file-like object
        background.save(response, 'PNG')

        return response # and we're done!


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

class MemberGenerateImage(TemplateView):
    form_class = MemberGenerateImageForm
    template = 'member.html'

    def get(self, request, member_id):

        form = self.form_class()

        return render(
            request,
            self.template,
            {
                'form': form,
                'member_id': member_id,
                'root_url': request.get_host()
            }
        )

    def post(self, request, member_id):
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            obj = Member.objects.get(pk=member_id)
            obj.image = form.cleaned_data['image']
            obj.save()

        return render(
            request,
            self.template,
            {
                'form': form,
                'member_id': member_id,
                'root_url': request.get_host()
            }
        )
