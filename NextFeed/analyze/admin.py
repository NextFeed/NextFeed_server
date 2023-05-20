from django.contrib import admin

# Register your models here.
from .models import User
from .models import Analyze
from .models import Picture

admin.site.register(User)
admin.site.register(Analyze)
admin.site.register(Picture)