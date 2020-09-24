from django.contrib import admin

from .models import User, Survey, Questions, Answer

admin.site.register(User)
admin.site.register(Survey)
admin.site.register(Questions)
admin.site.register(Answer)
