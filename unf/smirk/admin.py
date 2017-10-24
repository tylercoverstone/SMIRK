# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from django.apps import apps
from .models import *

for model in apps.get_app_config('smirk').models.values():
	admin.site.register(model)

