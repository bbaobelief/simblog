# -*- coding: utf-8 -*-

import datetime
import uuid
import os
from django.views.generic.edit import FormView
from django import forms
from django.conf import settings
from .mixins.views import JSONResponseMixin


class ImageForm(forms.Form):
    img = forms.ImageField()


class ImageUpload(JSONResponseMixin, FormView):
    form_class = ImageForm
    template_name = 'blog/blog_list.html'
    upload_root = getattr(settings, 'MEDIA_ROOT', '/upload/')

    def upload_dir(self):
        today = datetime.datetime.today()
        month = today.strftime('%m')
        img_dir = 'image' + '/%d%s/' % (today.year, month)
        if not os.path.exists(self.upload_root + img_dir):
            os.makedirs(self.upload_root + img_dir)
        return img_dir

    def form_invalid(self, form):
        try:
            error = form.errors.values()[-1][-1]
        except:
            error = 'Invalid file.'
        data = {
            'success': False,
            'msg': error,
            'file_path': '',
        }
        return self.render_to_json_response(data)

    def form_valid(self, form):
        files = form.cleaned_data['img']
        suffix = files.name.split('.')[-1]
        file_name = "%s.%s" % (uuid.uuid4(), suffix)
        file_url = settings.MEDIA_URL + self.upload_dir() + file_name
        path_file = self.upload_root + self.upload_dir() + file_name
        open(path_file, 'wb').write(files.file.read())
        data = {
            'sucess': True,
            'msg': '',
            'file_path': file_url
        }
        return self.render_to_json_response(data)
