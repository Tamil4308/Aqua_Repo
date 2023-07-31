from django.contrib import admin
from cartfish.models import Aqua,Post
# Register your models here.

class AquaAdmin(admin.ModelAdmin):
    list_display = ('id','image','fishname','orgin','quantity','price')
admin.site.register(Aqua,AquaAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ('NAME','MOBILE_NO','ENQUIRE','time')
admin.site.register(Post,PostAdmin)
