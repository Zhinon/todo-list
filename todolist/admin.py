from django.contrib import admin
from .models import Task
from .models import Prioridad
from .models import Estate

admin.site.register(Task)
admin.site.register(Prioridad)
admin.site.register(Estate)
