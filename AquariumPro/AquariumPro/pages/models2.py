# -*- coding: UTF-8 -*-
from django.db import models  
from django.utils.translation import ugettext_lazy as _

# class Profile(models.Model):  
#     name = models.CharField(_("name"), max_length=255)  
#     phone = models.CharField(_("phone"), max_length=6, null=True, blank=True)

def index(request):
    name = models.CharField(_("name"), max_length=255)
    phone = models.CharField(_("phone"), max_length=6, null=True, blank=True)
    translate_str = _("這裡放需要翻譯的文字")
    context = {"translate_str": translate_str}
    return render(request, 'index.html', context)