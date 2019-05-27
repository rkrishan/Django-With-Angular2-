# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Location,Family,Product,Transaction

admin.site.register(Product)
admin.site.register(Transaction)
admin.site.register(Family)
admin.site.register(Location)



# Register your models here.
