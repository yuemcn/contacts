from django.contrib import admin

from .models import Address
from .models import Contact

admin.site.register(Address)
admin.site.register(Contact)