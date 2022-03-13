from django.contrib import admin


from .models import User , School , District , Role

admin.site.register(User)
admin.site.register(School)
admin.site.register(District)
admin.site.register(Role)

